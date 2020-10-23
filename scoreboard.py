import pygame.font

class Scoreboard:
	""""""

	def __init__(self, ai_game):
		""""""
		# get ai attributes
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.stats = ai_game.stats
		self.screen_rect = self.screen.get_rect()
		#
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)
		self.prep_score()

	def prep_score(self):
		""""""
		score_string = f"Score: {str(self.stats.score)}"
		self.score_image = self.font.render(score_string, True,
			self.text_color, (40, 40, 40))
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20

	def show_score(self):
 		"""Draw score to the screen."""
 		self.screen.blit(self.score_image, self.score_rect)

	def prep_highscore(self):
		""""""
		highscore_string = f"Highscore: {str(self.stats.highscore)}"
		self.highscore_image = self.font.render(highscore_string, True,
			self.text_color, (40, 40, 40))
		self.highscore_rect = self.highscore_image.get_rect()
		self.highscore_rect.right = self.screen_rect.right - 20
		self.highscore_rect.top = 60

	def show_highscore(self):
 		"""Draw score to the screen."""
 		self.screen.blit(self.highscore_image, self.highscore_rect)
