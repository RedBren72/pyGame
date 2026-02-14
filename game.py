from dataclasses import dataclass, field
import random
import pygame
from ball import Ball
from bat import Bat
from wall import Wall

# Constants for the original game's screen/grid size
# ZX Spectrum screen is 32 columns x 24 rows (approx)

@dataclass
class GameState:
    # Screen dimensions
    scrAREA = scrWIDTH, scrHEIGHT = 1600, 1200
    scrSIZE = 50

    # Colour Definitions
    rgbBLACK = (0, 0, 0)
    rgbRED = (200, 0, 0)
    rgbGREEN = (0, 200, 0)
    rgbBLUE = (0, 0, 200)
    rgbYELLOW = (200, 200, 0)
    rgbCYAN = (0, 200, 200)
    rgbMAGENTA = (200, 0, 200)
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

    gameSpeed: int = field(default_factory=lambda: scrHEIGHT // 5)
    score: int = 0
    level: int = 1
    exit: bool = False
    keyPressed: bool = False

    # runtime objects
    ball: Ball = None
    bat: Bat = None
    wall: Wall = None
    gameDisplay = None
    gameScreen = None
    gameClock = None

    def __post_init__(self):
        # create game objects
        self.ball = Ball(
            random.randint(-self.scrSIZE * 5, self.scrSIZE * 5) + self.scrWIDTH // 2,
            self.scrHEIGHT // 2,
            self.scrSIZE // 2,
            self.dirSTOP,
            self.dirDOWN,
            self.rgbBLACK,
        )

        self.bat = Bat(
            (self.scrWIDTH // 2) - self.scrSIZE // 2,
            self.scrHEIGHT - self.scrSIZE * 3,
            self.scrSIZE * 4,
            self.scrSIZE,
            self.rgbBLACK,
        )

        self.wall = Wall(self.scrWIDTH, self.scrHEIGHT, self.scrSIZE)

        pygame.init()
        self.gameDisplay = pygame.display
        self.gameDisplay.set_caption("Breakout")
        self.gameScreen = self.gameDisplay.set_mode(self.scrAREA)
        self.gameClock = pygame.time.Clock()

    def reset_wall(self):
        self.wall.reset()
