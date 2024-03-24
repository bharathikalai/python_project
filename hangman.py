import random

from collections import Counter

somewords = '''apple banana mango strawberry orange grape pineapple 
apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon'''

somewords = somewords.split(' ')

word = random.choice(somewords)

print("word",word)

if __name__ == '__main__':
    print('Guess the word! HINT:word is a name of a fruit')

    for i in word:
        print('_', end=' ')
    print()

    playing = True

    lettergussed = ' '

    chances = len(word) + 2
    print(chances)