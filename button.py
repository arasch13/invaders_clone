import pygame.font

class Button:
	""""""

	def __init__(self, ai_game, msg):
		""""""
		# get screen dimensions
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = self.screen.get_rect()
		# set visual button attributes 
		self.width, self.height = (self.settings.screen_width / 10, 
			self.settings.screen_height / 20)  # size
		self.button_color = (230, 230, 230) # background color
		self.text_color = (0, 0, 0) # text color
		self.font = pygame.font.SysFont(None, 48) # font style
		# Build the button's rect object and center it.
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center
		# The button message needs to be prepped only once.
		self._prep_msg(msg)

	def _prep_msg(self, msg):
		""""""
		self.msg_image = self.font.render(msg, True, self.text_color,
			 self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		""""""
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)
