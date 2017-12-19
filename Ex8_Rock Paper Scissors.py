# This is a ROCK, PAPER and SCISSORS game.
# This programme took 10 hours to completed. 9pm to 10 am

guide = """Enter show simboles sone there
            s = Stone
            c = Ciser
            p = paper \n"""
print(guide)

a = input('Person A Enter three of one:')
b = input('Person B Enter three of one:')

# Combine person A and B's value
check = a + b

# List of game possibility.
winnerList = {
    'ss': 'This match is tai!',
    'sc': 'A won this game, B lose this game!',
    'sp': 'A lose the game. B won this game!',
    'cs': 'A lose the game, B won this game!',
    'cc': 'This match is tai!',
    'cp': 'A won this game, B lose this game!',
    'ps': 'A won the game, B lose this game!',
    'pc': 'A lose this game, B won this game',
    'pp': 'This match is tai!',
}

# Game main logic.
for k, v in winnerList.items():
    if check in k:
        print(v)

# game using nested IF CONDITION.

"""
if 's' in a:
    if 's' in b:
        print('This match is tai:')
    if 'c' in b:
        print('A won this game, B lose this game.')
    if 'p' in b:
        print('A lose the game. B won this game.')

if 'c' in a:
    if 's' in b:
        print('A lose the game, B won this game.')
    if 'c' in b:
        print('This match is tai:')
    if 'p' in b:
        print('A won this game, B lose this game.')

if 'p' in a:
    if 's' in b:
        print('A won the game, B lose this game.')
    if 'c' in b:
        print('A lose this game, B won this game.')
    if 'p' in b:
        print('This match is tai:')
"""