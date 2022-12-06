from tkinter import messagebox, Tk
import pygame
import sys

window_width = 500              # the width of the window
window_height = 500             # the height of the window 

window = pygame.display.set_mode((window_width, window_height))

columns = 25
rows = 25
box_width = window_width // columns     # size of the boxes
box_height = window_height // rows      # size of the boxes
grid = []

class Box:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.start = False  # where we start our search
        self.wall = False   # wall to close paths to the target
        self.target = False # where we want to go from out start to target
    def draw(self, window, color):
        pygame.draw.rect(window, color,(self.i * box_width, self.j * box_height, box_width - 2, box_height -2)) #some reason i must subtract to see the grid boxes 
         
        
# create the grid 
for i in range(columns):
    arr = [] 
    for j in range(rows):
        arr.append(Box(i, j))
    grid.append(arr)

start_box = grid[0][0]
start_box.start = True

def main():
    begin_search = False
    target_box_set = False
    start_box_set = False
    while True:
        for event in pygame.event.get():
            # quit window 
            if event.type == pygame.QUIT:   # we Creating black window 
                pygame.quit()               # quit the window thats what this block does.
                sys.exit()
            # mouse controls
            elif event.type == pygame.MOUSEMOTION: 
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                # Draw Wall
                if event.buttons[0]:    # left mouse button is pressed.
                    i = x // box_width  # we mark the boxes width that become walls.
                    j = y // box_height # we mark the boxes height that become walls.
                    grid[i][j].wall = True
                # Set Target Position
                if event.buttons[2] and not target_box_set: # we checking we havent alrdy set a target
                    i = x // box_width
                    j = y // box_height
                    target_box = grid[i][j] # where in the grid the target is located
                    target_box.target = True
                    target_box_set = True
                # Set Start Position
                if event.buttons[2] and not start_box_set: # we checking we havent alrdy set a target
                    i = x // box_width
                    j = y // box_height
                    start_box = grid[i][j] # where in the grid the start is located
                    start_box.target = True
                    start_box_set = True
                    
            # start the algorithm
            if event.type == pygame.KEYDOWN and target_box_set:
                begin_search = True
                
                    
            
        
        window.fill((0, 0, 0))
        
        for i in range(columns):
            for j in range(rows):
                box = grid[i][j]
                box.draw(window, (60, 60, 60))
                if box.start:
                    box.draw(window, (0,100,100))
                if box.wall:
                    box.draw(window, (0,200,200))
                if box.target:
                    box.draw(window, (200, 200,200))
        pygame.display.flip()               # can use display.update() as well.
main()
