# assets.py
import pygame

def load_image(path, alpha=True):
    image = pygame.image.load(path)
    if alpha:
        return image.convert_alpha()
    return image.convert()

# Load enemy images
enemy_type1_img = load_image('path_to_enemy_type1.png')
enemy_type2_img = load_image('path_to_enemy_type2.png')
enemy_type3_img = load_image('path_to_enemy_type3.png')
