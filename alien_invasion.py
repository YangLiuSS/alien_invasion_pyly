# -*- coding: utf-8 -*-
# @Author  : ly
import sys

from settings import Settings
from ship import Ship
import game_functions as gf

import pygame


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_with, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    ship = Ship(ai_settings, screen)
    # bg_color = (230, 230, 230)

    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)



run_game()

