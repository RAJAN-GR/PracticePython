# create user defined FIBONACCI series.

Unumber = int(input("Enter Number to create series of fibonacci:"))


def fibonacci(Unumber):
    n1 = 1
    n2 = 0
    series = []

    for x in range(0, Unumber):  # Loop number of timer user want to get fibonacci

        n2 += n1                 # Get values from the list as in list[-1] + list[-2].
        series.append(n2)        # adding the last value which is updated in 'n2'.
        length = len(series)     # check the length of the list.

        if length <= 1:          # if the length of series list is <1 then get last value of list.
            n1 = series[-1]

        else:
            n1 = series[-2]     # else part if the length of series is more than 1 than get 2nd  last value of the list.

    print('\nYour fibonacci series is:\n', series)  # print the list of the generated series of FIBONACCI.

fibonacci(Unumber)               # function is called.
