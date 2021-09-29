import pygame
from mainScreen import *
from pygame.sprite import Sprite

class Clock(Sprite):
    def __init__(self, time):

        default_image = self.create_surface_with_text(
            text=time, font_size=25, text_rgb=WHITE, bg_rgb=BLUE
        )
        center_position= (850, 100)

        self.images = [default_image]
        self.rects = [default_image.get_rect(center=center_position)]

        super().__init__()


    @property
    def image(self):
        return self.images[0]


    @property
    def rect(self):
        return self.rects[0]


    def update(self, mouse_pos, mouse_up):
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False


    def draw(self, surface):
        surface.blit(self.image, self.rect)


    def create_surface_with_text(self, text, font_size, text_rgb, bg_rgb):
        font = pygame.freetype.SysFont("Courier", font_size, bold=True)
        surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
        return surface.convert_alpha()


    # def game_clock(screen):
    #     clock_ = 10
    #     while clock_ > 0:
    #         pygame.time.get_ticks()
    #         if (pygame.time.get_ticks()%1000==0):
    #             clock_ = clock_ - 1
    #             clock_g = str(clock_)
    #             screen.fill(BLUE)
    #             textFont = pygame.font.SysFont('comicsansms', 25)
    #             TextSurf, TextReact = textObj(clock_g, textFont, TIMER)
    #             TextReact.center = (850, 100)
    #             screen.blit(timer, (780, 57))
    #             pygame.display.update()
    #             print(clock_)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


    # def textObj(text, font, color):
    #     textSurface = font.render(text, True, color)
    #     return textSurface, textSurface.get_rect()