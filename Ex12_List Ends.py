""" Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only
the first and last elements of the given list. For practice, write this code inside a function. """

lis = [5, 10, 15, 20, 25]
list2 = [x for x in range(1, 12)]


# print(list2)

def fL(l):

    l = [l[0], l[-1]]
    print(l)

fL(lis)
fL(list2)
