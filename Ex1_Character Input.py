# 1st Exercise Character Input

import time


# 1st condition is done 'Enter user's NAME and AGE.
name = input('Enter your name:')
age = int(input('Enter your age:'))

print('Hello {0} you are {1} year old.'.format(name, age))

# 2nd condition To find out the user will be 100 year old in the year of.
difference = 100 - age
Year = difference + int(time.strftime('%Y'))

# To tell the user that he/she will be 100 year old in the year of.
print('And Hey in the year of {0} you will be 100 year old.'.format(Year))

#This is new change done.push it to github.
