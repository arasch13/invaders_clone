'''Attempt to create space invaders clone game'''

# import relevant modules from standard library
import sys		# containing tools to exit game
import pygame	# game module

# import own modules
from settings import Settings

# create class for game
class SpaceInvadersClone:
	"""overall class to manage game assets and behavior"""

	def __init__(self):
		"""initialize game and create game resources"""

		# initialize background settings
		pygame.init()
		# load settings
		self.settings = Settings()
		 # set game window to predefined resolution in 'settings'
		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		# set window title
		pygame.display.set_caption("Space Invaders Clone")



	def run_game(self):
		"""start main loop for game"""
		while True:
			# event loop to listen to user input:
			for event in pygame.event.get():  # watch for keyboard and mouse events
				if event.type == pygame.QUIT: # exit game when 'QUIT' 
					sys.exit()				  # event was detected

			# screen updater (update game window for each while loop):
			self.screen.fill(self.settings.bg_color) # background color
			pygame.display.flip() # only make recently drawn screen visible:



# start game if module run directly
if __name__ == '__main__':
	sic = SpaceInvadersClone()
	sic.run_game()