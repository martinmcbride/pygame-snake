# Author:  Martin McBride
# Created: 2022-08-20
# Copyright (c) 2022, Martin McBride
# License: MIT

import os
import pygame as pg

class SnakeBody(pg.sprite.Sprite):

    def __init__(self, pos, tile_width):
        super(SnakeBody, self).__init__()
        self.image = pg.image.load('snake-body.png')
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.delay = 200
        self.direction = pg.Vector2(1, 0)
        self.timer = 0
        self.tile_width = tile_width

    def update(self, delta_time):
        self.timer += delta_time
        if self.timer > self.delay:
            self.rect.center += self.direction * self.tile_width
            self.timer %= self.delay
