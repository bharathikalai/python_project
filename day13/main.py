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
                displayed_word +=letter
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
            self.remaining_guesses -= 1
        self.guessed_letters.add(letter)


    def is_game_over(self):
        if self.remaining_guesses <= 0:
            print("you lost! the word was:", self.word_to_guess)
            return True
        elif '-' not in self.display_word():
            print("congratulations you guessed the word:",self.word_to_guess)
            return True
        return False


words = ["python","hangman","programming","game","computer"]

hangman_game = Hangman(words)

while not hangman_game.is_game_over():
    print("Word:", hangman_game.display_word())
    print("remaining guesses:",hangman_game.remaining_guesses)
    guess = input("guess a letter: ")
    hangman_game.guess(guess)
    print()