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

# Direction Definitions
dirLEFT = -1
dirRIGHT = 1
dirUP = -1
dirDOWN = 1
dirSTOP = 0

# Screen dimensions

scrAREA = scrWIDTH, scrHEIGHT = 640, 480
scrSIZE = 20

print(type(scrAREA))

gameDisplay = pygame.display
gameScreen = gameDisplay.set_mode( scrAREA )

gameDisplay.set_caption( "Thru' The Wall" )

print( type( gameScreen ) )

gameSpeed = 120
gameExit = False
keyPressed = False

batPosX = (scrWIDTH // 2) - scrSIZE // 2
batdirX = dirSTOP
batSpeed = 4

ballPos = ballPosX, ballPosY = scrWIDTH // 2, scrHEIGHT // 2
ballDir = ballDirX, ballDirY = dirSTOP, dirDOWN

# Outer loop
while not gameExit:
    gameClock = pygame.time.Clock()
    gameRunning = True
    while gameRunning:

        # Get keypresses
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print( "Key "+str(event.key)+" Detected" )
                if event.key == pygame.K_q:
                    print( "Quit Key Pressed" )
                    gameRunning = False
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    print( "Speed Key Pressed" )
                    batSpeed = scrSIZE // 2                   
                if event.key == pygame.K_z:
                    print( "Left Key Pressed" )
                    batdirX = dirLEFT
                if event.key == pygame.K_x:
                    print( "Right Key Pressed" )
                    batdirX = dirRIGHT

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    print( "Speed Key Released" )
                    batSpeed = scrSIZE // 4
                if event.key == pygame.K_z or event.key == pygame.K_x:
                    print( "Movement Key Released" )
                    batdirX = dirSTOP

            if event.type == pygame.QUIT:
                gameRunning = False
                gameExit = True 
                
        # Update bat position
        batPosX += batSpeed * batdirX
        if batPosX < 0:
            batPosX = 0
        if batPosX > scrWIDTH - 80:
            batPosX = scrWIDTH - 80

        # Update ball position
        if ballPosX >= scrWIDTH or ballPosX <= 0:
            ballDirX = -ballDirX
        if ballPosY >= scrHEIGHT or ballPosY <= 0:
            ballDirY = -ballDirY
        ballPosX += ballDirX
        ballPosY += ballDirY

        # Collision detection with bat
        if (ballPosY >= scrHEIGHT - scrSIZE*2.5) and (batPosX <= ballPosX <= batPosX + scrSIZE*4):
            # if ball hits the left corner of the bat from the left bounce up
            # if ball hits the right corner of the bat from the right bounce up
            if ballDirX == dirSTOP:
                ballDirX = random.choice( [dirLEFT, dirRIGHT] )
            ballDirY = -ballDirY
            gameSpeed += 5

        # Missed ball detection
        if ballPosY > scrHEIGHT-scrSIZE*2:
            print( "Missed Ball!" )
            ballPosX, ballPosY = scrWIDTH // 2, scrHEIGHT // 2
            ballDirX = dirSTOP
            ballDirY = dirDOWN

        # Draw everything
        gameScreen.fill( rgbBLACK )
        pygame.draw.circle( gameScreen, rgbWHITE, (ballPosX, ballPosY), scrSIZE // 2 )
        pygame.draw.rect( gameScreen, rgbWHITE, (batPosX, scrHEIGHT - scrSIZE*2, scrSIZE*4, scrSIZE) )
        pygame.display.update()
        
        
        gameClock.tick( gameSpeed )
        
    gameExit = True

    

print( "Exiting..." )
pygame.quit()
sys.exit()


