class Game:

    def __init__(self,word_to_guess):
        self.word_to_guess = word_to_guess
        self.guessed_letters = []

    def update_displayed_word(self):
        displayed_word = ''
        for letter in self.word_to_guess:
            if letter in self.guessed_letters:
                displayed_word += letter
            else:
                displayed_word += '-'
        return displayed_word



game = Game("hello")
game.guessed_letters = ['h','l','o']

print(game.update_displayed_word())