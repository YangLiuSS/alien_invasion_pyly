# -*- coding: utf-8 -*-
# @Author  : ly

import pygame


class Ship(object):

    def __init__(self, ai_setting, screen):
        self.screen = screen
        self.ai_setting = ai_setting
        self.image = pygame.image.load('images/ship3.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.center = float(self.screen_rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_setting.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_setting.ship_speed_factor

        print self.center
        print self.rect.centerx
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)