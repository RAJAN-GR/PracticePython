"""
Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of
lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password
every time the user asks for a new password. Include your run-time code in a main method. """

import random

guid = " s = strong password\n" \
       "ws = week password in string\n" \
       "wn = week password in number"

print(guid)
usCond = input('Enter any for your password generation condition:')


def GeneratPass(uCond):
    if 's' == uCond:

        # Generate list of 7 random numbers string.
        ListNumber = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        randNumber = random.sample(ListNumber, 7)
        randNumberStr = [str(x) for x in randNumber]
        fNumbStr = ''.join(randNumberStr)

        # Generate 4 random alphabets string.
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        randAlpha = random.sample(alphabets, 5)
        String = ''.join(randAlpha)
        fStr = String.title()

        # Generate any symbol string.
        symb = '!@#$%^&*()_+'
        randSym = random.choice(symb)

        # Merge the all strings to gather.
        ns = fStr + randSym + fNumbStr
        print('\nYour strong Password is generated:\n', ns)

    elif 'ws' == uCond:
        # Generate 4 random alphabets string.
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        randAlpha = random.sample(alphabets, 5)
        String = ''.join(randAlpha)
        fStr = String.title()
        f = fStr.swapcase()
        print('\nYour simple string password is generate:\n', f)

    elif 'wn' == uCond:
        # Generate list of 7 random numbers string.
        ListNumber = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        randNumber = random.sample(ListNumber, 7)
        randNumberStr = [str(x) for x in randNumber]
        fNumbStr = ''.join(randNumberStr)
        print('\nYour simple numeric password is generate:\n', fNumbStr)

GeneratPass(usCond)
