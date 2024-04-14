import os 
import time
import random

# x = 5
# y = 5

# for x in range(x):
#     print(x,"the value of x")
#     for y in range(y):
#         print(y,"the value of y")


# x = 5
# y = 5

# for i in range(x):
#     print(i, "the value of x")
#     for j in range(y):
#         print(j, "the value of y")



# width = 20

# hight = 10

# snake = [(width//2,hight//2)]

# #the data type of snake is tuple


# head_x,head_y = snake[0]

# # here by using [0] i am access the first index of tuple value

# print(head_x,"the value of head x")
# print(head_y,"the value of head y")



#lets decoding the first function 

# Function to print the game board
# Define constants
# WIDTH = 20
# HEIGHT = 10
# SNAKE_CHAR = 'O'
# FOOD_CHAR = '*'
# EMPTY_CHAR = ' '

# # Initialize variables
# snake = [(WIDTH//2, HEIGHT//2)]
# print("snake",snake)
# food = (random.randint(0, WIDTH-1), random.randint(0, HEIGHT-1))
# print("food",food)
# direction = 'RIGHT'
# score = 0

# def print_board():
#     # os.system('cls' if os.name == 'nt' else 'clear')
#     for y in range(HEIGHT):
#         for x in range(WIDTH):
#             if (x, y) == snake[0]:
#                 print(SNAKE_CHAR, end='')
#             elif (x, y) == food:
#                 print(FOOD_CHAR, end='')
#             elif (x, y) in snake[1:]:
#                 print('#', end='')
#             else:
#                 print(EMPTY_CHAR, end='')
#         print()

# print_board()
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
def move_snake():
    global snake, food, direction,score

    head_x,head_y = snake[0]

    if direction == 'UP':
        new_head = (head_x,head_y -1)
    elif direction == 'DOWN':
        new_head = (head_x,head_y + 1)
    elif direction == 'LEFT':
        new_head = (head_x - 1,head_y)
    elif direction == 'RIGHT':
        new_head = (head_x + 1,head_y)
    
    if (
        new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT or
        new_head in snake

    ):
        print("game over your score:",score)

    #calculate new head position based on the direction

    snake.insert(0,new_head)

    if new_head == food:
        food = (random.randint(0, WIDTH-1), random.randint(0, HEIGHT-1))
        score +=1
    else:
        snake.pop()

while True:
    print_board()
    move_snake()

    #get user input for direction
    key = input("enter direction (w/a/s/d): ").upper()

    if key == 'W':
        direction = 'UP'
    elif key == 'S':
        direction = 'DOWN'
    elif key == 'A':
        direction = 'LEFT'
    elif key == 'D':
        direction = 'RIGHT'




