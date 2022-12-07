import pygame
import math
import sys
from queue import PriorityQueue

WiDTH = 800
window = pygame.display.set_mode((WiDTH, WiDTH))
pygame.display.set_caption("Dijkstra's PATH FINDING ALGORITHM !")


RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,255,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
PURPLE = (128,0.128)
ORANGE = (255,165,0)
GREY = (128,128,128)
TURQUOISE = (64,224,208)            # pulled all the color values 

class Node: # we need to know the color to identify if we are start position or end position or wall.
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width        # WIDTH = 800 we will have aporx 50 cubes so width = 800/cubes and thats the width of the cube.
        self.y = col * width        # self.x means the row of the starting cube and self.y means the col of the starting cube
        self.color = GREY 
        self.width = width
        self.total_rows = total_rows
        self.neighbors = []
        
    def get_positions(self):
        return self.row, self.col   #We will index the positions using row and col
    
    def is_start(self): 
        return self.colored == BLUE
    
    def is_target(self):
        return self.colored == GREEN
    
    def is_barrier(self):
        return self.colored == BLACK
    def reset(self):
        self.colored = GREY
    
    while True:
        for event in pygame.event.get():
            # quit window 
            if event.type == pygame.QUIT:   # we Creating black window 
                pygame.quit()               # quit the window thats what this block does.
                sys.exit()