import pygame
import sys

def load_scaled_image(path, size):
    try:
        image = pygame.image.load(path).convert_alpha()
        return pygame.transform.smoothscale(image, size)
    except (pygame.error, FileNotFoundError) as err:
        print(f'Error loading {path}: {err}')
        pygame.quit()
        sys.exit()