from sys import exit

def new_york(bag):
	print "Welcome to New York!"
	if "bathing suit" in bag:
		if "clip on man bun" in bag: 
			print "You are an aquatic hipster. You can go to Ft. Tilden!\n"
		else:
			print "You brought a bathing suit. You can go to the beach!\n"
	elif "chopsticks" in bag:
		print "You brought chopsticks. You can go to Chinatown!\n"
	elif "clip on man bun" in bag:
		print "You're a wannabe hipster. You can go to Brooklyn!\n"
	else:
		print "You brought nothing with you! Time to go home!"
		exit(0)
	
	print "Where do you want to go?",
	
	choice = raw_input(": ")
	choice = choice.lower()
	
	if choice == "ft. tilden":
		print "You see a lot of topless chicks with tattoos!"
		exit(0)
	elif choice == "beach":
		print "You have an awesome day at the beach!"
		exit(0)
	elif choice == "chinatown":
		print "You eat delicious Chinese food!"
		exit(0)
	elif choice == "brooklyn":
		print "You listen to awesome music and eat great food!"
		exit(0)
	else:
		print "That's not a place! You get lost and wake up in New Jersey!"
		exit(0)
	
def london(bag):
	print "Welcome to London!"
	
	if "umbrella" in bag:
		print "You brought an umbrella. Smart! It's raining"
		if "clip on man bun" in bag:
			print "You're a wannabe hipster. You can go to Shoreditch!\n"
		print "You can go to the London Eye!\n"
		print "You can go to the Tower Bridge!\n"
	else:
		print "It's raining and you didn't bring an umbrella. You stay in the hotel."
		exit(0)
	
	print "Where do you want to go?"
	
	choice = raw_input(": ")
	choice = choice.lower()
	
	if choice == "shoreditch":
		print "You go out to awesome cafes, restuarants, and bars!"
		exit(0)
	elif choice == "london eye":
		print "You see an amazing view!"
		exit(0)
	elif choice == "tower bridge":
		print "You take a lot selfies! in front of the bridge!"
		exit(0)
	else:
		print "That's not a place! You get lost and wake up in Scotland!"
		exit(0)
	
def hong_kong(bag):
	print "Welcome to Hong Kong!"
	print "You can go to the Peak, the Big Buddha, or Kowloon"
	print "Where do you want to go?"
	
	choice = raw_input(": ")
	choice = choice.lower()
	
	if choice == "kowloon":
		print "You go out to awesome cafes, restuarants, and bars!"
		exit(0)
	elif choice == "peak":
		print "You see an amazing view!"
		exit(0)
	elif choice == "big buddha":
		print "You take a lot selfies! in front of the bridge!"
		exit(0)
	else:
		print "That's not a place! You get lost and wake up in Macau!"
		exit(0)

def start():
	print "You are like that guy in the movie 'Up in the Air.'"
	print "You have 10 million frequent flyer points to fly anywhere."
	print "You just showed up to the airport and are deciding where to go."
	print "The list of departures include New York, London, and Hong Kong."
	print "Where do you want to go?",
	
	choice = raw_input("> ")
	choice = choice.lower()
	
	print "Before you leave, what do you want to take with you?"
	print "You can bring a bathing suit, an umbrella, a clip on man bun, and"
	print "chopsticks. There's room in your bag for two"
	
	bag1 = raw_input("1: ")
	bag2 = raw_input("2: ")
	bag = [bag1.lower(), bag2.lower()]
	
	if choice == "new york":
		new_york(bag)
	elif choice == "london":
		london(bag)
	elif choice == "hong kong":
		hong_kong(bag)
	else:
		print "That's not a destiantion. You go home and watch TV."
		exit(0)

start()