# Author:  Martin McBride
# Created: 2022-08-20
# Copyright (c) 2020, Martin McBride
# License: MIT

import pygame

# Setup game

# Initialise pygame
pygame.init()

# Set display size
pygame.display.set_mode((800, 600))

# Set window title
pygame.display.set_caption('Snake')

# Game loop

running = True

while running:

    # Check all events in queue
    for event in pygame.event.get():

        # If a quit event occurs, reset running flag
        if event.type == pygame.QUIT:
            running = False
