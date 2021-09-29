import pygame
from pygame.sprite import Sprite

class Clock(Sprite):
    """ An user interface element that can be added to a surface """

    def __init__(self, center_position, text, font_size, bg_rgb, text_rgb):
        default_image = self.create_surface_with_text(
            text=text, font_size=font_size, text_rgb=text_rgb, bg_rgb=bg_rgb
        )

        # add both images and their rects to lists
        self.images = [default_image]
        self.rects = [
            default_image.get_rect(center=center_position)
        ]

        # calls the init method of the parent sprite class
        super().__init__()

    # properties that vary the image and its rect when the mouse is over the element
    @property
    def image(self):
        return self.images[0]

    @property
    def rect(self):
        return self.rects[0]


    def draw(self, surface):
        """ Draws element onto a surface """
        surface.blit(self.image, self.rect)

    def create_surface_with_text(self, text, font_size, text_rgb, bg_rgb):
        """ Returns surface with text written on """
        font = pygame.freetype.SysFont("Courier", font_size, bold=True)
        surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
        return surface.convert_alpha()