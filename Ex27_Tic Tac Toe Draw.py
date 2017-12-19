# Enter the user pieces in the list of list using as a board input.

one = [0, 0, 0]
two = [0, 0, 0]
three = [0, 0, 0]
matrix = [one, two, three]  # List is created.


def UserInput():  # UserInput Function.
    string = input('Enter ROW and COLUMN number:').split(',')  # 'split()' function is removing ',' form the string.
    integer = [int(x) for x in string]  # This is converting string numbers into integer list.
    return integer


def EvenOdd(number):  # Odd or Even function returns 0 and 1
    check = number % 2
    return check


def TicTacInput(InpRow, InpIndex):  # Function for places the pieces in the game.

    loopCounter = 1  # This 'loopCounter' checks that how many time this while loop is iterated.

    while True:
        # This if conditions are converting integer numbers into sublist 0, 1 or 2.
        if InpRow == 1:
            row = one
        if InpRow == 2:
            row = two
        if InpRow == 3:
            row = three

        if row[InpIndex - 1] == 0:  # it don't allow to put the value again in the same place.

            if EvenOdd(loopCounter) == 1:  # if the counter will be ODD then player ONE's turn.
                row[InpIndex - 1] = 'X'
                loopCounter += 1

            else:
                row[InpIndex - 1] = 'O'  # if the counter will be EVEN then player TWO's turn.
                loopCounter += 1

        else:
            print('Here is already one pies, try again.')

            if EvenOdd(loopCounter) == 1:
                print('\nPlayer 1:X')
                values = UserInput()  # Giving the user input list to value one.
                InpRow = values[0]    # Accessing the 'values[0]' of user input and giving to 'InpRow'.
                InpIndex = values[1]  # Accessing the 'values[1]' of user input and giving to 'InpIndex'.

            else:
                print('\nPlayer 2:O')
                values = UserInput()
                InpRow = values[0]
                InpIndex = values[1]

            continue

        if 0 in one:  # if row one's single place is not filled than it continue.
            print('   C1  C2  C3')
            print('R1{0}\nR2{1}\nR3{2}'.format(matrix[0], matrix[1], matrix[2]))

            if EvenOdd(loopCounter) == 1:
                print('\nPlayer 1:X')
                values = UserInput()
                InpRow = values[0]
                InpIndex = values[1]
            else:
                print('\nPlayer 2:O')
                values = UserInput()
                InpRow = values[0]
                InpIndex = values[1]
            continue

        elif 0 in two:  # if row two's single place is not filled than it continue.
            print('   C1  C2  C3')
            print('R1{0}\nR2{1}\nR3{2}'.format(matrix[0], matrix[1], matrix[2]))

            if EvenOdd(loopCounter) == 1:
                print('\nPlayer 1:X')
                values = UserInput()
                InpRow = values[0]
                InpIndex = values[1]
            else:
                print('\nPlayer 2:O')
                values = UserInput()
                InpRow = values[0]
                InpIndex = values[1]
            continue

        elif 0 in three:  # if row three's single place is not filled than it continue.
            print('   C1  C2  C3')
            print('R1{0}\nR2{1}\nR3{2}'.format(matrix[0], matrix[1], matrix[2]))

            if EvenOdd(loopCounter) == 1:
                print('\nPlayer 1:X')
                values = UserInput()
                InpRow = values[0]
                InpIndex = values[1]

            else:
                print('\nPlayer 2:O')
                values = UserInput()
                InpRow = values[0]
                InpIndex = values[1]
            continue
        else:
            break

    print('\n{0}\n{1}\n{2}'.format(matrix[0], matrix[1], matrix[2]))

instruction = """
R = Row
C = Column 
First try is Player 1 pies:X
Now Place your pieces, and  play the game. 
"""
print(instruction)
print('  C1  C2  C3')
print('R1{0}\nR2{1}\nR3{2}'.format(matrix[0], matrix[1], matrix[2]))

TicTacInput(*UserInput())
