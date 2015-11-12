numbers = []

def list_add(n):
	i = 0
	while i < n:
		print "At the top i is %d" % i
		numbers.append(i)

		i = i + 1
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i


n = raw_input("How many? ")
list_add(int(n))
print "The numbers: "

for num in numbers:
    print num