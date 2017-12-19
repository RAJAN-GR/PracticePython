"""
This time the user will pick any number and computer will guss the number.
"""

import random

low = 1
high = 100
counter = 1
instructions = """
Enter 'l' if your number is Less then this Number.
Enter 'h' if your number is High this Number.
Enter 'y' if it is the number what you have guessed.
Enter 'q' to quit the game.
"""

while True:

    print(instructions)

    guss = random.randrange(low, high)
    uIn = input('Is your number {0} :'.format(guss))

    if uIn == 'l':  # This checks the guessed number is Lower than this.
        low = guss  # This 'low' variable is replacing the starting value of random with 'guss' number in 'randrange' fun.
        counter += 1

    elif uIn == 'h':  # This checks the guessed number is Higher than this.
        high = guss  # This 'high' variable is replacing the ending value of random with 'guss' number in 'randrange' fun.
        counter += 1

    elif uIn == 'y':
        print('I have guessed it in {0} trial.'.format(counter))
        break

    elif uIn == 'q':  # This statement allow to quit the game.
        print('You quit the game!, Bay Bay')
        break
