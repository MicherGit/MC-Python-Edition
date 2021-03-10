import pygame
pygame.init

# Set up window
screen = pygame.display.set_mode([854, 480])

# Run until the user asks to quit
running = True
while running:

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill((255, 255, 255))

    pygame.display.flip()


pygame.quit()
