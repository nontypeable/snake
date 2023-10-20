import pygame

window_size_x, window_size_y = 800, 600

pygame.init()
pygame.display.set_caption("Snake")
window = pygame.display.set_mode((window_size_x, window_size_y))
clock = pygame.time.Clock()

is_running = True
while is_running:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
