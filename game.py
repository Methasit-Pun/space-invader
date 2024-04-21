# game.py
import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_SPEED, BULLET_SPEED, ENEMY_WIDTH, ENEMY_HEIGHT
import sys
from player import Player
from enemy import EnemyType1, EnemyType2, EnemyType3
from bullet import Bullet
import random
import time

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF)
        pygame.display.set_caption('Space Invaders Wave System')
        self.running = True
        self.player = Player()  # Assume player has a default image set
        self.enemies = []
        self.bullets = []
        self.score = 0
        self.boss_active = False
        self.wave_number = 0
        self.last_wave_time = time.time()
        self.spawn_delay = 0.5
        self.max_enemies_per_wave = 10  # Adjust as needed

    def reset_wave(self):
        self.wave_number += 1
        self.enemies.clear()
        if self.wave_number % 2 == 0:
            self.boss_active = True
            # Boss specific settings
        else:
            self.boss_active = False
            # Normal wave settings

    def spawn_enemy(self):
        enemy_type = random.choice([EnemyType1, EnemyType2, EnemyType3])
        enemy = enemy_type(random.randint(0, SCREEN_WIDTH - ENEMY_WIDTH), 0)
        self.enemies.append(enemy)

    def fire_bullet(self):
        bullet = self.player.shoot()
        self.bullets.append(bullet)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.move("LEFT")
                elif event.key == pygame.K_RIGHT:
                    self.player.move("RIGHT")
                elif event.key == pygame.K_SPACE:
                    self.fire_bullet()

    def update(self):
        for bullet in self.bullets:
            bullet.move()
            if bullet.state == "ready":
                self.bullets.remove(bullet)
        for enemy in self.enemies:
            enemy.move()
            if enemy.y > SCREEN_HEIGHT:  # If enemy moves out of screen, remove it
                self.enemies.remove(enemy)

    def draw(self):
        self.screen.fill((0, 0, 0))  # Clear screen
        self.player.draw(self.screen)
        for bullet in self.bullets:
            bullet.draw(self.screen)
        for enemy in self.enemies:
            enemy.draw(self.screen)
        pygame.display.flip()

    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            clock.tick(60)  # Maintain 60 FPS
        pygame.quit()
        sys.exit()

# Entry point
if __name__ == "__main__":
    game = Game()
    game.run()
