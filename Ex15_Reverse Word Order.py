"""
Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the
user the same string, except with the words in backwards order. For example, say I type the string:
   My name is Michele
Then I would see the string:

   Michele is name My
shown back to me.
"""

uStr = input('Enter any string you want to revers:')


def reversStr(string):

    # This 'split()' function splits the string in list. and removes entered character,
    # in attribute. for example. it 'split("l")' it will remove every single l from the string.
    final = string.split("l")

    revers = ' '.join(final[::-1])
    print(revers)

reversStr(uStr)
