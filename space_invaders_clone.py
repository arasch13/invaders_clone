'''Attempt to create space invaders clone game'''

## import relevant modules from standard library
import sys		# containing tools to exit game
import pygame	# game module

## import own modules
from settings import Settings
from ship import Ship
from bullet import Bullet

## create class for game
class SpaceInvadersClone:
	"""overall class to manage game assets and behavior"""

	def __init__(self):
		"""initialize game and create game resources"""
		pygame.init() # initialize background settings
		self.settings = Settings() # load settings
		self.clock = pygame.time.Clock() # get clock for fps limitation
		self._set_screen() # set game window resolution and title
		self.ship = Ship(self) # initialize ship
		self.bullets = pygame.sprite.Group() # create sprite group for bullets

	def run_game(self):
		"""start main loop for game"""
		while True:
			self.dt = self.clock.tick(self.settings.fps) # limit game fps
			self._check_events() # check user input
			self._update_physics() # check game mechanics physics
			self._update_screen() # screen updater


	# -----------------------------  helper methods  ---------------------------------
	# helper methods: methods to refactor code (commonly start with underscore)
	def _set_screen(self):
		"""set screen properties"""
		# set game window to predefined resolution in 'settings'
		 # the self.screen object here is a 'surface'
		 # any visual element in the game window is its own surface
		if self.settings.screen_mode == 'fullscreen':
			self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		elif self.settings.screen_mode == 'window':
			self.screen = pygame.display.set_mode(
			(self.settings.window_screen_width, self.settings.window_screen_height))
		# set window title
		pygame.display.set_caption("Space Invaders Clone")

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
		"""calculate object positions"""
		self.ship.update(self.dt)
		self.bullets.update(self.dt) # update method from bullet class is applied to all 
									 # bullet instances inside 'bullets' group
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)

	def _update_screen(self):
		"""update screen object surfaces"""
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

	def _fire_bullet(self):
		"""create new bullet and add to sprite group"""
		if len(self.bullets) < self.settings.bullets_allowed:
			# if bullet is fired, create instance from Bullet class
			# and add object to sprite group 'bullets'
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

## start game if module run directly
if __name__ == '__main__':
	sic = SpaceInvadersClone()
	sic.run_game()