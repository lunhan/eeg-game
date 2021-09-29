import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum

#For the other class, write it into an individiual file and import like this
from UIElement import UIElement
from clock import Clock

img = pygame.image.load("img/nosignal_v1.png") #import img
img = pygame.transform.scale(img, (60,60))
main_img = pygame.image.load('img/gameMain.png')
main_img = pygame.transform.scale(main_img, (260, 260))
logo = pygame.image.load("img/logo.png")
logo = pygame.transform.scale(logo, (32, 32))
rule = pygame.image.load("img/rule.png")
rule = pygame.transform.scale(rule, (633, 513))
timer_img = pygame.image.load("img/clock.png")
timer_img = pygame.transform.scale(timer_img, (142, 88))

#color we gonn are reuse
BLUE = (106, 159, 181)
BG_1 = (83, 228, 179) #Mint Green
TXT_1 = (0, 0, 0)#Black
PINK = (234, 208, 209)
WHITE = (255, 255, 255)

# The function below could write into the class
# def create_surface_with_text(text, font_size, text_rgb, bg_rgb):

# The class below could write into an independent file
# class UIElement(Sprite):


class GameState(Enum):
    QUIT = -1
    TITLE = 0 #main page
    NEWGAME = 1
    FINISH = 2
    INFO = 3

def main():
    pygame.init()

    '''change: the size of main window and elememt position'''
    screen = pygame.display.set_mode((1000, 800)) #windows_size

    game_state = GameState.TITLE #start with main(title) screen

    #set app name on top bar
    pygame.display.set_caption("EEG-Game")

    #set icon:
    pygame.display.set_icon(logo)

    # create a ui element
    # quit_btn = UIElement(
    #     center_position=(500, 650), #make sure our element will be center//The center right justfy 500 and top justify 700
    #     font_size=30,
    #     bg_rgb=BLUE,
    #     text_rgb=WHITE,
    #     text="Quit",
    #     action=GameState.QUIT,
    # )

    # main loop
    while True:
        #The function below has move to independent def refere to different pages
        '''
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill(BLUE)

        ui_action = quit_btn.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            return
        quit_btn.draw(screen)
        pygame.display.flip()
        '''

        if game_state == GameState.TITLE:
            game_state =  title_screen(screen)

        if game_state == GameState.NEWGAME:
            game_state = play_level(screen)

        if game_state == GameState.FINISH:
            game_state = game_finish(screen)

        if game_state == GameState.INFO:
            game_state = game_info(screen)

        if game_state == GameState.QUIT:
            pygame.quit()
            return

def title_screen(screen): #to have our button, check main loop
    #start and quit button will be here
    start_btn = UIElement(
        center_position=(500, 470),
        font_size=40,
        bg_rgb=BG_1,
        text_rgb=TXT_1,
        text="Start",
        action=GameState.NEWGAME,
    )
    quit_btn = UIElement(
        center_position=(500, 670),
        font_size=30,
        bg_rgb=BG_1,
        text_rgb=TXT_1,
        text="Quit",
        action=GameState.QUIT,
    )
    info_btn = UIElement(
        center_position=(500, 570),
        font_size=30,
        bg_rgb=BG_1,
        text_rgb=TXT_1,
        text="How to play",
        action=GameState.INFO,
    )

    buttons = [start_btn, info_btn, quit_btn]

    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill(BG_1)#re-draw the background
        screen.blit(img, (930, 10))
        screen.blit(main_img, (370, 100))

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            button.draw(screen)

        pygame.display.flip()

def play_level(screen):
    finsih_btn = UIElement(
        center_position=(140, 770),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=TXT_1,
        text="Game finished",
        action=GameState.FINISH,
    )

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

    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill(BLUE)

        ui_action = finsih_btn.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            return ui_action
        finsih_btn.draw(screen)
        clock_ = 10
        while clock_ > 0:
            pygame.time.get_ticks()
            if (pygame.time.get_ticks() % 1000 == 0):
                clock_ = clock_ - 1
                clock_g = str(clock_)
                timer = Clock(
                    center_position=(850, 100),
                    font_size=20,
                    bg_rgb=BLUE,
                    text_rgb=WHITE,
                    text=clock_g,
                )
                timer.draw(screen)
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
        timer = Clock(
            center_position=(850, 100),
            font_size=20,
            bg_rgb=BLUE,
            text_rgb=WHITE,
            text="5",
        )
        timer.draw(screen)
        screen.blit(timer_img, (780, 57))

        pygame.display.flip()


def game_finish(screen):
    return_btn = UIElement(
        center_position=(500, 500),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Game Over, Back to main page",
        action=GameState.TITLE,
    )

    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill(BLUE)

        ui_action = return_btn.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            return ui_action
        return_btn.draw(screen)

        pygame.display.flip()

def game_info(screen):
    info_btn = UIElement(
        center_position=(500, 700),
        font_size=30,
        bg_rgb=PINK,
        text_rgb=TXT_1,
        text="Back to main",
        action=GameState.TITLE,
    )
    clock = Clock

    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill(PINK)

        ui_action = info_btn.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            return ui_action
        info_btn.draw(screen)
        screen.blit(rule, (193, 80))

        pygame.display.flip()

# call main when the script is run
if __name__ == "__main__":
    main()