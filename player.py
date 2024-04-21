# player.py
import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_SPEED
from bullet import Bullet

class Player:
    def __init__(self, image):
        self.image = image
        self.width, self.height = PLAYER_WIDTH, PLAYER_HEIGHT
        self.x = SCREEN_WIDTH // 2 - self.width // 2
        self.y = SCREEN_HEIGHT - 100
        self.speed = PLAYER_SPEED

    def move(self, direction):
        if direction == "LEFT":
            self.x -= self.speed
        elif direction == "RIGHT":
            self.x += self.speed
        elif direction == "UP":
            self.y -= self.speed
        elif direction == "DOWN":
            self.y += self.speed
        # Ensure the player remains within the screen bounds
        self.x = max(0, min(SCREEN_WIDTH - self.width, self.x))
        self.y = max(0, min(SCREEN_HEIGHT - self.height, self.y))

    def shoot(self):
        return Bullet(self.x + self.width // 2, self.y)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
