import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Font for displaying text
font = pygame.font.Font(None, 36)

# Snake and food initialization
snake = [(100, 100), (90, 100), (80, 100)]  # Initial snake body
snake_dir = (CELL_SIZE, 0)  # Initial direction (moving right)
food = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
        random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)

# Game variables
running = True
score = 0

def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE))

def draw_food(food):
    pygame.draw.rect(screen, RED, pygame.Rect(food[0], food[1], CELL_SIZE, CELL_SIZE))

def move_snake(snake, direction):
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake = [head] + snake[:-1]
    return snake

def check_collision(snake):
    head = snake[0]
    # Check if the snake collides with the walls
    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        return True
    # Check if the snake collides with itself
    if head in snake[1:]:
        return True
    return False

def grow_snake(snake):
    tail = snake[-1]
    snake.append(tail)

def show_start_menu():
    screen.fill(BLACK)
    title_text = font.render("Snake Game", True, WHITE)
    start_text = font.render("Press SPACE to Start", True, WHITE)
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 3))
    screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False

def show_score(score):
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

# Show the start menu
show_start_menu()

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_dir != (0, CELL_SIZE):
        snake_dir = (0, -CELL_SIZE)
    if keys[pygame.K_DOWN] and snake_dir != (0, -CELL_SIZE):
        snake_dir = (0, CELL_SIZE)
    if keys[pygame.K_LEFT] and snake_dir != (CELL_SIZE, 0):
        snake_dir = (-CELL_SIZE, 0)
    if keys[pygame.K_RIGHT] and snake_dir != (-CELL_SIZE, 0):
        snake_dir = (CELL_SIZE, 0)

    # Move the snake
    snake = move_snake(snake, snake_dir)

    # Check for collisions
    if check_collision(snake):
        print(f"Game Over! Your score: {score}")
        running = False

    # Check if the snake eats the food
    if snake[0] == food:
        grow_snake(snake)
        food = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)
        score += 1

    # Draw everything
    screen.fill(BLACK)
    draw_snake(snake)
    draw_food(food)
    show_score(score)
    pygame.display.flip()

    # Control the frame rate
    clock.tick(10)

# Quit Pygame
pygame.quit()