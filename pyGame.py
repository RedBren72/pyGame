# A simple pygame implementation of the ZX Spectrum game "Thru' The Wall"
# Original game by Costa Panayi
# Pygame version by ChatGPT 4.0


import pygame
import random
import sys

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
scrAREA = scrWIDTH, scrHEIGHT = 1600, 1200
scrSIZE = 50

# Initialise Game Variables
gameSpeed = scrHEIGHT//10
gameScore = 0
gameExit = False
keyPressed = False

batPosX = (scrWIDTH // 2) - scrSIZE // 2
batdirX = dirSTOP
batSpeed = 4

ballPos = ballPosX, ballPosY = scrWIDTH // 2, scrHEIGHT // 2
ballDir = ballDirX, ballDirY = dirSTOP, dirDOWN

# Set up display
pygame.init()
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
    pygame.time.delay( 200 )    
    gameScreen.fill( rgbCYAN )
    pygame.display.update()
    pygame.time.delay( 200 )    
    gameScreen.fill( rgbBLUE )
    pygame.display.update()
    pygame.time.delay( 200 )    
    gameScreen.fill( rgbMAGENTA )
    pygame.display.update()
    pygame.time.delay( 200 )    
    gameScreen.fill( rgbRED )
    pygame.display.update()
    pygame.time.delay( 200 )    
    gameScreen.fill( rgbYELLOW )
    pygame.display.update()
    pygame.time.delay( 200 )    
    gameScreen.fill( rgbWHITE )
    pygame.display.update()
    pygame.time.delay( 100 )    
    gameScreen.fill( rgbGREY224 )
    gameScreen.blit(titleText, (scrWIDTH // 2 - titleText.get_width() // 2, scrHEIGHT // 4))
    pygame.display.update()
    pygame.time.delay( 100 )
    gameScreen.fill( rgbGREY192 )
    gameScreen.blit(titleText, (scrWIDTH // 2 - titleText.get_width() // 2, scrHEIGHT // 4))
    pygame.display.update()
    pygame.time.delay( 100 )
    gameScreen.fill( rgbGREY192 )
    gameScreen.blit(titleText, (scrWIDTH // 2 - titleText.get_width() // 2, scrHEIGHT // 4))
    pygame.display.update()
    pygame.time.delay( 100 )
    gameScreen.fill( rgbGREY160 )
    gameScreen.blit(titleText, (scrWIDTH // 2 - titleText.get_width() // 2, scrHEIGHT // 4))
    pygame.display.update()
    pygame.time.delay( 100 )
    gameScreen.fill( rgbGREY128 )
    gameScreen.blit(titleText, (scrWIDTH // 2 - titleText.get_width() // 2, scrHEIGHT // 4))
    pygame.display.update()
    pygame.time.delay( 100 )
    gameScreen.fill( rgbGREY096 )
    gameScreen.blit(titleText, (scrWIDTH // 2 - titleText.get_width() // 2, scrHEIGHT // 4))
    pygame.display.update()
    pygame.time.delay( 100 )
    gameScreen.fill( rgbGREY064 )
    gameScreen.blit(titleText, (scrWIDTH // 2 - titleText.get_width() // 2, scrHEIGHT // 4))
    pygame.display.update()
    pygame.time.delay( 100 )
    gameScreen.fill( rgbGREY032 )
    gameScreen.blit(titleText, (scrWIDTH // 2 - titleText.get_width() // 2, scrHEIGHT // 4))
    pygame.display.update()
    pygame.time.delay( 100   )
    gameScreen.fill( rgbBLACK )
    gameScreen.blit(titleText, (scrWIDTH // 2 - titleText.get_width() // 2, scrHEIGHT // 4))
    gameScreen.blit(directionText, (scrWIDTH // 2 - directionText.get_width() // 2, scrHEIGHT // 2))
    gameScreen.blit(instructionText, (scrWIDTH // 2 - instructionText.get_width() // 2, scrHEIGHT * 3 // 4))
    pygame.display.update()
    pygame.time.delay( 500 )
    


# Function to create walls
def createWalls():
    # The wall is an array of bricks
    # Bricks are rectangles with width = size scrSIZE x 2 and height = scrSIZE
    # Half-Bricks are rectangles with width = scrSIZE and height = scrSIZE
    # There are 5 rows of bricks
    # Each row is a different colour but all bricks have a black border
    # The wall is as wide as the screen
    # The odd rows have full bricks only
    # The even rows start and end with half-bricks
    # Brick positions are stored in a 2D array
    wall = []
    brickColours = [ rgbRED, rgbGREEN, rgbMAGENTA, rgbYELLOW, rgbBLUE ]
    for row in range(5):
        brickRow = []
        yPos = (3+row) * scrSIZE
        if row % 2 == 0:
            # Odd row - full bricks only
            for col in range(scrWIDTH // (scrSIZE * 2)):
                xPos = col * scrSIZE * 2
                brickRect = pygame.Rect(xPos, yPos, scrSIZE * 2, scrSIZE)
                brickRow.append( (brickRect, brickColours[row]) )
        else:
            # Even row - half-bricks at start and end
            halfBrickRectStart = pygame.Rect(0, yPos, scrSIZE, scrSIZE)
            brickRow.append( (halfBrickRectStart, brickColours[row]) )
            for col in range(1, (scrWIDTH // (scrSIZE * 2))):
                xPos = col * scrSIZE * 2 - scrSIZE
                brickRect = pygame.Rect(xPos, yPos, scrSIZE * 2, scrSIZE)
                brickRow.append( (brickRect, brickColours[row]) )
            halfBrickRectEnd = pygame.Rect(scrWIDTH - scrSIZE, yPos, scrSIZE, scrSIZE)
            brickRow.append( (halfBrickRectEnd, brickColours[row]) )
        wall.append(brickRow)    
        
    return wall

# Display the wall five rows down from the top
def displayWall(wall):
    for row in wall:
        for brick, colour in row:
            pygame.draw.rect(gameScreen, colour, brick)
            pygame.draw.rect(gameScreen, rgbBLACK, brick, 1)  # Black border
            

# Main game loop
while not gameExit:
    gameClock = pygame.time.Clock()

    showIntro()

    # Menu loop
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
                    gameRunning = True
                    menu = False
                    
    wall = createWalls()

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
        if batPosX > scrWIDTH - scrSIZE * 4:
            batPosX = scrWIDTH - scrSIZE * 4

        # Update ball position
        if ballPosX >= ( scrWIDTH - scrSIZE // 2 ) or ballPosX <= scrSIZE // 2:
            ballDirX = -ballDirX
        if ballPosY >= ( scrHEIGHT - scrSIZE // 2 ) or ballPosY <= scrSIZE // 2:
            ballDirY = -ballDirY
        ballPosX += ballDirX
        ballPosY += ballDirY

        # Collision detection with bat
        if ( scrHEIGHT - scrSIZE*3.5 <= ballPosY <= scrHEIGHT - scrSIZE * 2.5) and (batPosX - scrSIZE*1.5 <= ballPosX <= batPosX + scrSIZE*4.5):
            # if ball hits the left corner of the bat from the left bounce up
            # if ball hits the right corner of the bat from the right bounce up
            if ballDirX == dirSTOP:
                ballDirX = random.choice( [dirLEFT, dirRIGHT] )
            ballDirY = -ballDirY
            gameScore += 1

        # Missed ball detection
        if ballPosY > scrHEIGHT-scrSIZE*2.5:
            ballPosX, ballPosY = scrWIDTH // 2, scrHEIGHT // 2
            ballDirX = dirSTOP
            ballDirY = dirDOWN

        # Collision detection with bricks
        # Check wall in reverse order so that bricks are removed correctly
        for row in reversed(wall):
            for brick, colour in row:
                # check the edge of the ball against the brick
                if brick.collidepoint(ballPosX + ( ballDirX * scrSIZE // 2 ), ballPosY + ( ballDirY * scrSIZE // 2 ) ):
                    row.remove( (brick, colour) )
                    ballDirY = -ballDirY
                    gameScore += 5 * ( len(wall) - wall.index(row) )
                    # if ball hits the side of a brick, reverse X direction
                    #if (ballPosX <= brick.left) or (ballPosX >= brick.right):
                    #    ballDirX = -ballDirX

        # Draw everything
        gameScreen.fill( rgbCYAN )
        displayWall( wall )
        pygame.draw.circle( gameScreen, rgbBLACK, (ballPosX, ballPosY), scrSIZE // 2 )
        pygame.draw.rect( gameScreen, rgbBLACK, (batPosX, scrHEIGHT - scrSIZE*3, scrSIZE*4, scrSIZE) )
        font = pygame.font.SysFont(None, 35)
        scoreText = font.render("Score: " + str(gameScore), True, rgbBLACK)
        gameScreen.blit(scoreText, (10, scrHEIGHT - scrSIZE))
        pygame.display.update()        
        
        gameClock.tick( gameSpeed )
        
    gameExit = True

    

print( "Exiting..." )
pygame.quit()
sys.exit()


