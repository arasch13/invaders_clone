"""Settings class for space invaders clone"""

class Settings:

	def __init__(self):
		"""Initialize game settings"""
		# fps settings
		self.fps = 60
		# screen settings
		self.screen_mode = 'fullscreen' # 'window' or 'fullscreen'
		self.window_screen_width = 600
		self.window_screen_height = 300
		self.bg_color = (230, 230, 230)
		# object settings
		self.ship_speed_factor = 0.001
		self.bullet_speed_factor = 0.0005
		self.bullet_width_factor = 0.002
		self.bullet_height_factor = 0.02
		self.bullet_color = (60, 60, 60) 
		self.bullets_allowed = 3
		# game difficulty
		self.difficulty = 'normal'