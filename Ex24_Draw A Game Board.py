#  Draw a tic tac toe game board.

# This is an Instruction to user.
instruction = """Enter 3 for 3X3 Tic Tac
Enter 8 for 8X8 Tic Tac 
Enter 19 for 8X8 Tic Tac """
print(instruction)

# Get user's input for create a size of Tic Tac.
usrInput = int(input("Enter any number you want to create a size of TicTac:"))


def DrawTicTac(size):  # Function is defined here

    for x in range(0, size):  # This loop Draws in vertical.
        #    print('\t')
        for y in range(0, 1):  # This loop Draws in Horizontal.
            print(' ---' * size)
            for z in range(0, 1):  # This loop Draws in Horizontal.
                print('|  \t' * (size + 1))
    for l in range(0, 1):  # This loop Draws in Horizontally in the last.
        print(' ---' * size)

DrawTicTac(usrInput)  # Function is called.
