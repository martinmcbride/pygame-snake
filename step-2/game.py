# Author:  Martin McBride
# Created: 2022-08-20
# Copyright (c) 2020, Martin McBride
# License: MIT

import pygame as pg
from sprites import SnakeBody

# Setup game

screen_width = 640
screen_height = 480
tile_width = 20

# Initialise pygame
pg.init()

# Set display size
screen = pg.display.set_mode((screen_width, screen_height))

# Set window title
pg.display.set_caption('Snake')

clock = pg.time.Clock()

# Create snake sprite

snake_sprite = SnakeBody((100, 200), tile_width)
snake_group = pg.sprite.RenderPlain()
snake_group.add(snake_sprite)

# Game loop

running = True

while running:

    # Check all events in queue
    for event in pg.event.get():

        # If a quit event occurs, reset running flag
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                snake_sprite.direction = pg.Vector2(-1,  0)
            if event.key == pg.K_RIGHT:
                snake_sprite.direction = pg.Vector2(1,  0)
            if event.key == pg.K_UP:
                snake_sprite.direction = pg.Vector2(0,  -1)
            if event.key == pg.K_DOWN:
                snake_sprite.direction = pg.Vector2(0,  1)

    dt = clock.tick(30)
    snake_group.update(dt)
    screen.fill((0, 0, 0))
    snake_group.draw(screen)
    pg.display.flip()
