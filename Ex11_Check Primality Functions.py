# Check Primality Functions (check the number is given by use is prime or not).

number = int(input('Enter any number to check the number is prime or not:'))
counter = 0

if number != 1:
    if number != 2:
        oddNum = number % 2                 # Check the entered number is ODD.
        if oddNum == 1:                     # if the number is ODD then check the number is prime of not.
            for x in range(1, 1001, 2):     # To Generate list of ODD numbers.
                if x <= number:             # Check the number is entered is not bigger than the divisor.
                    reminder = number % x   # if the number is not divisible than go in range and check another number
                    if reminder == 0:       # make sure the number is divisible,
                        counter += 1        # and increase the counter.
                        if counter <= 2:    # if counter is less then or equal to 2 than continue division.
                            continue
                        else:
                            print('You have entered number {0} is NOT prime number'.format(number))
                            break
                else:
                    print('You have entered number {0} IS prime number'.format(number))
                    break
        else:
            print("Even Numbers are not prime number Except 'Number 2'.")
    else:
        print(number, 'IS Prime number.')
else:
    print(number, 'is NOT Prime number.')
