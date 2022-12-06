from tkinter import messagebox, Tk
import pygame
import sys

window_width = 500
window_height = 500

window = pygame.display.set_mode((window_width, window_height))

def main():
    while True:
        for event in pygame.event.get():
            # quit window 
            if event.type == pygame.QUIT:   # we Creating black window 
                pygame.quit()
                sys.exit()
        
        window.fill((0, 0, 0))
        pygame.display.flip()
main()