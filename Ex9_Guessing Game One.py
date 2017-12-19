# Guessing Game One
# This programme took 4 hours to completed.

import random

gNume = random.randrange(1, 11)
guessNumber = int(input('Enter Number to guess the value:'))
t = 1

while gNume != guessNumber:
    t += 1
    print(guessNumber)
    print(gNume)
    print('Enter "q" to quit the game!\n')

    if gNume > guessNumber:
        print('You have entered value is low:')
        guessNumber = (input('Enter Number to guess the value:'))

    elif gNume < guessNumber:
        print('You have entered value is high:')
        guessNumber = (input('Enter Number to guess the value:'))

    if 'q' in guessNumber:
        print('Game is exit!')
        break
    else:
        guessNumber = int(guessNumber)

if 'q' != guessNumber:
    print('\nYou guess the value:', gNume)
    print('You guess the value in {0} in tray!'.format(t))
