import pygame
import random

# Initialize the game
pygame.init()

# Set up the game window
width, height = 640, 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up the game clock
clock = pygame.time.Clock()

# Set up the snake and food
snake_pos = [[100, 50], [90, 50], [80, 50]]
snake_size = 10
snake_speed = 15
direction = "RIGHT"

food_pos = [random.randrange(1, width // 10) * 10, random.randrange(1, height // 10) * 10]
food_spawned = True

# Game over flag
game_over = False

# Game loop
while not game_over:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    # Update snake position
    if direction == "UP":
        snake_pos[0][1] -= snake_size
    elif direction == "DOWN":
        snake_pos[0][1] += snake_size
    elif direction == "LEFT":
        snake_pos[0][0] -= snake_size
    elif direction == "RIGHT":
        snake_pos[0][0] += snake_size

    # Check for collision with food
    if snake_pos[0] == food_pos:
        food_spawned = False
        snake_pos.append([0, 0])

    # Check for collision with boundaries
    if (
        snake_pos[0][0] < 0
        or snake_pos[0][0] > width
        or snake_pos[0][1] < 0
        or snake_pos[0][1] > height
    ):
        game_over = True

    # Check for collision with the snake's body
    for block in snake_pos[1:]:
        if snake_pos[0] == block:
            game_over = True

    # Move the snake
    if not game_over:
        snake_pos.insert(0, list(snake_pos[0]))
        if not food_spawned:
            food_pos = [random.randrange(1, width // 10) * 10, random.randrange(1, height // 10) * 10]
            food_spawned = True
        else:
            snake_pos.pop()

    # Clear the screen
    window.fill(BLACK)

    # Draw the snake
    for pos in snake_pos:
        pygame.draw.rect(window, GREEN, pygame.Rect(pos[0], pos[1], snake_size, snake_size))

    # Draw the food
    pygame.draw.rect(window, RED, pygame.Rect(food_pos[0], food_pos[1], snake_size, snake_size))

    # Update the display
    pygame.display.update()

    # Set the game speed
    clock.tick(snake_speed)

# Quit the game
pygame.quit()
