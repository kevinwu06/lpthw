import sys
import time
from sys import exit
from random import randrange, randint

hero_health = 3
villlain_health = 3
print "Hit CTRL+C to activate reactive armor."
time.sleep(4)
print "Ready!"
print "Go!"
t = 10
print " "*7, 
print "\ /"
print " "*7, 
print "/ \\"
while hero_health > 0 and villlain_health > 0:
	try:
		for i in range(t):
			sys.stdout.write("\r{0}>".format("="*i))
			sys.stdout.flush()
			time.sleep(0.5)
		print "Too late! You've been hit! He's getting closer!"
		hero_health -= 1
		t = t - randint(1,3)
				
	except KeyboardInterrupt:
		print "\nYou blocked it! You fire back! Direct hit!"
		villlain_health -= 1
		t = t - randint(1,3)
	