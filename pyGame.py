# pyGame.py
# A simple pygame script that initializes a window and prints types of objects.

import pygame
import random
import sys

pygame.init()

# Constants for the original game's screen/grid size
# ZX Spectrum screen is 32 columns x 24 rows (approx)

# Colour Definitions
rgbRED = (200, 0, 0)
rgbGREEN = (0, 200, 0)
rgbBLUE = (0, 0, 200)
rgbYELLOW = (200, 200, 0)
rgbCYAN = (0, 200, 200)
rgbMAGENTA = (200, 0, 200)
rgbBLACK = (0, 0, 0)
rgbGREY032 = (32, 32, 32)
rgbGREY064 = (64, 64, 64)
rgbGREY096 = (96, 96, 96)
rgbGREY128 = (128, 128, 128)
rgbGREY160 = (160, 160, 160)
rgbGREY192 = (192, 192, 192)
rgbGREY224 = (224, 224, 224)
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

# Initialise Game Variables
gameSpeed = 120
gameExit = False
keyPressed = False

batPosX = (scrWIDTH // 2) - scrSIZE // 2
batdirX = dirSTOP
batSpeed = 4

ballPos = ballPosX, ballPosY = scrWIDTH // 2, scrHEIGHT // 2
ballDir = ballDirX, ballDirY = dirSTOP, dirDOWN

# Set up display
gameDisplay = pygame.display
gameDisplay.set_caption( "Thru' The Wall" )
gameScreen = gameDisplay.set_mode( scrAREA )

# Function to show intro screen
def showIntro():

    font = pygame.font.SysFont(None, 55)
    titleText = font.render("Thru' The Wall", True, rgbWHITE)
    directionText = font.render("Z for Left - X for Right SHIFT for Speed", True, rgbWHITE)
    instructionText = font.render("Press SPACE to Start", True, rgbWHITE)

    # Flashing screen
    gameScreen.fill( rgbGREEN )
    pygame.display.update()
    pygame.time.delay( 50 )    
    gameScreen.fill( rgbCYAN )
    pygame.display.update()
    pygame.time.delay( 50 )    
    gameScreen.fill( rgbBLUE )
    pygame.display.update()
    pygame.time.delay( 50 )    
    gameScreen.fill( rgbMAGENTA )
    pygame.display.update()
    pygame.time.delay( 50 )    
    gameScreen.fill( rgbRED )
    pygame.display.update()
    pygame.time.delay( 50 )    
    gameScreen.fill( rgbYELLOW )
    pygame.display.update()
    pygame.time.delay( 50 )    
    gameScreen.fill( rgbWHITE )
    pygame.display.update()
    pygame.time.delay( 50 )    
    gameScreen.fill( rgbGREY224 )
    gameScreen.blit(titleText, (scrWIDTH // 2 - titleText.get_width() // 2, scrHEIGHT // 3))
    pygame.display.update()
    pygame.time.delay( 50 )
    gameScreen.fill( rgbGREY192 )
    gameScreen.blit(titleText, (scrWIDTH // 2 - titleText.get_width() // 2, scrHEIGHT // 3))
    pygame.display.update()
    pygame.time.delay( 50 )
    gameScreen.fill( rgbGREY192 )
    gameScreen.blit(titleText, (scrWIDTH // 2 - titleText.get_width() // 2, scrHEIGHT // 3))
    pygame.display.update()
    pygame.time.delay( 50 )
    gameScreen.fill( rgbGREY160 )
    gameScreen.blit(titleText, (scrWIDTH // 2 - titleText.get_width() // 2, scrHEIGHT // 3))
    pygame.display.update()
    pygame.time.delay( 50 )
    gameScreen.fill( rgbGREY128 )
    gameScreen.blit(titleText, (scrWIDTH // 2 - titleText.get_width() // 2, scrHEIGHT // 3))
    pygame.display.update()
    pygame.time.delay( 50 )
    gameScreen.fill( rgbGREY096 )
    gameScreen.blit(titleText, (scrWIDTH // 2 - titleText.get_width() // 2, scrHEIGHT // 3))
    pygame.display.update()
    pygame.time.delay( 50 )
    gameScreen.fill( rgbGREY064 )
    gameScreen.blit(titleText, (scrWIDTH // 2 - titleText.get_width() // 2, scrHEIGHT // 3))
    pygame.display.update()
    pygame.time.delay( 50 )
    gameScreen.fill( rgbGREY032 )
    gameScreen.blit(titleText, (scrWIDTH // 2 - titleText.get_width() // 2, scrHEIGHT // 3))
    pygame.display.update()
    pygame.time.delay( 50 )
    gameScreen.fill( rgbBLACK )
    gameScreen.blit(titleText, (scrWIDTH // 2 - titleText.get_width() // 2, scrHEIGHT // 3))
    gameScreen.blit(directionText, (scrWIDTH // 2 - directionText.get_width() // 2, scrHEIGHT // 2))
    gameScreen.blit(instructionText, (scrWIDTH // 2 - instructionText.get_width() // 2, scrHEIGHT // 2))
    pygame.display.update()

    font = pygame.font.SysFont(None, 55)
    titleText = font.render("Thru' The Wall", True, rgbWHITE)
    instructionText = font.render("Press SPACE to Start", True, rgbWHITE)
    gameScreen.blit(titleText, (scrWIDTH // 2 - titleText.get_width() // 2, scrHEIGHT // 3))
    pygame.display.update()

# Main game loop
while not gameExit:
    gameClock = pygame.time.Clock()
    gameRunning = True

    showIntro()

    # Start loop
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    menu = False
                    

    # Game loop
    while gameRunning:

        # Get keypresses
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    gameRunning = False
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    batSpeed = scrSIZE // 2                   
                if event.key == pygame.K_z:
                    batdirX = dirLEFT
                if event.key == pygame.K_x:
                    batdirX = dirRIGHT

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    batSpeed = scrSIZE // 4
                if event.key == pygame.K_z or event.key == pygame.K_x:
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
            ballPosX, ballPosY = scrWIDTH // 2, scrHEIGHT // 2
            ballDirX = dirSTOP
            ballDirY = dirDOWN

        # Draw everything
        gameScreen.fill( rgbCYAN )
        pygame.draw.circle( gameScreen, rgbBLACK, (ballPosX, ballPosY), scrSIZE // 2 )
        pygame.draw.rect( gameScreen, rgbBLACK, (batPosX, scrHEIGHT - scrSIZE*2, scrSIZE*4, scrSIZE) )
        pygame.display.update()
        
        
        gameClock.tick( gameSpeed )
        
    gameExit = True

    

print( "Exiting..." )
pygame.quit()
sys.exit()


