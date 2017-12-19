# Create and write to a txt file.

# Method one to write the file.
openFile = open('helo.txt', 'w')
openFile.write('Just for testing the file is working or not.')
openFile.close()

# Second method do write the file.
with open('secToTest.txt', 'w') as open_file:
    open_file.write('\nI\'m from the file "secToTest". \nA string to write')

# Create a new file for getting data from this
with open('nameslist.txt', 'w') as wri:
    wri.write('a')
