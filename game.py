import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
SNAKE_SIZE = 20
SNAKE_SPEED = 15

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake initial position
snake_x = WIDTH // 2
snake_y = HEIGHT // 2

# Snake initial direction
snake_direction = "UP"

# Initialize the snake body
snake = [(snake_x, snake_y)]

# Food position
food_x = random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
food_y = random.randint(0, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE

# Score
score = 0

# Clock to control game speed
clock = pygame.time.Clock()

# Game over flag
game_over = False

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                snake_direction = "UP"
            if event.key == pygame.K_DOWN and snake_direction != "UP":
                snake_direction = "DOWN"
            if event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                snake_direction = "LEFT"
            if event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                snake_direction = "RIGHT"

    # Move the snake
    if snake_direction == "UP":
        snake_y -= SNAKE_SIZE
    if snake_direction == "DOWN":
        snake_y += SNAKE_SIZE
    if snake_direction == "LEFT":
        snake_x -= SNAKE_SIZE
    if snake_direction == "RIGHT":
        snake_x += SNAKE_SIZE

    # Check for collisions with the boundaries
    if snake_x < 0 or snake_x >= WIDTH or snake_y < 0 or snake_y >= HEIGHT:
        game_over = True

    # Check for collisions with itself
    if (snake_x, snake_y) in snake[:-1]:
        game_over = True

    # Add the new head to the snake
    snake.append((snake_x, snake_y))

    # Check if the snake ate the food
    if snake_x == food_x and snake_y == food_y:
        score += 1
        food_x = random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
        food_y = random.randint(0, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
    else:
        # If not, remove the tail
        snake.pop(0)

    # Clear the screen
    screen.fill(BLACK)

    # Draw the food
    pygame.draw.rect(screen, GREEN, (food_x, food_y, SNAKE_SIZE, SNAKE_SIZE))

    # Draw the snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))

    # Display the score
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, GREEN)
    screen.blit(text, (10, 10))

    pygame.display.update()

    # Control game speed
    clock.tick(SNAKE_SPEED)

# Quit the game
pygame.quit()
sys.exit()

