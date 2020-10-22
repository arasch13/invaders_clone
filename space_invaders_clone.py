'''Attempt to create space invaders clone game'''

## import relevant modules from standard library
import sys		# containing tools to exit game
import pygame	# game module
import os
from time import sleep

## import own modules
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button

## create class for game
class SpaceInvadersClone:
	"""overall class to manage game assets and behavior"""

	def __init__(self):
		"""initialize game and create game resources"""
		pygame.init() # initialize background settings
		self.settings = Settings() # load settings
		self.stats = GameStats(self) # initial game statistics
		self.stats.game_active = False	 # game is active
		self.clock = pygame.time.Clock() # get clock for fps limitation
		self._set_screen() # set game window resolution and title
		self.ship = Ship(self) # initialize ship
		self.bullets = pygame.sprite.Group() # create sprite group for bullets
		self.aliens = pygame.sprite.Group() # create sprite group for aliens
		self.play_button = Button(self, "Play")

	def run_game(self):
		"""start main loop for game"""
		while True:
			self.dt = self.clock.tick(self.settings.fps) # limit game fps
			self._check_events() # check user input
			self._update_screen() # screen updater
			if self.stats.game_active:
				self._update_physics() # check game mechanics physics
			

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
		# save screen resolution
		displayInfo = pygame.display.Info()
		self.settings.screen_width = displayInfo.current_w
		self.settings.screen_height = displayInfo.current_h
		# set window title
		pygame.display.set_caption("Space Invaders Clone")
		# load background image and scale
		path = os.path.dirname(__file__)
		self.background_image = pygame.image.load(rf"{path}\images\background.png")
		self.background_image = pygame.transform.scale(self.background_image, (self.settings.screen_width+2, self.settings.screen_height+2))
	
	def _play_music(self):
		"""play background music in endless loop"""
		path = os.path.dirname(__file__)
		pygame.mixer.music.load(rf"{path}\sounds\background.mp3") 
		pygame.mixer.music.play(-1,0.0)

		"""set screen properties"""
	def _check_events(self):
		"""event loop to listen to user input"""
		for event in pygame.event.get():  # watch for keyboard and mouse events
			if event.type == pygame.QUIT: # check game exit by hitting 'x'
				sys.exit()
			elif event.type == pygame.KEYDOWN: # check if key is pressed down
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP: # check if key is released again
				self._check_keyup_events(event)
			elif event.type == pygame.MOUSEBUTTONDOWN: # check if mouse button pressed
				self._check_mousebutton_events(event)
			if self.stats.game_active == True:
				x_mouse, y_mouse =  pygame.mouse.get_pos()
				if x_mouse > 0 and x_mouse < (self.settings.screen_width - self.ship.rect.width):
					self.ship.rect.x = x_mouse

	def _update_physics(self):
		"""calculate object positions"""
		self.ship.update(self.dt)
		self._bullets_update()
		self._aliens_update()

	def _update_screen(self):
		"""update screen object surfaces"""
		self.screen.blit(self.background_image, [-2, -2]) # background
		if self.stats.game_active == False:
			self.play_button.draw_button()# button
		else:
			pygame.mouse.set_visible(False) # make mouse invisible
		self.ship.blitme() # draw ship
		for bullet in self.bullets.sprites(): # draw bullets
			bullet.draw_bullet()
		self.aliens.draw(self.screen) # draw aliens
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

	def _check_mousebutton_events(self, event):
		""""""
		mouse_pos = pygame.mouse.get_pos() # get position of mouse cursor
		self._check_on_button(mouse_pos)

	def _check_on_button(self, mouse_pos):
		""""""
		# check if play button
		if self.stats.game_active == False:
			# 'collidepoint()' checks collision of a rectangle with a point
			if self.play_button.rect.collidepoint(mouse_pos):
				self.stats.game_active = True
				self._play_music() # set background music
		if self.stats.game_active == True:
			self._fire_bullet()

	def _fire_bullet(self):
		"""create new bullet and add to sprite group"""
		if len(self.bullets) < self.settings.bullets_allowed:
			# if bullet is fired, create instance from Bullet class
			# and add object to sprite group 'bullets'
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _bullets_update(self):
		"""update bullets' positions"""
		self.bullets.update(self.dt) # update method from bullet class is applied to all 
									 # bullet instances inside 'bullets' group
		# check if bullet leaves screen area
		self._leaving_bullets()
		# check if bullet hits alien
		self._alien_collision()
	
	def _leaving_bullets(self):
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)

	def _alien_collision(self):
		collisions = pygame.sprite.groupcollide(	# 'groupcollide()' can detect collisions between
			self.bullets, self.aliens, True, True)	# sprite objects and remove any object based on
													# input arguments
		# check if aliens are gone
		if not self.aliens: # check if aliens group is empty
			self.bullets.empty() # empty bullets group
			self._create_fleet() # create new alien fleet
			self.settings.increase_speed()

	def _aliens_update(self):
		"""update aliens' positions"""
		self.aliens.update(self.dt)
		# check ship collision
		# 'spritecollideany()' checks collision between any sprite object and all objects of a group
		shipHit = pygame.sprite.spritecollideany(self.ship, self.aliens)
		if shipHit or (1==2):
			self._dead_sequence()

	def _dead_sequence(self):
		# stop music
		pygame.mixer.music.stop()
		# pause
		sleep(1)
		# replay music
		self._play_music()
		# decrease remaining lifes
		self.stats.ships_left -= 1
		# empty aliens and bullets groups
		self.bullets.empty() # empty bullets group
		self.aliens.empty() # empty aliens group
		# set initial speed values
		self.settings.initialize_dynamic_settings()
		# create new fleet
		self._create_fleet()
		# recenter ship
		self.ship.center_ship()
		if self.stats.ships_left == 0:
			self.stats.reset_stats()
			pygame.mixer.music.stop()
			self.aliens.empty() # empty aliens group
			pygame.mouse.set_visible(True) # make mouse visible again

	def _create_fleet(self):
		"""create an alien fleet that fills row space"""
		# create first alien to get its attributes
		alien = Alien(self)
		# get available row space for aliens
		available_x_space = self.settings.screen_width - (2 * alien.rect.width) - (int(self.settings.screen_width / 60))
		available_y_space = self.settings.screen_height - (6 * alien.rect.height) - self.ship.rect.height
		number_aliens_x = available_x_space // (2 * alien.rect.width)
		# create alien rows
		number_rows = available_y_space // (2 * alien.rect.height)

		for i in range(number_rows):
			# create alien row
			for j in range(number_aliens_x):
				alien = Alien(self)
				alien.rect.x = alien.rect.width + 2 * alien.rect.width * j
				alien.rect.y = alien.rect.height + 2 * alien.rect.height * i
				self.aliens.add(alien)
		

## start game if module run directly
if __name__ == '__main__':
	sic = SpaceInvadersClone()
	sic.run_game()