# pyGame.py
# A simple pygame script that initializes a window and prints types of objects.

import pygame
import random
import sys

pygame.init()

screen_area = width, height = 640, 480

print(type(screen_area))

screen = pygame.display.set_mode( screen_area )

print( type( screen ) )

print( "Exiting..." )
pygame.quit()
sys.exit()


