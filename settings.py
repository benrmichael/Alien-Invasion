class Settings:
	"""A class that stores all the settings for Alien Invasion"""

	def __init__(self):
		"""Initialize the game's settings"""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		# Ship settings
		self.ship_speed = 1.5
		self.ship_limit = 3

		# Bullet settings
		self.bullet_speed = 1.0
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (235, 47, 50)
		self.bullets_allowed = 4

		# Alien settings
		self.alien_speed = 0.25
		self.fleet_drop_speed = 15
		self.fleet_direction = 1

		# Game speed up scale
		self.speedup_scale = 1.1

		# Alien points scale
		self.score_scale = 1.5

		self.initialilze_dynamic_settings()

	def initialilze_dynamic_settings(self):
		"""Initialize settins that change throughout the game"""
		self.ship_speed = 1.0
		self.bullet_speed = 3.0
		self.alien_speed = 0.5

		self.fleet_direction = 1

		# Scoring
		self.alien_points = 50

	def increase_speed(self):
		"""Increase the speed of the game"""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale

		self.alien_points = int(self.alien_points * self.score_scale)