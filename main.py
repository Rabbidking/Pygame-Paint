import pygame

# Initialize pygame
pygame.init()

# Set the screen size
window_size = (500, 500)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Paint")

# Set the brush color
color = (0, 0, 255)

# Set a flag to keep track of the mouse button state
mouse_down = False

# Run the game loop
running = True
while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        # Detect mouse button events
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_down = False

        # Change colors depending on what key is pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = (255, 0, 0)
            elif event.key == pygame.K_g:
                color = (0, 255, 0)
            elif event.key == pygame.K_b:
                color = (0, 0, 255)

    # Continuously draw the selected color on screen
    if mouse_down:
        pygame.draw.circle(screen, color, pygame.mouse.get_pos(), 5)

    # Update the screen
    pygame.display.update()

# Quit pygame
pygame.quit()