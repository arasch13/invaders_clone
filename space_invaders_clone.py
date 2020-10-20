'''Attempt to create space invaders clone game'''

# import relevant modules from standard library
import sys		# containing tools to exit game
import pygame	# game module

# import own modules
from settings import Settings
from ship import Ship
from bullet import Bullet

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
		if self.settings.screen_mode == 'fullscreen':
			self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		elif self.settings.screen_mode == 'window':
			self.screen = pygame.display.set_mode(
			(self.settings.window_screen_width, self.settings.window_screen_height))
		displayInfo = pygame.display.Info()
		self.settings.bullet_width = self.settings.bullet_width_factor * displayInfo.current_w
		self.settings.bullet_height = self.settings.bullet_height_factor * displayInfo.current_h

		# set window title
		pygame.display.set_caption("Space Invaders Clone")
		# initialize ship
		self.ship = Ship(self)
		# create sprite group for bullets
		self.bullets = pygame.sprite.Group()

	def run_game(self):
		"""start main loop for game"""
		while True:
			# limit game fps
			self.dt = self.clock.tick(self.settings.fps)
			# helper methods: methods to refactor code (commonly start with underscore)
			self._check_events() # check user input
			self._update_physics() # check game mechanics physics
			self._update_screen() # screen updater

	def _check_events(self):
		"""event loop to listen to user input"""
		for event in pygame.event.get():  # watch for keyboard and mouse events
			if event.type == pygame.QUIT: # check game exit by hitting 'x'
				sys.exit()
			elif event.type == pygame.KEYDOWN: # check if key is pressed down
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP: # check if key is released again
				self._check_keyup_events(event)

	def _update_physics(self):
		""""""
		self.ship.update(self.dt)
		self.bullets.update(self.dt)
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)

	def _update_screen(self):
		"""screen updater (update game window for each while loop)"""
		self.screen.fill(self.settings.bg_color) # background color
		self.ship.blitme() # draw ship
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		pygame.display.flip() # only make recently drawn screen visible

	def _check_keydown_events(self, event):
		"""event checks when keys are pressed"""
		if event.key == pygame.K_ESCAPE: # check game exit by typing 'esc'
			sys.exit()
		elif event.key == pygame.K_LEFT: # check move left
			self.ship.moving_left = True
		elif event.key == pygame.K_RIGHT: # check move right
			self.ship.moving_right = True
		elif event.key == pygame.K_SPACE: # check fire bullet
			self._fire_bullet()

	def _check_keyup_events(self, event):
		"""event checks when keys are released"""
		if event.key == pygame.K_LEFT: # check move left
			self.ship.moving_left = False
		elif event.key == pygame.K_RIGHT: # check move right
			self.ship.moving_right = False
		elif event.key == pygame.K_SPACE: # check fire bullet
			pass

	def _fire_bullet(self):
		""""""
		new_bullet = Bullet(self)
		self.bullets.add(new_bullet)


# start game if module run directly
if __name__ == '__main__':
	sic = SpaceInvadersClone()
	sic.run_game()