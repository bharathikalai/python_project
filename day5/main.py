import random
import os
import time

# Define constants
WIDTH = 20
HEIGHT = 10
SNAKE_CHAR = 'O'
FOOD_CHAR = '*'
EMPTY_CHAR = ' '

# Initialize variables
snake = [(WIDTH//2, HEIGHT//2)]
food = (random.randint(0, WIDTH-1), random.randint(0, HEIGHT-1))
direction = 'RIGHT'
score = 0

# Function to print the game board
def print_board():
    os.system('cls' if os.name == 'nt' else 'clear')
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) == snake[0]:
                print(SNAKE_CHAR, end='')
            elif (x, y) == food:
                print(FOOD_CHAR, end='')
            elif (x, y) in snake[1:]:
                print('#', end='')
            else:
                print(EMPTY_CHAR, end='')
        print()

# Function to move the snake
def move_snake():
    global snake, food, direction, score

    head_x, head_y = snake[0]

    # Calculate new head position based on the direction
    if direction == 'UP':
        new_head = (head_x, head_y - 1)
    elif direction == 'DOWN':
        new_head = (head_x, head_y + 1)
    elif direction == 'LEFT':
        new_head = (head_x - 1, head_y)
    elif direction == 'RIGHT':
        new_head = (head_x + 1, head_y)

    # Check if the snake has hit the wall or itself
    if (
        new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT or
        new_head in snake
    ):
        print("Game Over! Your Score:", score)
        exit(0)

    # Move the snake and check if it has eaten the food
    snake.insert(0, new_head)
    if new_head == food:
        food = (random.randint(0, WIDTH-1), random.randint(0, HEIGHT-1))
        score += 1
    else:
        snake.pop()

# Main game loop
while True:
    print_board()
    move_snake()

    # Get user input for direction
    key = input("Enter direction (W/A/S/D): ").upper()
    if key == 'W':
        direction = 'UP'
    elif key == 'S':
        direction = 'DOWN'
    elif key == 'A':
        direction = 'LEFT'
    elif key == 'D':
        direction = 'RIGHT'
