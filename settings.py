"""Settings class for space invaders clone"""

class Settings:

	def __init__(self):
		"""Initialize game settings"""
		## static settings
		# fps settings
		self.fps = 60
		# screen settings
		self.screen_mode = 'fullscreen' # 'window' or 'fullscreen'
		self.window_screen_width = 640
		self.window_screen_height = 520
		self.bg_color = (230, 230, 230)
		# object settings
		self.bullet_width_factor = 0.005
		self.bullet_height_factor = 0.02
		self.bullet_color = (230, 230, 230) 
		self.bullets_allowed = 3
		# game settings
		self.speedup_scale = 1.5
		self.ship_limit = 3
		## dynamic settings
		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		""""""
		# object settings
		self.ship_speed_factor = 0.001
		self.bullet_speed_factor = 0.00075
		self.alien_speed_factor = 0.0001

	def increase_speed(self):
		"""increase game speed"""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale