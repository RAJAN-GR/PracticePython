# Check the winner of Tic Tac Toe

one = ['O', 'X', 'O']
two = ['O', 'X', 'X']
three = ['O', 'X', 'O']
matrix = [one, two, three]

# one = matrix[0]  # This variable is for accessing the FIRST list's members.
# two = matrix[1]  # This variable is for accessing the SECOND list's members.
# three = matrix[2]  # This variable is for accessing the THIRD list's members.

print(one[1])  # This one accessing the FIRST member of first row.


# This for player A
if one[0] == 'X' and two[0] == 'X' and three[0] == 'X':  # This is checking the column's winner.
    print('Congratulation! \nWinner is A, In 1st column.')

elif one[1] == 'X' and two[1] == 'X' and three[1] == 'X':
    print('Congratulation! \nWinner is A, In 2nd column.')

elif one[2] == 'X' and two[2] == 'X' and three[2] == 'X':
    print('Congratulation! \nWinner is A, In 3rd column.')


elif one[0] == 'X' and one[1] == 'X' and one[2] == 'X':  # This is checking the row's winner.
    print('Congratulation! \nWinner is A, In 1st row.')

elif two[0] == 'X' and two[1] == 'X' and two[2] == 'X':
    print('Congratulation! \nWinner is A, In 2nd row.')

elif three[0] == 'X' and three[1] == 'X' and three[2] == 'X':
    print('Congratulation! \nWinner is A, In 3rd row.')


elif one[0] == 'X' and two[1] == 'X' and three[2] == 'X':  # This is checking Cross side down.
    print('Congratulation! \nWinner is A, In right to left downside.')

elif one[2] == 'X' and two[1] == 'X' and three[0] == 'X':
    print('Congratulation! \nWinner is A, In left to right downside.')


    # This for player B
elif one[0] == 'O' and two[0] == 'O' and three[0] == 'O':  # This is checking the column's winner.
    print('Congratulation! \nWinner is B, In 1st column.')

elif one[1] == 'O' and two[1] == 'O' and three[1] == 'O':
    print('Congratulation! \nWinner is B, In 2nd column.')

elif one[2] == 'O' and two[2] == 'O' and three[2] == 'O':
    print('Winner is in 3rd columnA B')

elif one[0] == 'O' and one[1] == 'O' and one[2] == 'O':  # This is checking the row's winner.
    print('Winner is in 1st row B')

elif two[0] == 'O' and two[1] == 'O' and two[2] == 'O':
    print('Winner is in 2nd row B')

elif three[0] == 'O' and three[1] == 'O' and three[2] == 'O':
    print('Winner is in 3rd row B')


elif one[0] == 'O' and two[1] == 'O' and three[2] == 'O':  # This is checking Cross side down.
    print('Winner is in right to left downside B')

elif one[2] == 'O' and two[1] == 'O' and three[0] == 'O':
    print('Winner is in left to right downside B')

else:
    print('This game is tai.')
