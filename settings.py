"""Settings class for space invaders clone"""

class Settings:

	def __init__(self):
		"""Initialize game settings"""
		# fps settings
		self.fps = 120
		# screen settings
		self.screen_width = 1400
		self.screen_height = 900
		self.bg_color = (230, 230, 230)
		# game settings
		self.difficulty = 'normal'