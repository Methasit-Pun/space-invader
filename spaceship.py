# spaceship.py
import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Spaceship:
    def __init__(self, image):
        self.image = image
        self.width, self.height = self.image.get_size()
        self.x = SCREEN_WIDTH // 2 - self.width // 2
        self.y = SCREEN_HEIGHT - self.height - 10
        self.speed = 10

    def move(self, dx):
        self.x += dx * self.speed
        self.x = max(0, min(SCREEN_WIDTH - self.width, self.x))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
