# bullet.py
import pygame
from settings import BULLET_SPEED, BULLET_WIDTH, BULLET_HEIGHT

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = BULLET_WIDTH
        self.height = BULLET_HEIGHT
        self.speed = BULLET_SPEED
        self.state = "fired"

    def move(self):
        if self.state == "fired":
            self.y -= self.speed
            if self.y < 0:
                self.state = "ready"

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height))
