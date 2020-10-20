"""class for bullets shot from the ship"""

# import sprite class from pygame
import pygame
from pygame.sprite import Sprite

# create bullet class as child class from Sprite
# sprite can be used for objects that could appear multiple times simultaniously
class Bullet(Sprite):
	""""""
	def __init__(self, ai_game):
		"""create a bullet object at ship's current position"""
		super().__init__()
		# copy screen and settings from the game instance
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		# get bullet color from settings
		self.color = self.settings.bullet_color
		# set bullet size relative to screen resolution
		displayInfo = pygame.display.Info()
		self.settings.bullet_width = self.settings.bullet_width_factor * displayInfo.current_w
		self.settings.bullet_height = self.settings.bullet_height_factor * displayInfo.current_h
		# create a rectangle for bullet in screen origin 
		# with width and height from settings
		self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
			self.settings.bullet_height)
		# set midtop of bullet rectangle to ship rectangle midtop 
		self.rect.midtop = ai_game.ship.rect.midtop

	def update(self, dt):
		"""update bullet position based on speed and screen size"""
		displayInfo = pygame.display.Info()
		self.rect.y -= (self.settings.bullet_speed_factor * displayInfo.current_h) * dt

	def draw_bullet(self):
		"""draw bullet to screen"""
		pygame.draw.rect(self.screen, self.color, self.rect)
