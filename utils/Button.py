import pygame

class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		if self.text_input is not None:
			self.text = self.font.render(self.text_input, True, self.base_color)
			self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.mouse_click_sfx = pygame.mixer.Sound('assets/music/ClickButton.mp3')
		self.mouse_click_sfx.set_volume(0.25)

	def update(self, screen):

		if self.image is not None:
			screen.blit(self.image, self.rect)
		if self.text_input is not None:
			screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.mouse_click_sfx.play()
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)
