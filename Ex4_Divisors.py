# Exercise no.4 Find the Divisors!


uNumber = int(input('Enter any number:'))

print('Your list of Divisor in 1 to 100 is:')
for check in range(1, 101):
    ans = uNumber % check
    if ans == 0:
        print(check)
