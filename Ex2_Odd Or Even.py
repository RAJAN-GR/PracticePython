# 1st condition: Check ODD or EVEN number!
number = int(input('Enter any Number:'))

check = number % 2

if check == 0:
    print('Youe have enter EVEN number:')
else:
    print('You have entered ODD number.')


# 2nd condition: If the number is a multiple of 4, print out a different message.
check = number % 4

if check == 0:
    print('Yes it is multiple of 4.')
else:
    print('No it is not multiplication of 4.')

# 3rd condition:
'''Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
If check divides evenly into num, tell that to the user. 
If not, print a different appropriate message.'''

print('\n------- Check your own number are divisible or not? -------')
number = int(input('Number to check:'))
check = int(input('Number is divide by:'))

check = number % check
print('your answer is:', check)
if check == 0:
    print('You have enter numbers are EVENly dividable.')
else:
    print('You have enter numbers are ODDly dividable.')
