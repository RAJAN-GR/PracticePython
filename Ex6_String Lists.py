# This program is to check Palindrome sentence

# DO: Make an Module which removes unwanted characters form the file or string.

sentence = input('Enter any Palindrome sentence:')
newList = []

# This code is removing extra characters from the sting.
for char in sentence:

    flist = list(char)

    if ' ' in flist:
        flist.remove(' ')           # ".remove()" This function is used to remove character from the list.
    elif ',' in flist:
        flist.remove(',')
    elif '!' in flist:
        flist.remove('!')
    elif '.' in flist:
        flist.remove('.')
    elif '-' in flist:
        flist.remove('-')
    elif '\'' in flist:
        flist.remove('\'')
    elif '?' in flist:
        flist.remove('?')
    else:
        newList.extend(flist)        # To convert form LIST to STRING again.
        jo = ''.join(newList)        # compress this string in straight way.
        re = ''.join(newList[::-1])  # compress this string in revers way.

print('compressed string in straight way.\n', jo, '\n')
print('compressed string in revers way.\n', re, '\n')

# Main Logic of Palindrome.
if jo.casefold() == re.casefold():
    print('Your sentence is Planidrome.', sentence)
else:
    print('Your string is not Palindrome.', sentence)
