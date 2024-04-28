
#project 1 debug


poweres = [2,3,4,5]   # this is the input of powers

mini,maxi = 0,0       # initate the maxi and min 

for power in poweres:    # this loop will execute 4 time because powers variable has 4 list
    if mini == 0 and maxi == 0:   # first itteration this if condtion will be true
        mini,maxi = poweres[0],poweres[0]  # set the value of powers first index the first index is 2 so mini and maxi is 2
        print(mini,maxi)
    else:                        # this else part i am using two methods one is mini and another one is maxi
        mini = min(mini,power)   # this else part will execute 2nd and third and fourth itteration
        maxi = max(maxi,power)

        print(mini,maxi)


#output 

# 2 2
# 2 3
# 2 4
# 2 5




#project two explain 


# rock vs scissor rock will be a winner

# papper vs rock papper will be a winner

# papper vs scissor  scissor will be a winner


import random

print("welcome to stone papper scissor")


while True:
    print("choose any one........... \nRock 1 \nPaper 2 \nScissor 3 ")
    choose = int(input("please enter the number"))

    if choose == 1:
        user_choice = "Rock"
    elif choose == 2:
        user_choice = "Paper"
    else:
        user_choice = "Scissor"

    print("your choice is " + user_choice)

    print("Now computer turn")

    comp_choose = random.randint(1,3)

    if comp_choose == 1:
        computer_choice = "rock"
    elif comp_choose == 2:
        computer_choice = "paper"
    else:
        computer_choice = "scissor"
        
    if choose == comp_choose:
        print("<<<<<<<<match tie>>>>>>>>")
        result = "DRAW"

    if (choose == 1 and computer_choice == 2):
        print("paper win")
        result = "paper"
    elif (choose ==2 and computer_choice == 1):
        print("Paper win")
        result = "Paper"

    if (choose ==3 and computer_choice==1):
        print("rock win")
        result = "rock"
    elif (choose ==1 and computer_choice == 3):
        print("ROCK win")
        result = "Rock"

    if (choose == 2 and computer_choice == 3):
        print("scissor win")
        result = "scissor"

    elif (choose ==3 and computer_choice ==2):
        print("Scissor win")
        result = "Scissor"


    if result == "DRAW":
        print("Match is Draw")
    if result == user_choice:
        print("user win the game")
    else:
        print("computer win the game")
    
    print("you want to play again ennter  yes/no")

    ans = input()

    if ans == "yes":
        break

print("thanks for playing")



