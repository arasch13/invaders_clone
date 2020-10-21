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
		self.settings = ai_game.settings
		# load image of alien and get its rectangle dimension
		path = os.path.dirname(__file__) # get path of this file
		self.image = pygame.image.load(rf"{path}\images\alien.png")
		# resize ship based on screen resolution
		displayInfo = pygame.display.Info()
		self.image = pygame.transform.scale(self.image, (int(116/1920 * displayInfo.current_w), int(86/1080 * displayInfo.current_h)))
		# get alien's rectangle dimension
		self.rect = self.image.get_rect()
		# start each alien near the top left corner of screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		# set alien movement speed
		self.alien_speed = 0 # self.settings.alien_speed_factor * displayInfo.current_h

	def update(self, dt):
		"""update alien position based on speed and screen size"""
		#displayInfo = pygame.display.Info()
		# self.rect.y -= (self.settings.bullet_speed_factor * displayInfo.current_h) * dt