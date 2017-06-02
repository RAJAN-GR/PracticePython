# 1st condition write a program that prints out all the elements of the list that are less than 5.
list = [1, 1, 2, 3, 4, 5, 8, 13, 21, 34, 55, 89]
'''
list1 = [2, 4, 5, 6]
list2 = [3, 4, 6, 7, 9, 0]
list1.extend(list2)
print(list1)
'''

for check in list:
    if check <= 5:
        print(check)

        Sec_list = [check]
        Sec_list.append(check)
#    print(Sec_list)


# 1st condition
