import libtcodpy as libtcod
import pygame, sys, random

import const

def draw_game():

    global SURFACE_MAIN

    #clear the surface
    SURFACE_MAIN.fill(const.COLOR_DEFAULT_BG)

    #TODO draw the map

    #draw the character
    SURFACE_MAIN.blit(const.S_PLAYER, ( const.GAME_WIDTH/2-16, const.GAME_HEIGHT/2-16 ))

    #update the display
    pygame.display.flip()


def game_main_loop():

    game_quit = False

    while not game_quit:

        #get player input
        events_list = pygame.event.get()

        #process input
        for event in events_list:
            if event.type == pygame.QUIT:
                game_quit = True

        #draw the game
        draw_game()

    #quit the game
    pygame.quit()
    exit()

def game_init():

    global SURFACE_MAIN

    #initialize pygame
    pygame.init()

    SURFACE_MAIN = pygame.display.set_mode( (const.GAME_WIDTH, const.GAME_HEIGHT) )

if __name__ == '__main__':
    game_init()
    game_main_loop()