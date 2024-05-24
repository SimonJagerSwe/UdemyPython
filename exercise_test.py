########## EXERCISE: TEST ##########
import unittest
import random

answer = random.randint(1, 10)
while True:
    try:
        guess = int(input('Guess a number from 1 to 10'))
        if 0 < guess < 11:
            if guess == answer:
                print('Bing bong! You\'re a genius!')
                break

        else:
            print('Hey, nurmnurts, I said 1 to 10!')

    except ValueError:
        print('Please enter a number, it\'s really not that hard!')
        continue