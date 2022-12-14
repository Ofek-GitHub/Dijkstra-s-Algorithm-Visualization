from tkinter import messagebox, Tk
import pygame
import math
import sys

window_width = 500
window_height = 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Dijkstra's PATH FINDING ALGORITHM !")

columns = 25
rows = 25               

box_width = window_width //columns # this will be the width of each tiny box inside the window
box_height = window_height //rows # this will be the height of each, #essentially we took the large grid and divide it with the columns and rows to tiny boxes

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0 ,0, 255)
YELLOW = (255,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
PURPLE = (128,0.128)
ORANGE = (255,165,0)
GREY = (128,128,128)
TURQUOISE = (64,224,208)            # pulled all the color values 

grid = []           # this empty array is going to store all this individual boxes in the grid
queue = [] # this empty array is going to store all this individual boxes in the queue for building the best path!
path = [] # this empty array is going to store all this individual boxes in the path

class Box:
    def __init__(self,i, j): # we identify the box itself from the grid with I, and j.  i will through the rows, j will go through the columns.
        self.i = i
        self.j = j
        self.start = False
        self.wall = False
        self.target = False
        self.queued = False # this line and the next two lines were added after i finished the grid to continue processing the algorithm itself.
        self.visited = False    # there is the neighbors above and below and from the left side to the right side of the box ! important to remember this.
        self.neighbors = []
        self.prior = None 
    
    def draw(self, window, color):  # here we mark the box as being drawn.  #in window we talk about the grid itself
        pygame.draw.rect(window, color, (self.i * box_width, self.j * box_height, box_width - 2, box_height -2)) #some sort of margin around the grid border
    
    def set_neighbors(self):
        if self.i > 0:
            self.neighbors.append(grid[self.i - 1][self.j])     # checking if im not in the first row so i wont get out of bounds and adding the neighbor from above.
        if self.i < columns - 1:                            # same check for the last row.
            self.neighbors.append(grid[self.i + 1][self.j]) # adding the neighbor from below 
        if self.j > 0:
            self.neighbors.append(grid[self.i][self.j - 1]) # im doing it for the left side neighbor as well as the right side neighbor in the next line :)
        if self.j < rows - 1:
            self.neighbors.append(grid[self.i][self.j + 1]) # adding the neighbor from the right side.
        
# create the grid
for i in range(columns):            # short explanation, we save all the instance variables of the box within the grid array.
    arr = []
    for j in range(rows):
        arr.append(Box(i, j))
    grid.append(arr)                # in the main we will draw the boxes themselves.
    
# set Neighbors
for i in range(columns):
    for j in range(rows):
        grid[i][j].set_neighbors()
        

def main():
    begin_search = False
    target_box_set = False
    target_box_start = False
    searching = True # this variable going to help us interrupt the algorithm once the end point is find. 
    target_box = None
    while True:
        for event in pygame.event.get():
            #quit window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                # draw wall
                if event.buttons[0]:
                    i = x // box_width 
                    j = y // box_height
                    grid[i][j].wall = True
                # set target position
                if event.buttons[2] and not target_box_set:
                    i = x //box_width
                    j = y //box_height
                    target_box = grid[i][j]
                    target_box.target = True
                    target_box_set = True
                # set start position
                if event.buttons[1] and not target_box_start:
                    i = x //box_width
                    j = y //box_height
                    start_box = grid[i][j]
                    start_box.start = True
                    target_box_start = True
                    start_box.visited = True # set start position and update it for the algorithm ofc this is visited, since its where we start.
                    start_box.prior = None
                    queue.append(start_box)
            # start algorithm
            if event.type == pygame.KEYDOWN and target_box_set and target_box_start:
                begin_search = True
        if begin_search:
            if len(queue) > 0  and searching :  # we check if the len of queue is bigger then 0 and searching = true
                current_box =queue.pop(0)       # current box equal for the first box in the que, will be the start box first of! afterwards will get rid of it.
                current_box.visited = True      #
                if current_box == target_box:
                    searching = False # to interrupt the algo, because we finished.
                    while current_box.prior != start_box:
                        path.append(current_box.prior)  # in this while loop, we append boxes to array call path that is the Dijkstra algorithm ! that shows shortest path.
                        current_box = current_box.prior
                else:
                    for neighbor in current_box.neighbors:
                        if not neighbor.queued and not neighbor.wall:
                            neighbor.queued = True
                            queue.append(neighbor)  # this else contains for loop iteration for all the neighbor in the current box.
                                                     # if the neighbor not yet been added to the que, and he is not a wall box, we will add it to the que to check it later.
            else:
                if searching :
                    Tk().wm_withdraw()
                    messagebox.showinfo("No solution found")        # A pop up window.
                    searching = False
                    
                    
                        
                    
        window.fill(BLACK)
    
        for i in range(columns):
            for j in range(rows):
                box = grid[i][j]        # there is a BOX in the grid we give it to the object box
                box.draw(window, GREY)  # the grid is being drawn with boxes
                
                if box.queued:
                    box.draw(window, RED)   # the box is being drawn RED if is queued and not yet visited
                if box.visited:
                    box.draw(window,GREEN)
                if box in path:
                    box.draw(window, ORANGE) 
                if box.start:
                    box.draw(window,TURQUOISE)
                if box.target:
                    box.draw(window,YELLOW)
                if box.wall:
                    box.draw(window,BLACK)
        
        pygame.display.update()
        
main()
    