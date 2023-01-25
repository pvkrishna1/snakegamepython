import pygame
import time

# Initialize pygame and create a window
pygame.init()
width = 500
height = 500
screen = pygame.display.set_mode((width, height))

# Create a snake and food
snake = [(200, 200), (210, 200), (220, 200)]
food = (250, 250)

# Set initial score and movement direction
score = 0
direction = 'right'

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the snake in the current direction
    if direction == 'right':
        snake[0] = (snake[0][0] + 10, snake[0][1])
    elif direction == 'left':
        snake[0] = (snake[0][0] - 10, snake[0][1])
    elif direction == 'up':
        snake[0] = (snake[0][0], snake[0][1] - 10)
    elif direction == 'down':
        snake[0] = (snake[0][0], snake[0][1] + 10)

    # Check if the snake has hit the food
    if snake[0][0] == food[0] and snake[0][1] == food[1]:
        food = (snake[0][0]+10, snake[0][1]+10)
        score += 1

    # Move the rest of the snake
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    # Draw the snake and food
    screen.fill((0, 0, 0))
    for pos in snake:
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(food[0], food[1], 10, 10))
    pygame.display.set_caption("Score: " + str(score))
    pygame.display.flip()

    # Handle key presses for movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        direction = 'left'
    elif keys[pygame.K_RIGHT]:
        direction = 'right'
    elif keys[pygame.K_UP]:
        direction = 'up'
    elif keys[pygame.K_DOWN]:
        direction = 'down'

    # Wait for a bit
    time.sleep(0.1)

# Exit the game
pygame.quit()
