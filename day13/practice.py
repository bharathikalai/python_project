# import time

# start_time = time.time()
# counter = 0

# while counter < 5:

#     print("counter is:",counter)

#     counter = counter + 1

# print("loop ended")
# end_time = time.time()

# execution_time = end_time - start_time

# print("execution time:",execution_time)


# import time

# def countdown(seconds):
#     while seconds > 0:
#         print("countdown:",seconds, "seconds remaining")
#         time.sleep(1)    #  we can use this sleep is for slow down the execution time  i mentioned 1 sec slow 
#         seconds = seconds - 1 
#     print("countdown finished!")


# countdown_duration = 10

# countdown(countdown_duration)




#while not

# import time 

# def countdown(sec):
#     while not sec == 0:
#         print(sec,"the value of sec")
#         time.sleep(2)
#         sec = sec - 1
#     print("count down complete")

# a = 10

# countdown(a)

#code explain  no 1

# import random  #this is the packing which i am using this hangman game

# class Hangman:     # this is the class name Hangman
#     def __init__(self,words):
#         self.words = words      #set the variable  these are global variable
#         self.word_to_guess = self.choose_word()   #set the variable

#     def choose_word(self):    #no 4 funtion name
#         return random.choice(self.words).lower()  #this function return the random choice of words
    


# word = ["bharathi","kalai","mohan"]  #no 1 the varibale name is word and the data type is list

# a = Hangman(word)  #no 2 create the object instance of this class

# b = a.choose_word()  #no 3 call the function and the return value stored in b 

# print(b)    # no 5 finally print the value of b 





# #explain no 2 two def is_gameover(self):  check the number start with 1 

# import random

# class Hangman:
#     def __init__(self,words):
#         self.words = words
#         self.choose_word = self.choose_word()
#         self.remaining_guesses = 6

#     def choose_word(self):
#         return random.choice(self.words).lower()
    

#     def display_word(self):    # this function explain in below code(check explain no 4)
#         displayed_word = ''

    
#     def is_gameover(self):   #no 4 when the while loop starts  this function will execute
#         if self.remaining_guesses <=0:   #no 5 in globle variable i have mention this self.remaining_guesses = 6  so this so this if condtion will not execute
#             print("you lost",self.choose_word)
#             return True
#         elif '-' not in self.display_word(): #no 6 this condtion also will not execute
#             print("congratylations you guessed the word: ", self.choose_word)
#             return True
        
#         return False  #no 7 this only execute  so beginning when i run the code this value will be a return of this function that why the loop will start




# words = ["vijay","ajith","kamal","vimal","raja","kuja","boja"] #no 1  store the list in the variable words

# Hangman_game = Hangman(words)  # no 2create the object for hangman class store it in hangman_game variable

# while not Hangman_game.is_gameover():     #no 3 using while loop this loop i am using not operator which mean if the condtion is false this loop will execute if the condtion is true this loop will end now   check this function def is_gameover(self):





 
#explain no 3  set ()


# import random

# class Hangman:
#     def __init__(self,words):
#         self.words = words
#         self.word_to_guess = self.choose_word()
#         self.remaining_guesses = 6
#         self.guessed_letters = set()


#self.guessed_letters = set()  

# numbers = [1,2,3,3,4,5,6,11,1,1,2]

# print(set(numbers))

# output = {1, 2, 3, 4, 5, 6, 11} # the output   if we using set method in list it will remove all the duplicate value 
# print(type(output))  # the data type is set  


# lets try set method with dict 

# dic = {"1":1,"2":2,"3":3,"1":1}

# print(set(dic))

# output = {'3', '1', '2'}   this is the output as i use the set with dict   it is remove the duplicate value but the order is changing   but in list order not changing



#explain not 4


import random

class Hangman:
    def __init__(self,words):
        self.words = words
        self.word_to_guess = self.choose_word()
        self.remaining_guesses = 6
        self.guessed_letters = set()
    def choose_word(self):
        return random.choice(self.words).lower()
    
    def display_word(self):
        displayed_word = ''

        for letter in self.word_to_guess:
            if letter in self.guessed_letters:
                displayed_word +=  letter
            else:
                displayed_word +='-'
        return displayed_word
    
    def guess(self,letter):
        letter = letter.lower()
        if letter in self.guessed_letters:
            print("you have already guessed this letter")
        elif letter in self.word_to_guess:
            print("correct guess!")
        else:
            print("incorrect guess!")
            self.remaining_guesses -=1
        self.guessed_letters.add(letter)

    def is_game_over(self):
        if self.remaining_guesses <= 0:
            print("you lost the word was",self.word_to_guess)
            return True
        elif "-" not in self.display_word():
            print("you won you guessed the word",self.word_to_guess)
            return True
        return False


words = ["python","hangman","programming","game","computter"]

hangman_gam = Hangman(words)

while not hangman_gam.is_game_over():
    print("word:", hangman_gam.display_word())
    print("remaining guesses", hangman_gam.remaining_guesses)
    guess = input("guess a letter: ")
    hangman_gam.guess(guess)
    print()