# Search an element.

Ulist = input("Enter series of numbers in ordered list:")


def shortCheck(Unumber):

    ConvList = [int(x) for x in Unumber for x in ''.join(x)]

    sec = sorted(ConvList)
    print(ConvList, sec)

    if ConvList == sec:
        x = int(input('Enter any number to check that does it exist in shorted list or not:'))

        if x in ConvList:
            print('{0} is in the list.'.format(x))
        else:
            print('{0} is not in the list.'.format(x))
    else:
        print('You have Entered list is not shorted:')

shortCheck(Ulist)
