# importing file name from function call on command line
from sys import argv

script, filename = argv

# opening file and creating file object
txt = open(filename)

# reading contents of file and printing them out
print "Here's your file %r:" % filename
print txt.read()

# prompting user to enter a file name
print "Type the filename again:"
file_again = raw_input("> ")

# opening file and creating file object
txt_again = open(file_again)

# reading contents of file and printing them out
print txt_again.read()

txt.close()
txt_again.close()