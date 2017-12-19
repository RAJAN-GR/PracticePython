"""
Write a program (function!) that takes a list and returns a new list that contains all the elements of the first
list minus all the duplicates.
"""
# This one is mine with different understanding of the definition.
list1 = [x for x in range(1, 13, 3)]
list1.append(4)
list2 = [x for x in range(4, 20, 3)]
list2.append(1)
list3 = []

c = [list3.append(i) for i in list1 if i not in list3]  # This is not working properly check it out tomorrow.
print(c)
def extendList(ac, b):
    list3.extend(ac)
    list3.extend(b)
    print('List1:', list1)
    print('List2:', list2)

    a = set(list3)
    print(list(a))

extendList(list1, list2)

# The original solution.
"""
# Exercise 13:
# Write a function that takes a list and returns a new list that contains 
# all the elements of the first list minus duplicates.

# this one uses a for loop
def dedupe_v1(x):
  y = []
  for i in x:
    if i not in y:
      y.append(i)
  return y

#this one uses sets
def dedupe_v2(x):
    return list(set(x))

a = [1,2,3,4,3,2,1]
print a
print dedupe_v1(a)
print dedupe_v2(a)
"""