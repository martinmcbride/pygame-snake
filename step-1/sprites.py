# Author:  Martin McBride
# Created: 2022-08-20
# Copyright (c) 2020, Martin McBride
# License: MIT

import os
import pygame as pg

class SnakeBody(pg.sprite.Sprite):

    def __init__(self, pos):
        super(SnakeBody, self).__init__()
        self.image = pg.image.load('snake-body.png')
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self):
        pass
