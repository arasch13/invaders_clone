import json
import os
import pygame 

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
		# get highscore
		self.highscore = self._get_highscore()

	def _get_highscore(self):
		""""""
		path = os.path.dirname(__file__)
		filename = rf"{path}\highscore.json"
		with open(filename) as f:
			highscore = json.load(f)
		return highscore

	def _save_highscore(self, highscore):
		""""""
		path = os.path.dirname(__file__)
		filename = rf"{path}\highscore.json"
		with open(filename, 'w') as f:
			json.dump(highscore, f)