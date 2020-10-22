""""""

import pygame
from pygame.sprite import Sprite
import os

class Alien(Sprite):

	def __init__(self, ai_game):
		"""create an alien object"""
		super().__init__()
		# copy screen and settings from the game instance
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		self.settings = ai_game.settings
		# load image of alien and get its rectangle dimension
		path = os.path.dirname(__file__) # get path of this file
		self.image = pygame.image.load(rf"{path}\images\alien.png")
		# resize ship based on screen resolution
		self.image = pygame.transform.scale(self.image, (int(70/1280 * self.settings.screen_width), int(52/1024 * self.settings.screen_height)))
		# get alien's rectangle dimension
		self.rect = self.image.get_rect()
		# start each alien near the top left corner of screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		# set alien movement speed
		self.alien_speed_factor = 0.00005 # horizontal movement speed
		self.alien_dropspeed_factor = 0.75 # drop speed when hitting the edge
		self.alien_x_direction = 1 # initially move to the right

	def update(self, dt):
		"""update alien position based on speed and screen size"""
		# check if alien reaches screen border
		if (self.rect.right > self.screen_rect.right) or (self.rect.left < self.screen_rect.left):
			self.rect.y += self.alien_dropspeed_factor * self.settings.screen_height
			self.alien_x_direction *= -1
		# move alien
		self.rect.x += (self.alien_speed_factor * self.settings.screen_width * self.alien_x_direction) * dt