from dataclasses import dataclass, field
import random
import pygame
from constants import (
    rgbBLACK, rgbRED, rgbGREEN, rgbBLUE, rgbYELLOW, rgbCYAN, rgbMAGENTA,
    rgbGREY032, rgbGREY064, rgbGREY096, rgbGREY128, rgbGREY160, rgbGREY192,
    rgbGREY224, rgbWHITE, dirLEFT, dirRIGHT, dirUP, dirDOWN, dirSTOP,
    scrAREA, scrWIDTH, scrHEIGHT, scrSIZE
)
from ball import Ball
from bat import Bat
from wall import Wall


@dataclass
class GameState:
    scrWIDTH: int = scrWIDTH
    scrHEIGHT: int = scrHEIGHT
    scrSIZE: int = scrSIZE
    scrAREA = scrAREA

    rgbBLACK = rgbBLACK
    rgbCYAN = rgbCYAN
    rgbWHITE = rgbWHITE
    rgbGREEN = rgbGREEN
    rgbBLUE = rgbBLUE
    rgbMAGENTA = rgbMAGENTA
    rgbRED = rgbRED
    rgbYELLOW = rgbYELLOW
    rgbGREY224 = rgbGREY224
    rgbGREY192 = rgbGREY192
    rgbGREY160 = rgbGREY160
    rgbGREY128 = rgbGREY128
    rgbGREY096 = rgbGREY096
    rgbGREY064 = rgbGREY064
    rgbGREY032 = rgbGREY032

    dirSTOP = dirSTOP
    dirDOWN = dirDOWN
    dirLEFT = dirLEFT
    dirRIGHT = dirRIGHT

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
        self.gameDisplay.set_caption("Thru' The Wall")
        self.gameScreen = self.gameDisplay.set_mode(self.scrAREA)
        self.gameClock = pygame.time.Clock()

    def reset_wall(self):
        self.wall.reset()
