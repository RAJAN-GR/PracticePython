# 1st condition write a program that prints out all the elements of the list that are less than 5.
list = [1, 1, 2, 3, 4, 5, 8, 13, 21, 34, 55, 89]
u_input = int(input('Enter any Number:'))
'''
This code was the fuck never do this mistake again and this be care full and check everything properly.

for check in list:
    if check <= 5:
        Sec_list = [check] #don't create list ever in the loop until it is hardly required to make list clear every time clear. 
    Sec_list.append(check)
    print(Sec_list)        # this wa very silly mistake to print every thing in the loop.
'''
Sec_list = []

for check in list:
    if check <= u_input:
        Sec_list.append(check)
print(Sec_list)


# 1st condition
