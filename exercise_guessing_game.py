########## EXERCISE: GUESSING GAME ##########
from random import randint

# GENERATE A NUMBER FROM 1 TO 10
answer = randint(1, 10)
print(answer)

# GET INPUT FROM USER
guess = int(input('Guess the number: '))

# CHECK IF INPUT IS 1-10
while guess < 1 or guess > 10:
    guess = int(input('Please select an integer between 1 and 10: '))

# CHECK IF NUMBER IS CORRECT, OTHERWISE, ASK AGAIN
while guess != answer:
    guess = int(input('Tough luck! Try again!\nGuess the number: '))

if guess == answer:
    print('Great guess!')

