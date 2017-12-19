# This program was done by reference not my self i just understood this program.

counter_dict = {}
with open('nameslist.txt') as f:
    line = f.readline()
    while line:  # not sure that how this WHILE loop stops may be, when the variable is empty it stops working.
        print('lenght of line', len(line))
        line = line.strip()  # This 'strip()' function removes Space around the word.
        if line in counter_dict:  # This condition is checks that is a word in the line is in set or not.
            counter_dict[line] += 1  # If the word is in a set it increases the variable counter to that word label.
        else:
            counter_dict[line] = 1  # IF it is not in a set so it add to set and makes its counter variable with 1.
        line = f.readline()  # This one is again reading from the line.

print(counter_dict)
