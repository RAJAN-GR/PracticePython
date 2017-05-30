# 1st Exercise Character Input

import time


# 1st condition is done 'Enter user's NAME and AGE.
name = input('Enter your name:')
age = int(input('Enter your age:'))

pname = 'Hello {0} you are {1} year old.'.format(name, age)

# 2nd condition To find out the user will be 100 year old in the year of.
difference = 100 - age
Year = difference + int(time.strftime('%Y'))

# To tell the user that he/she will be 100 year old in the year of.
page = 'And Hey in the year of {0} you will be 100 year old.'.format(Year)
fprint = pname, page

times = int(input('Enter numbers you want to see the massage is repeated on screen:'))

# Message will be printed on user requirement.
for a in range(0, times):
    for x in fprint:
        print(x)
    print('\n')
