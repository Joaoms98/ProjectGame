import pygame, textwrap

class TextBox:
    def __init__(self, screen, font_size, font, size):
        self.screen = screen
        self.font_size = font_size
        self.font = font
        self.size = size

    def draw(self, text, color, pos):
        text_rect = pygame.Rect((pos), (self.size))
        y = text_rect.top
        line_spacing = -2
        words = textwrap.wrap(text, width=text_rect.width // self.font_size)

        for word in words:
            word_surface = self.font.render(word, True, color)
            word_height = word_surface.get_height()
            self.screen.blit(word_surface, (text_rect.x, y))
            y += word_height + line_spacing

