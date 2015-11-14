import sys
import puzzle

class Room(object):

	def enter(self):
		print "Room.enter() called"
		exit(1)
		
class Runner(object):

	def __init__(self, map):
		self.map = map

	def run(self):
		current_room = self.map.start()
		last_scene = self.map.next_room('dead')
		
		
		while current_room != last_scene:
			next_room_name = current_room.enter(puzzles[current_room.name()]['choices'], puzzles[current_room.name()]['answer'])
			current_room = self.map.next_room(next_room_name)
		
		current_room.enter()
		
class Blade_Room(Room):

	def enter(self, choices, answer):
		print 'You walk into a cave. There are straight grooves cut into the walls.'
		print 'Clue: Only the penitent man shall pass',
		if puzzle.play(choices, answer):
			return 'name_room'
		else:
			print "You get cut in half by massive blades that come out of the walls"
			return 'dead'

	def name(self):
		return 'blade_room'
	
class Name_Room(Room):

	def enter(self, choices, answer):
		print "You enter a room with a stone floor. Each stone has a letter on it. Where do you step?"
		print 'Clue: The name of God'
		if puzzle.play(choices, answer):
			return 'bridge_room'
		else:
			print "The first stone collapses and you fall into a spiked pit"
			return 'dead'
			
	def name(self):
		return 'name_room'
		
class Bridge_Room(Room):

	def enter(self, choices, answer):
		print "There is an abyss in front of you with an opening on the other side. It's very far away."
		print "Clue: Only in the leap from the lion's head will he prove his worth"
		if puzzle.play(choices, answer):
			return 'grail_room'
		else:
			print "You fall to your death"
			return 'dead'
			
	def name(self):
		return 'bridge_room'

class Grail_Room(Room):

	def enter(self, choices, answer):
		print "There are 3 cups in front of you each in a different style. One is the cup of Christ."
		print 'Clue: Choose wisely'
		if puzzle.play(choices, answer):
			print "We're going to live forever!"
			exit(1)
		else:
			print "You chose...poorly."
			return 'dead'
			
	def name(self):
		return 'grail_room'

class Dead(Room):

	def enter(self):
		exit(1)

class Map(object):

	rooms = {
		'blade_room':Blade_Room(),
		'name_room':Name_Room(),
		'bridge_room':Bridge_Room(),
		'grail_room':Grail_Room(),
		'dead':Dead()
	}

	def next_room(self, room):
		val = Map.rooms.get(room)
		return val

	def start(self):
		return self.next_room('blade_room')
		
puzzles ={
		'blade_room':{
			'choices':['Jump', 'Kneel','Wave'],
			'answer':2	
			},
		'name_room':{
			'choices':['Iehovah','Jehovah','Allah'],
			'answer':1
			},
		'bridge_room':{
			'choices':['Turn back','Jump','Walk'],
			'answer':3		
			},
		'grail_room':{
			'choices':['Jewels','Plain','Cross'],
			'answer':2		
			}
}			

m = Map()			
game = Runner(m)
game.run()