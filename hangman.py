# Write your code here
import random
import string


def dashed(word, characters):
    word_list = list(word)
    for count in range(len(word)):
        if word_list[count] not in characters:
            word_list[count] = '-'
    return ''.join(word_list)


print('H A N G M A N')
while True:
    play = input('Type "play" to play the game, "exit" to quit:')
    if play not in ['play', 'exit']:
        print()
        continue
    if play != 'exit':
        my_list = ['python', 'java', 'kotlin', 'javascript']
        guess = random.choice(my_list)
        guess_ = '-' * len(guess)
        guessed = set()
        not_guessed = set()
        i = 8
        while i > 0:
            print()
            print(guess_)
            c = input('Input a letter: ')
            if len(c) != 1:
                print('You should input a single letter')
            elif c in guessed or c in not_guessed:
                print('You already typed this letter')
            elif c not in string.ascii_lowercase:
                print("It is not an ASCII lowercase letter")
            elif c not in guess:
                print('No such letter in the word')
                i -= 1
                not_guessed.add(c)
            else:
                guessed.add(c)
            if guessed == set(guess):
                print('\n'+guess)
                print('You guessed the word!')
                print('You survived!\n')
                break
            guess_ = dashed(guess, guessed)
        else:
            print("You are hanged!\n")
    else:
        break
