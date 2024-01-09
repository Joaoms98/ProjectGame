import pygame, textwrap

class TextBox:
    def __init__(self, screen, font_size, font):
        self.screen = screen
        self.font_size = font_size
        self.font = font
        self.text_rect = pygame.Rect(250, 500, 1200, 500)

    def draw(self, text, color):
        y = self.text_rect.top
        line_spacing = -2
        words = textwrap.wrap(text, width=self.text_rect.width // self.font_size)
        
        for word in words:
            word_surface = self.font.render(word, True, color)
            word_height = word_surface.get_height()
            self.screen.blit(word_surface, (self.text_rect.x, y))
            y += word_height + line_spacing

