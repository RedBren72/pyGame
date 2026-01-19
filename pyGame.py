# pyGame.py
# A simple pygame script that initializes a window and prints types of objects.

import pygame
import random
import sys

pygame.init()

# Constants for the original game's screen/grid size
# ZX Spectrum screen is 32 columns x 24 rows (approx)

# Colour Definitions
rgbBLACK = (0, 0, 0)
rgbRED = (200, 0, 0)
rgbGREEN = (0, 200, 0)
rgbBLUE = (0, 0, 200)
rgbYELLOW = (200, 200, 0)
rgbCYAN = (0, 200, 200)
rgbMAGENTA = (200, 0, 200)
rgbWHITE = (255, 255, 255)

# Screen dimensions

scrAREA = scrWIDTH, scrHEIGHT = 640, 480
scrSIZE = 20

print(type(scrAREA))

gameDisplay = pygame.display
gameScreen = gameDisplay.set_mode( scrAREA )

gameDisplay.set_caption( "Thru' The Wall" )

print( type( gameScreen ) )

gameExit = False
keyCount = 0
batPosX = (scrWIDTH // 2) - 2
ballPosX = scrWIDTH // 2
ballPosY = scrHEIGHT // 2
ballDirX = -1

# Outer loop
while not gameExit:
    
    # We only move when the keycount is zero
    if keyCount < 100:
        keyCount += 1
    else:
        keyCount = 0

        keyPressed = pygame.key.get_pressed()
        if keyPressed[ pygame.K_LSHIFT ]:
            print( "Speed Key Pressed" )
        if keyPressed[ pygame.K_z ]:
            print( "Left Key Pressed" )
        if keyPressed[ pygame.K_x ]:
            print( "Right Key Pressed" )
        if keyPressed[ pygame.K_q ]:
            print( "Quit Key Pressed" )
            gameExit = True



    gameScreen.fill( rgbBLACK )
    pygame.display.update()
    

print( "Exiting..." )
pygame.quit()
sys.exit()


