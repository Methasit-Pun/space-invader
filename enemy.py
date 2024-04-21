# enemy.py
import pygame
from settings import ENEMY_WIDTH, ENEMY_HEIGHT, ENEMY_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT
from assets import enemy_type1_img, enemy_type2_img, enemy_type3_img
class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = ENEMY_WIDTH
        self.height = ENEMY_HEIGHT
        self.speed = ENEMY_SPEED

    def move(self):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))

class EnemyType1(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.dx = self.speed
        self.image = enemy_type1_img

    def move(self):
        self.x += self.dx
        if self.x <= 0 or self.x + self.width >= SCREEN_WIDTH:
            self.dx *= -1

class EnemyType2(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.dy = self.speed
        self.image = enemy_type2_img

    def move(self):
        self.y += self.dy
        if self.y >= SCREEN_HEIGHT:
            self.y = -self.height  # Reset to top if it goes beyond the screen

class EnemyType3(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.dx = self.speed
        self.dy = self.speed
        self.image = enemy_type3_img

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x <= 0 or self.x + self.width >= SCREEN_WIDTH:
            self.dx *= -1
        if self.y < 0 or self.y + self.height >= SCREEN_HEIGHT:
            self.dy *= -1
