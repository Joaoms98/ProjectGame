import pygame, textwrap

class TextBox:
    """
    A class used to draw text onto a rect

    ...

    Attributes
    ----------
    font_size : int
        text font size 
    font : any
        pygame font (tff file or name of font)
    size_rect : tuple
        size of rect
        text : str
            The text for printing
        color: rgb
            The RGB color of the text
        pos: tuple
            the position of text
    Methods
    -------
    draw(text, color, pos)
        Print the text in screen
    """

    animation_counter = 0
    text_animation_speed = 1
    animation_done = False

    def __init__(self, font_size, font, size_rect, text, color, pos):
        """
        Parameters
        ----------
        font_size : int
            text font size 
        font : any
            pygame font (tff file or name of font)
        size_rect : tuple
            size of rect
        text : str
            The text for printing
        color: rgb
            The RGB color of the text
        pos: tuple
            the position of text
        """
        self.font_size = font_size
        self.font = font
        self.size_rect = size_rect
        self.text = text
        self.color = color
        self.pos = pos

    def update(self, screen):
        """Prints text in rect.

        If the argument 'text', 'color' and 'pos' isn't passed in, 
        raised a ValueError exception

        Parameters
        ----------
        screen : any
            pygame display

        Raises
        ------
        ValueError
            If the argument 'text', 'color' and 'pos' isn't passed in
        """

        if self.text is None or self.color is None or self.pos is None:
            raise ValueError()

        text_rect = pygame.Rect((self.pos), (self.size_rect))
        y = text_rect.top
        line_spacing = -2
        words = textwrap.wrap(self.text, width=text_rect.width // self.font_size)

        for word in words:
            word_surface = self.font.render(word, True, self.color)
            word_height = word_surface.get_height()
            screen.blit(word_surface, (text_rect.x, y))
            y += word_height + line_spacing

    def updateText(self, screen, text):
        """Prints text in rect, with new text.

        If the argument 'text', 'color' and 'pos' isn't passed in, 
        raised a ValueError exception

        Parameters
        ----------
        screen : any
            pygame display
        text : str
            text for draw

        Raises
        ------
        ValueError
            If the argument 'text', 'color' and 'pos' isn't passed in
        """

        if text is None or self.color is None or self.pos is None:
            raise ValueError()

        text_rect = pygame.Rect((self.pos), (self.size_rect))
        y = text_rect.top
        line_spacing = -2
        words = textwrap.wrap(text, width=text_rect.width // self.font_size)

        for word in words:
            word_surface = self.font.render(word, True, self.color)
            word_height = word_surface.get_height()
            screen.blit(word_surface, (text_rect.x, y))
            y += word_height + line_spacing


    def updateTextAnimation(self, screen, text):
        if self.animation_done == False:
            if self.animation_counter< self.text_animation_speed * len(text):
                self.animation_counter += 1
            elif self.animation_counter >= self.text_animation_speed * len(text):
                self.animation_done = True
                self.animation_counter = 0

            snip = text[0:self.animation_counter//self.text_animation_speed]
            self.updateText(screen, snip)
        else:
             self.updateText(screen, text)