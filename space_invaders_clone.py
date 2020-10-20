'''Attempt to create space invaders clone game'''

# import relevant modules from standard library
import sys		# containing tools to exit game
import pygame	# game module

# import own modules
from settings import Settings
from ship import Ship

# create class for game
class SpaceInvadersClone:
	"""overall class to manage game assets and behavior"""

	def __init__(self):
		"""initialize game and create game resources"""

		# initialize background settings
		pygame.init()
		# load settings
		self.settings = Settings()
		# get clock for fps limitation
		self.clock = pygame.time.Clock()
		 # set game window to predefined resolution in 'settings'
		 # the self.screen object here is a 'surface'
		 # any visual element in the game window is its own surface
		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		# set window title
		pygame.display.set_caption("Space Invaders Clone")
		# initialize ship
		self.ship = Ship(self)

	def run_game(self):
		"""start main loop for game"""
		while True:
			# limit game fps
			self.dt = self.clock.tick(self.settings.fps)
			
			# check user input
			self._check_events() # this is a helper method to refactor code
								 # helper methods commonly start with underscore 
			# check game mechanics updates
			self.ship.update(self.dt)
			
			# screen updater
			self._update_screen()

	def _check_events(self):
		"""event loop to listen to user input"""
		for event in pygame.event.get():  # watch for keyboard and mouse events
			if event.type == pygame.QUIT: # check game exit by hitting 'x'
				sys.exit()
			elif event.type == pygame.KEYDOWN: # check if key is pressed down
				if event.key == pygame.K_q: # check game exit by typing 'q'
					sys.exit()
				elif event.key == pygame.K_ESCAPE: # check full screen
					pass
				elif event.key == pygame.K_LEFT: # check move left
					self.ship.moving_left = True
				elif event.key == pygame.K_RIGHT: # check move right
					self.ship.moving_right = True
				elif event.key == pygame.K_SPACE: # check fire bullet
					pass
			elif event.type == pygame.KEYUP: # check if key is released again
				if event.key == pygame.K_ESCAPE: # check full screen
					pass
				elif event.key == pygame.K_LEFT: # check move left
					self.ship.moving_left = False
				elif event.key == pygame.K_RIGHT: # check move right
					self.ship.moving_right = False
				elif event.key == pygame.K_SPACE: # check fire bullet
					pass

	def _update_screen(self):
		"""screen updater (update game window for each while loop)"""
		self.screen.fill(self.settings.bg_color) # background color
		self.ship.blitme() # draw ship
		pygame.display.flip() # only make recently drawn screen visible


# start game if module run directly
if __name__ == '__main__':
	sic = SpaceInvadersClone()
	sic.run_game()