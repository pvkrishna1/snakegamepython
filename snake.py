import pygame
import time

# Initialize pygame
pygame.init()

# Set the size of the window
width = 500
height = 500

# Create the window
win = pygame.display.set_mode((width, height))

# Set the title of the window
pygame.display.set_caption("Snake Game")

# Set the starting position of the snake
x = 50
y = 50

# Set the size of each snake segment
segment_width = 10
segment_height = 10

# Set the initial length of the snake
length = 1

# Set the initial direction of the snake
x_change = 0
y_change = 0

# Set the initial speed of the snake
speed = 10

# Set the initial color of the snake
color = (255, 0, 0)

# Create a clock to control the speed of the game
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the snake
    x += x_change
    y += y_change

    # Draw the snake
    pygame.draw.rect(win, color, (x, y, segment_width, segment_height))

    # Update the screen
    pygame.display.update()

    # Set the speed of the game
    clock.tick(speed)

# Quit pygame
pygame.quit()
