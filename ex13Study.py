from sys import argv

script, a, b = argv

print "This script is:", script
print "The sum of ", a, " and ", b, "is ", int(a)+int(b)
c = raw_input("Add another number: ")
print "The grand total is ", int(a)+int(b)+int(c)