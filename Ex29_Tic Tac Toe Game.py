""" Note: This project is not completed,
complete it with apropriate user input and removing extra mass from the screen while playing the game.
 """
# Make the full Tic Tac Toe Game.


import os

one = [' ', ' ', ' ']
two = [' ', ' ', ' ']
three = [' ', ' ', ' ']
matrix = [one, two, three]  # List is created.


def cls():  # To clear the screen.
    os.system("CLS")


def DrawTicTac():  # 'DrawTicTac' is declared.
    size = 3
    print(' \t C1     C2     C3')
    for x in range(0, size):  # This loop Draws in vertical.
        r = x
        if x == 0:
            row = matrix[x]

        if x == 1:
            row = matrix[x]

        if x == 2:
            row = matrix[x]

        for y in range(0, 1):  # This loop Draws in Horizontal.
            print('   -----' * size)
            print('R{3}|  {0}   |   {1}   |   {2}  '.format(row[0], row[1], row[2], (r + 1)) + ' |')

    for l in range(0, 1):  # This loop Draws in Horizontally in the last.
        print('   -----' * size)


# Enter the user pieces in the list of list using as a board input.
suggetion = """
Make sure you have entered NUMBERS, and that numbers must be less than 4.
And you are allow to only TWO numbers, and spate them with (,) comma.

Example:
2,2
"""


def UserInput():  # 'UserInput' Function Declared.


    string = input('Enter ROW and COLUMN number:').split(',')  # 'split()' function is removing ',' form the string.

    if 'q' == string:
        return string
    else:
        integer = [int(x) for x in string]  # This is converting string numbers into integer list.

        if integer[0] < 4 and integer[1] < 4:
            return integer
        else:
            return None


def EvenOdd(number):  # Odd or Even function declared and returns 0 and 1.
    check = number % 2
    return check


def TicTacInput(InpRow, InpIndex):  # Function for places the pieces in the game.
    print("I'm in: TicTacInput(InpRow, InpIndex):")
    loopCounter = 1  # This 'loopCounter' checks that how many time this while loop is iterated.

    while True:
        # This if conditions are converting integer numbers into sublist 0, 1 or 2.
        if InpRow == 1:
            row = one
        if InpRow == 2:
            row = two
        if InpRow == 3:
            row = three

        if row[InpIndex - 1] == ' ':  # it don't allow to put the value again in the same place.

            if EvenOdd(loopCounter) == 1:  # if the counter will be ODD then player ONE's turn.
                row[InpIndex - 1] = 'X'
                loopCounter += 1
                # print(Winner())
                if Winner() == "exit":
                    break


            else:
                row[InpIndex - 1] = 'O'  # if the counter will be EVEN then player TWO's turn.
                loopCounter += 1
                print('I\'m in: else:')
                if Winner() == "exit":
                    break


        else:
            print('Here is already one pies, try again.')

            if EvenOdd(loopCounter) == 1:
                print('\nPlayer 1:X')
                values = UserInput()  # Giving the user input list to value one.
                if 'q' in values:
                    break
                InpRow = values[0]  # Accessing the 'values[0]' of user input and giving to 'InpRow'.
                InpIndex = values[1]  # Accessing the 'values[1]' of user input and giving to 'InpIndex'.

            else:
                print('\nPlayer 2:O')
                values = UserInput()
                if 'q' in values:
                    break
                InpRow = values[0]
                InpIndex = values[1]

            continue

        if ' ' in one:  # if row one's single place is not filled than it continue.

            DrawTicTac()  # Function is called to show Tic Tac board to user.

            if EvenOdd(loopCounter) == 1:
                print('\nPlayer 1:X')
                values = UserInput()
                if 'q' in values:
                    break
                InpRow = values[0]
                InpIndex = values[1]

            else:
                print('\nPlayer 2:O')
                values = UserInput()
                if 'q' in values:
                    break
                InpRow = values[0]
                InpIndex = values[1]

            continue

        elif ' ' in two:  # if row two's single place is not filled than it continue.

            DrawTicTac()

            if EvenOdd(loopCounter) == 1:
                print('\nPlayer 1:X')
                values = UserInput()
                if 'q' in values:
                    break
                InpRow = values[0]
                InpIndex = values[1]

            else:
                print('\nPlayer 2:O')
                values = UserInput()
                if 'q' in values:
                    break
                InpRow = values[0]
                InpIndex = values[1]

            continue

        elif ' ' in three:  # if row three's single place is not filled than it continue.

            DrawTicTac()

            if EvenOdd(loopCounter) == 1:
                print('\nPlayer 1:X')
                values = UserInput()
                if 'q' in values:
                    break
                InpRow = values[0]
                InpIndex = values[1]

            else:
                print('\nPlayer 2:O')
                values = UserInput()
                if 'q' in values:
                    break
                InpRow = values[0]
                InpIndex = values[1]

            continue
        else:
            if tie() == "tie":
                break

    DrawTicTac()


def Winner():  # This function tells that who is winner.

    # This for player A
    if one[0] == 'X' and two[0] == 'X' and three[0] == 'X':  # This is checking the column's winner.
        print('\nCongratulation! \nWinner is A, In C1 column.')
        return "exit"

    elif one[1] == 'X' and two[1] == 'X' and three[1] == 'X':
        print('\nCongratulation! \nWinner is A, In C2 column.')
        return "exit"

    elif one[2] == 'X' and two[2] == 'X' and three[2] == 'X':
        print('\nCongratulation! \nWinner is A, In C3 column.')
        return "exit"


    elif one[0] == 'X' and one[1] == 'X' and one[2] == 'X':  # This is checking the row's winner.
        print('\nCongratulation! \nWinner is A, In R1 row.')
        return "exit"

    elif two[0] == 'X' and two[1] == 'X' and two[2] == 'X':
        print('Congratulation! \nWinner is A, In R2 row.')
        return "exit"

    elif three[0] == 'X' and three[1] == 'X' and three[2] == 'X':
        print('Congratulation! \nWinner is A, In R3 row.')
        return "exit"


    elif one[0] == 'X' and two[1] == 'X' and three[2] == 'X':  # This is checking Cross side down.
        print('Congratulation! \nWinner is A, In right to left downside.')
        return "exit"

    elif one[2] == 'X' and two[1] == 'X' and three[0] == 'X':
        print('Congratulation! \nWinner is A, In left to right downside.')
        return "exit"


        # This for player B
    elif one[0] == 'O' and two[0] == 'O' and three[0] == 'O':  # This is checking the column's winner.
        print('Congratulation! \nWinner is B, In C1 column.')
        return "exit"

    elif one[1] == 'O' and two[1] == 'O' and three[1] == 'O':
        print('Congratulation! \nWinner is B, In C2 column.')
        return "exit"

    elif one[2] == 'O' and two[2] == 'O' and three[2] == 'O':
        print('Congratulation! \nWinner is B, In C3 column.')
        return "exit"

    elif one[0] == 'O' and one[1] == 'O' and one[2] == 'O':  # This is checking the row's winner.
        print('Congratulation! \nWinner is B, In R1 row.')
        return "exit"

    elif two[0] == 'O' and two[1] == 'O' and two[2] == 'O':
        print('Congratulation! \nWinner is B, In R2 row.')
        return "exit"

    elif three[0] == 'O' and three[1] == 'O' and three[2] == 'O':
        print('Congratulation! \nWinner is B, In R3 row.')
        return "exit"


    elif one[0] == 'O' and two[1] == 'O' and three[2] == 'O':  # This is checking Cross side down.
        print('Congratulation! \nWinner is B, In right to left downside.')
        return "exit"

    elif one[2] == 'O' and two[1] == 'O' and three[0] == 'O':
        print('Congratulation! \nWinner is B, In left to right downside.')
        return "exit"


def tie():
    if ' ' not in one and ' ' not in two and ' ' not in three:
        print('This game is tie.')
        return "tie"


instruction = """
R = Row
C = Column 
First try is Player 1, pies:X
Now Place your pieces, and  play the game. 
Enter 'q' to quit the game.
"""
print(instruction)
DrawTicTac()
# TicTacInput(*UserInput())

try:
    TicTacInput(*UserInput())
except TypeError:
    print('You are not allow to enter other values.')
    UserInput()
else:
    TicTacInput(*UserInput())
