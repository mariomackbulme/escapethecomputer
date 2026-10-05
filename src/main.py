import pygame
import config
from characters import Nibble

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
pygame.display.set_caption(config.CAPTION)
clock = pygame.time.Clock()
running = True

# Load and scale the background image
board_image = pygame.image.load(config.BOARD_BRIGHT_IMG).convert_alpha()
board_image = pygame.transform.smoothscale(board_image, (config.BOARD_SIZE_WIDTH, config.BOARD_SIZE_HEIGHT))

board_image = pygame.transform.smoothscale(board_image, (config.BOARD_SIZE_WIDTH, config.BOARD_SIZE_HEIGHT))
board_rect = board_image.get_rect(center=(config.WINDOW_WIDTH // 2, config.WINDOW_HEIGHT // 2))

# Create a Nibble instance
nibble = Nibble(config.WINDOW_WIDTH // 2, config.WINDOW_HEIGHT // 2)

nibble_group = pygame.sprite.GroupSingle()
nibble_group.add(nibble)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    delta_time = clock.tick(config.FPS)

    nibble.move(delta_time)

    # Render the background and the Nibble character
    screen.fill('white')
    screen.blit(board_image, board_rect)
    
    nibble_group.draw(screen)

    pygame.display.flip()

pygame.quit()