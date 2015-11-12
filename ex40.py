class Song(object):

	def __init__(self, lyrics, playcount = 0):
		self.lyrics = lyrics
		self.playcount = playcount
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
		self.playcount += 1
			
happy_bday = Song(["Happy birthday to you",
				   "I don't want to get sued",
				   "So I'll stop right there"])
				   
bulls_on_parade = Song(["They rally around tha family",
						"With pockets full of shells"])
						
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

all_my_friends_lyrics = ["That's how it starts.",
						"We go back to our house."]

all_my_friends = Song(all_my_friends_lyrics)

all_my_friends.sing_me_a_song()
print all_my_friends.playcount
all_my_friends.sing_me_a_song()
print all_my_friends.playcount