# Author:  Martin McBride
# Created: 2022-08-20
# Copyright (c) 2020, Martin McBride
# License: MIT

import pygame as pg

# Setup game

screen_width = 640
screen_height = 480

# Initialise pygame
pg.init()

# Set display size
pg.display.set_mode((screen_width, screen_height))

# Set window title
pg.display.set_caption('Snake')

# Game loop

running = True

while running:

    # Check all events in queue
    for event in pg.event.get():

        # If a quit event occurs, reset running flag
        if event.type == pg.QUIT:
            running = False
