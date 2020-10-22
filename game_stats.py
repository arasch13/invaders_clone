

class GameStats:
	"""Track game statistics"""

	def __init__(self,ai_game):
		""""""
		self.settings = ai_game.settings
		self.reset_stats()

	def reset_stats(self):
		"""reset stats when new game starts"""
		self.ships_left = self.settings.ship_limit
		self.game_active = False
		self.score = 0