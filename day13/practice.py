import random

class Hangman:
    def __init__(self,words):
        self.words = words
        self.word_to_guess =  self.choose_word()
        self.remaining_guesses = 6
        self.guessed_letters = set()

    def is_game_over(self):
        if self.remaining_guesses <=0:
            print("you lost the word was",self.word_to_guess)
            return True
        elif '-' not in self.display_word():
            print("congratulations you guessed the word", self.word_to_guess)
            return True
        


word = ["python","hangman","programming","game","computer"]

hangman_game = Hangman(word)


