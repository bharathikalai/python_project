hight = 10
width = 20

snake = [(hight//2,width//2)]

print("the value of snake",snake)

# head_x,head_y = snake[0]

# print("the value of head x", head_x)
# print("the value of head y", head_y)


# new_head = (head_x,head_y - 1)
# print("the value of new_head is head of ",new_head
      
#       )

# new_head = (5,10)
# if new_head in snake:
#     print("there is same value in snake and new head")
# else:
#     print("no value match ")
import random

WIDTH = 20
HEIGHT = 10

food = (random.randint(0, WIDTH-1), random.randint(0, HEIGHT-1))
print("the value of food is ",food)

new_head = (5,9)

snake.insert(0,new_head)

print("the value of insert snake is ",snake)

snake.pop()
print("the pop method value of snake",snake)

