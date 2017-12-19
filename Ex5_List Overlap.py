from builtins import list

first = [1, 3, 5, 7, 1, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57,
         59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
second = [1, 7, 13, 19, 25, 31, 37, 43, 49, 55, 61, 67, 73, 79, 85, 91, 97]

list1 = []

# Method version2.0 to solve the problem.

for x in set(first):
    if x in second:
        list1.append(x)
print(list1)




'''
# Method version1.1 to solve the problem.
for x in first:          # Put every single value in variable X using loop.
    if x in list1:       # To avoid duplicate value,
        continue         # If value will already in a final list it wan't get that value again to check.
    if x in second:      # To get same values which are in both List.
        list1.append(x)  # append all values in another list which are same and avoid duplication.
print(list1)
'''

'''
# Method version1.0 to solve the problem.
for x in first:          # Put every single value in variable X using loop.
    if x in second:
        if x not in list1: # This 'NOT IN' key word is important instead of 'IF CONDITION and CONTINUE keyword'.
            print(x)
            list1.append(x)
print(list1)
'''