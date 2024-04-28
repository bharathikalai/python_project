#python code to train    project 1 pokiman project

powers = [3,8,9,7]

mini,maxi = 0,0

for power in powers:
    if mini ==0 and maxi ==0:
        mini,maxi = powers[0],powers[0]
        print(mini,maxi)

    else:
        mini = min(mini,power)
        maxi = max(maxi,power)
        print(mini,maxi)


#output 
# 3 3
# 3 8
# 3 9
# 3 9




#stone papper scissors  project


import random

print('winning rules of the game rock papper scissors are \n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissores -> Rock wins \n"
      + "Paper vs Scissors -> Scissor wins \n")


while True:
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    choice = int(input("Enter your choice"))

    while choice > 3 or choice < 1:
        choice = int(input("enter a valid choice please"))

    if choice == 1:
        choice_name = "Rock"
    elif choice == 2:
        choice_name = "Paper"
    else:
        choice_name = "Scissors"
    
    print("User choice is \n", choice_name)

    print("now its coumputer Trun...")

    comp_choice = random.randint(1,3)

    # while  comp_choice == choice:
    #     comp_choice = random.randint(1,3)

    if comp_choice == 1:
        comp_choice_name = 'rock'
    elif comp_choice == 2:
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissors'
    print("compuer choice is \n", comp_choice_name)

    print(choice_name, 'Vs' ,comp_choice_name)



    if (choice ==1 and comp_choice==2):
        print("paper wins =>",end=" ")
        result = "paper"
    elif(choice ==2 and comp_choice ==1):
        print("paper wins =>",end=" ")
        result = "Paper"

    if (choice == 1 and choice_name == 3):
        print("Rock wins =>\n",end=" ")
        result = "Rock"
    elif (choice ==3 and comp_choice ==1):
        print("Rock wins =>\n",end = " ")
        result = 'rocK'

    if(choice ==2 and comp_choice==3):
        print("Scissors wins =>",end = " ")
        result = "scissors"
    elif (choice==3 and comp_choice ==2):
        print("Scissors wins =>",end="")
        result = "Scissors"
    if (choice == comp_choice):
        print("Its a Draw",end= " ")
        result = "DRAW"

    if result =="DRAW":
        print("<==match tie==>")

    if result == choice_name:
        print("user won")
    else:
        print("computer won")
    print("do you want to play again? (y/n)")

    ans = input().lower()

    if ans =="n":
        break
print("thanks for playing")
    
    


