import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Horizontal Gradient Rectangle")

# Define the gradient colors
start_color = (221, 7, 99) # Starting color (red)
end_color = (25, 14, 93)     # Ending color (blue)

# Define the rectangle position and size
rect_x, rect_y = 100, 100
rect_width, rect_height = 400, 200

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the gradient rectangle
    for x in range(rect_width):
        # Calculate the color at this column using linear interpolation
        t = x / rect_width
        color = [int(start_color[c] * (1 - t) + end_color[c] * t) for c in range(3)]
        pygame.draw.rect(screen, color, (rect_x + x, rect_y, 1, rect_height))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
