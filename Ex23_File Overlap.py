"""
Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. One .txt file has
a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.
"""

# Converting the .txt string data into 'int list'
openf = open('Ex23_HappyNumbers.txt', 'r')
content = openf.readline()
splitStr = content.split(',')
HappyList = [int(x) for x in splitStr]
# print(content)
openf.close()
print('Happy Numbers form txt files:', HappyList)


# Converting the .txt string data into 'int list'
openf = open('Ex23_PrimeNumbers.txt', 'r')
content = openf.read()
splitStr = content.split(',')
Prime = [int(x) for x in splitStr]
# print(content)
openf.close()
print('Prime Numbers form txt files:', Prime)


# Now find the overlapping values in this two lists.
Overlap = [x for x in HappyList if x in Prime]
print('\n\nPrinting the Overlapping values of Prime numbers and Happy Numbers:\n', Overlap)


# This one was just for testing and fun.
"""
with open('Ex23_HappyNumbers.txt') as read:
    readPrime = read.readline()
    print(readPrime)
"""