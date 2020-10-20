"""Settings class for space invaders clone"""

class Settings:

	def __init__(self):
		"""Initialize game settings"""
		# fps settings
		self.fps = 60
		# screen settings
		self.screen_mode = 'fullscreen' # 'window' or 'fullscreen'
		self.window_screen_width = 1400
		self.window_screen_height = 900
		self.bg_color = (230, 230, 230)
		## game settings
		# game difficulty
		self.difficulty = 'normal'
		# bullet settings
		self.bullet_speed = 1.0
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60) 