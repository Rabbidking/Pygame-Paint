import pygame
import datetime

# Initialize pygame
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
VIOLET = (148, 0, 211)
INDIGO = (75, 0, 130)
YELLOW = (255, 255, 0)
ORANGE = (255, 127, 0)

# Set the screen size
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Paint")

# Set the background color to white
screen.fill(WHITE)

# Create a separate surface for the swatch HUD
swatch_surface_width = 40
swatch_surface_height = screen_height
swatch_surface = pygame.Surface((swatch_surface_width, swatch_surface_height))
swatch_surface.fill((200, 200, 200))

# Define a dictionary of color swatches
swatches = {
    RED: (10, 20),
    ORANGE: (10, 50),
    YELLOW: (10, 80),
    GREEN: (10, 110),
    BLUE: (10, 140),
    INDIGO: (10, 170),
    VIOLET: (10, 200),
    BLACK: (10, 230),
    WHITE: (10, 260),
}

# Set the initial brush color to blue
color = BLUE

# Set a flag to keep track of the mouse button state
mouse_down = False

# Set a flag to keep track of whether to save the image
save_image = False

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Mouse events
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse click is within the canvas area
            if event.pos[0] > swatch_surface_width:
                mouse_down = True
            else:
                # Check if the mouse click is on a swatch
                for swatch_color, swatch_pos in swatches.items():
                    if pygame.Rect(swatch_pos, (20, 20)).collidepoint(event.pos):
                        color = swatch_color
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_down = False

        # Key events
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = RED
            elif event.key == pygame.K_g:
                color = GREEN
            elif event.key == pygame.K_b:
                color = BLUE
            elif event.key == pygame.K_v:
                color = VIOLET
            elif event.key == pygame.K_i:
                color = INDIGO
            elif event.key == pygame.K_y:
                color = YELLOW
            elif event.key == pygame.K_o:
                color = ORANGE
            elif event.key == pygame.K_s:
                save_image = True

    if mouse_down:
        # Check if the mouse is within the canvas area
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[0] > swatch_surface_width:
            pygame.draw.circle(screen, color, mouse_pos, 5)

    # Draw the color swatches on the swatch surface
    for swatch_color, swatch_pos in swatches.items():
        pygame.draw.rect(swatch_surface, swatch_color, pygame.Rect(swatch_pos, (20, 20)))

    # Draw the swatch surface on top of the canvas surface
    screen.blit(swatch_surface, (0, 0))

    pygame.display.update()

    # Save the image as a PNG
    if save_image:
        filename = datetime.datetime.now().strftime("drawing-%Y%m%d-%H%M%S.png")
        pygame.image.save(screen, filename)
        save_image = False

# Quit pygame
pygame.quit()
