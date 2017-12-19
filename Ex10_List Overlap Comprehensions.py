# find same values in 2 list using comprehension
# Merge the Exercise5 and Exercise7 to gather.

# Thia solved by me.
first = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
second = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
list1 = []

c = [x for x in set(first) if x in second]
print(c)

"""
# This is final solution from the web.
import random

a = random.sample(range(1,30), 12) 
b = random.sample(range(1,30), 16) # 'SAMPLE' function is used to generate multiple numbers in a lis, 
                                   #and it's second argument'(16)' is use for, number of values you wat to generate in sample.

result = [i for i in set(a) if i in b]
"""