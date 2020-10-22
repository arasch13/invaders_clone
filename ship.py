"""class for user's ship"""

import pygame
import os


class Ship:

	def __init__(self, ai_game): # 'ai_game' is the 'self' body of the space invaders
								 # instance, hence the class has access to the game
								 # resources defined in the space invaders clone class
		"""initialize ship and its starting position"""
		# get settings
		self.settings = ai_game.settings
		# get screen dimensions as rectangle
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		# load image of ship and get its rectangle dimension
		path = os.path.dirname(__file__) # get path of this file
		self.image = pygame.image.load(rf"{path}\images\ship.png")
		# resize ship based on screen resolution
		self.image = pygame.transform.scale(self.image, (int(112/1280 * self.settings.screen_width), int(144/1024 * self.settings.screen_height)))
		# get ship's rectangle dimension
		self.rect = self.image.get_rect()
		
		# center ship at screen bottom center
		self.center_ship()
		# set inital flags for ship movement
		self.moving_right = False
		self.moving_left = False
		# set ship movement speed
		self.ship_speed = self.settings.ship_speed_factor * self.settings.screen_height

	def update(self, dt):
		"""update ships behavior based on ship movement flags"""
		if self.moving_right and self.moving_left:
			pass
		elif self.moving_right and self.rect.right < self.screen_rect.right:
			 self.rect.x += self.ship_speed * dt
		elif self.moving_left and  self.rect.left > self.screen_rect.left:
			self.rect.x -= self.ship_speed * dt
		pygame.mouse.set_pos(self.rect.x, self.settings.screen_height/2)

	def blitme(self):
		"""draw ship at its current position"""
		self.screen.blit(self.image, self.rect) # 'blit()' function draws a provided 
												# image into a provided position

	def center_ship(self):
		""""""
		# get bottom center of screen and set as bottom center of ship rectangle
		# possible position attributes of a rectangle:
		# top, bottom, left, right or center, centerx, centery
		# or midbottom, midtop, midleft, midright 
		self.rect.midbottom = self.screen_rect.midbottom 