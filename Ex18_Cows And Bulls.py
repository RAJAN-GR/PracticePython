# Note: Handle it's extra values with exceptions.
"""
Create a program that will play the “cows and bulls” game with the user. The game works like this:

Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed
correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a
“bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the
correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the
user at the end.
"""

import random

fDigit = [x for x in range(0, 10)]  # List for generate random numbers.

# Generate 4 digit random numbers.
rNumber = random.sample(fDigit, 4)
print(rNumber)


def cowbull():  # Cow and Bull main function.
    tc = 0  # tc = Trayl Counter

    print('Type exit to EXIT the game:')
    e = True  # e = exit the while loop.

    while e:

        c = 0  # c = counter, This counter is countering the potion of integer in list.
        cow = 0
        bull = 0

        uInput = input("Enter any number to guess the Numbers:")
        tc += 1
        if 'exit' == uInput:  # To exit the game while playing.
            print('You are exited the game.')
            break

        uInput = list(uInput)  # Convert number string into list.
        uInput = [int(x) for x in uInput]  # Convert STRING LIST into INTEGER STING.

        for y in uInput:
            if y not in rNumber:  # check if any single integer number exist in random number or not.
                c += 1  # This counter is countering the potion of integer in list.
                continue
            else:
                if rNumber[c] == y:  # if both integers are at the same place in different list.
                    cow += 1
                    c += 1

                    if cow == 4:  # if all values are in right and at the same places than exit the while loop.
                        e = False

                else:  # if user input values are right nut not in the same places in the list.
                    bull += 1
                    c += 1

        print('cow:{0} bull:{1}'.format(cow, bull))
    print('You have attemed {0} try.'.format(tc))
    print('The game is over')


cowbull()
