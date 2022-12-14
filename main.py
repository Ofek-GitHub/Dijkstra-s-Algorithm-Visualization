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

class Box:
    def __init__(self,i, j): # we identify the box itself from the grid with I, and j.  i will through the rows, j will go through the columns.
        self.i = i
        self.j = j
        self.start = False
        self.wall = False
        self.target = False
    def draw(self, window, color):  # here we mark the box as being drawn.  #in window we talk about the grid itself
        pygame.draw.rect(window, color, (self.i * box_width, self.j * box_height, box_width - 2, box_height -2)) #some sort of margin around the grid border
        
        
# create the grid
for i in range(columns):            # short explanation, we save all the instance variables of the box within the grid array.
    arr = []
    for j in range(rows):
        arr.append(Box(i, j))
    grid.append(arr)                # in the main we will draw the boxes themselves.
    

def main():
    begin_search = False
    target_box_set = False
    target_box_start = False
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
            # start algorithm
            if event.type == pygame.KEYDOWN and target_box_set and target_box_start:
                begin_search = True
                        
                    
        window.fill(BLACK)
    
        for i in range(columns):
            for j in range(rows):
                box = grid[i][j]        # there is a BOX in the grid we give it to the object box
                box.draw(window, GREY)  # the grid is being drawn with boxes
                if box.start:
                    box.draw(window,BLUE)
                if box.target:
                    box.draw(window,GREEN)
                if box.wall:
                    box.draw(window,ORANGE)
        
        pygame.display.update()
        
main()
    