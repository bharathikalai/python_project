# hay guys this is my first project in python rock paper scisser

import random

def get_user_choise():
    user_input = input("Enter the option rock,paper,scisser  :").lower()
    while user_input not in ["rock","paper","scisser"]:
        print("hay please enter the valide option")

        user_input = input("Enter the option rock paper scisser")

    return user_input
def get_computer_choise():
    compuer_input = random.choice(["rock","paper","scisser"])
    return compuer_input

def final_result(user_choise,computer_choise):
    print("you choise",user_choise)
    print("computer choise", computer_choise)

    if user_choise == computer_choise:
        return "match tie"
    elif((user_choise == "paper" and computer_choise == "stone")or(user_choise ==
                                                                   "scisser" and computer_choise== "paper")or
                                                                   (user_choise == "stone" and 
                                                                    computer_choise == "scisser")):
        return "you win"
    else:
        return "computer win"
    


def play_game():
    print("welcome to the rock paper scisser game")
    while True:
        user_choise = get_user_choise()
        computer_choise = get_computer_choise()
        result = final_result(user_choise,computer_choise)

        print(result)

        regame = input("Do want to play again:(yes/no)").lower()
        if regame !="yes":
            print("bye bye see to again")
            break

if __name__ == "__main__":
    play_game()


#wow  successfullly complet my first project in python 
    