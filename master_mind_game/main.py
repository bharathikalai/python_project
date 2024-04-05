import random 

num = random.randrange(1000, 10000)

n = int(input("Guess the 4 digit number: "))

if (n == num):
    print("greate you guessed the number in just 1 try you are the mastermind")

else:
    print("better luck next time")
