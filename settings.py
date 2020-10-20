"""Settings class for space invaders clone"""

class Settings:

	def __init__(self):
		"""Initialize game settings"""
		# fps settings
		self.fps = 60
		# screen settings
		self.screen_mode = 'fullscreen' # 'window' or 'fullscreen'
		self.window_screen_width = 800
		self.window_screen_height = 600
		self.bg_color = (230, 230, 230)
		# bullet settings
		self.bullet_speed = 0.5
		self.bullet_width_factor = 0.002
		self.bullet_height_factor = 0.02
		self.bullet_color = (60, 60, 60) 
		# game difficulty
		self.difficulty = 'normal'