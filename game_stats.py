from os import path

class GameStats:
	"""Track the statistics for the game"""

	def __init__(self, ai_game):
		"""Initialize the stats"""
		self.settings = ai_game.settings
		self.reset_stats()

		# Start alien invasion in an inactive state
		self.game_active = False

		HS_FILE = open("highscore.txt", "r")
		self.high_score = HS_FILE.read()
		HS_FILE.close()
		#self.load_highscore

	#def load_highscore(self):
	 	# High score

	 	# HS_FILE = 'highscore.txt'
	 	# self.dir = path.dirname(__file__)
	 	# with open(path.join(self.dir, HS_FILE), 'w') as f:
	 	# 	try:
	 	# 		self.high_score = int(f.read())
	 	# 	except:
	 	# 		self.high_score = 0
	 	# return self.high_score

	def reset_stats(self):
		"""Initialize stats that can change during the game"""
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.level = 1