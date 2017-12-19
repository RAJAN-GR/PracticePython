"""
Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of
Python that takes this list a and makes a new list that has only the even elements of this list in it.
"""

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Learn this LIST COPREHENSIONS in detail.
c = [x for x in a if x % 2 == 0]    # Understand that how this Comprehension is printing the Orignal value directly.
print(c)

d = [x for x in a]
print(d)
