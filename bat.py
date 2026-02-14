import pygame
from constants import dirSTOP, dirLEFT, dirRIGHT

class Bat:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.direction = dirSTOP
        self.speed = 4
    
    def update(self, width):
        """Update bat position based on direction and speed"""
        self.x += self.speed * self.direction
        
        # Keep bat within screen bounds
        if self.x < 0:
            self.x = 0
        if self.x > width - self.width:
            self.x = width - self.width
    
    def set_direction(self, direction):
        """Set the direction of movement"""
        self.direction = direction
    
    def set_speed(self, speed):
        """Set the speed of movement"""
        self.speed = speed
    
    def get_rect(self):
        """Return pygame Rect for collision detection"""
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    def draw(self, screen):
        """Draw the bat on screen"""
        pygame.draw.rect(screen, self.color, self.get_rect())
    
    def check_collision(self, ball_obj):
        """Check for collision with ball and handle bouncing"""
        if self.get_rect().colliderect(pygame.Rect(ball_obj.x - ball_obj.radius, ball_obj.y - ball_obj.radius, ball_obj.radius * 2, ball_obj.radius * 2)):
            # If the ball is currently not moving horizontally, bounce it towards the side of the bat.
            if ball_obj.dx == dirSTOP:
                if ball_obj.x < self.x + self.width / 2:
                    ball_obj.dx = dirLEFT
                else:
                    ball_obj.dx = dirRIGHT

            ball_obj.dy = -ball_obj.dy
            return True  # Return True to indicate collision occurred
        return False
