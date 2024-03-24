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
    correct = 0
    flag = 0
    try: 
        while (chances !=0) and flag == 0:
            print()
            chances -=1
            print("chances",chances)
            try:
                guess = str(input('enter a letter to guess: '))
            except:
                print('Enter only a Letter')
                continue
            if not guess.isalpha():
                print('Enter only a Letter')
                continue
            elif len(guess)  > 1:
                print('Enter only a Single Letter')
                continue
            elif guess in lettergussed:
                print('you have already guessed that letter')
                continue
            if guess in word:
                k = word.count(guess)
                for _ in range(k):
                    lettergussed += guess
            for char in word:
                if char in lettergussed and (Counter(lettergussed) != Counter(word)):
                    print(char, end= '')
                    correct +=1

                elif (Counter(lettergussed) == Counter(word)):
                    
                    print("The word is: ", end= ' ')
                    print(word)

                    flag = 1

                    print('congratulation ypou won')
                    break
                    break
                else:
                    print('__', end= '')

        if chances  <=0 and (Counter(lettergussed) != Counter(word)):
            print()
            print('you lost try again')

            print('the word was {}'.format(word))
    except KeyboardInterrupt:
        print()
        print('bye try again')
        exit()

