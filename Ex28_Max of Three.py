# Make a function which finds the MAX between three numbers.


def MaxOfThree(noA, noB, noC):
    if noA > noB:
        if noA > noC:
            print(noA, 'is Msx.')
        else:
            print(noC, 'is Msx.')
    else:
        if noB > noC:
            print(noB, 'is Msx.')
        else:
            print(noC, 'is Msx.')

MaxOfThree(100, 55, 8)
