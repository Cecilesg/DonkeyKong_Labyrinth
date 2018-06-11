#! /usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Donkey Kong Lavbyrinth Game
This is a game in which we must move DK until he finds his way through the labyrinth to the bananas.

Script Python3
Files: dklabyrinth.py, classes.py, constants.py, level1, level2 + images
"""

# TODO: import libraries
import pygame
from pygame.locals import *

from classes import *
from constants import *

# TODO: initialize Pygame library
pygame.init()

# TODO: Open the start menu display window with background, title, icon, and choice
display = pygame.display.set_mode((display_per_side, display_per_side)) # Game display is a squarre: length = height
# Game icon
icon = pygame.image.load(image_icon)
pygame.display.set_icon(icon)
# Game title
pygame.display.set_caption(game_name)

# TODO: Create global loop
carry_on = 1
while carry_on:
	# load and display game menu
	game_menu = pygame.image.load(image_game_menu).convert() # paste image as game menu
	display.blit(game_menu, (0,0))

	# Refresh
	pygame.display.flip()

	# reset variables to 1 every lap of the loop
	carry_on_game = 1
	carry_on_game_menu = 1

	# TODO: create game menu loop
	while carry_on_game_menu:

		# limit loop speed
		pygame.time.Clock().tick(30)

		# TODO: give user possibility to choose event in game menu
		for event in pygame.event.get():

			# if user quits variables in game menu loop all go to 0
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
				carry_on_game_menu = 0
				carry_on_game = 0
				carry_on = 0
				choice = 0 # variable for choice in game menu

			elif event.type == KEYDOWN:
				# launch level 1
				if event.key == K_F1:
					carry_on_game_menu = 0 # user leaves game menu and starts playing in level 1
					choice = 'lvl1' # define what game level to load
				# launch level 2
				elif event.key == K_F2:
					carry_on_game_menu = 0
					choice = 'lvl2'


	# While in the main loop, check if the user chose their level,
	# so as not to load the game if they quit
	if choice != 0:
		# load background
		background = pygame.image.load(image_background).convert()

		# generate gmae level from file
		level = Level(choice)
		level.generate()
		level.display(display)

		# create Donkey kong
		dk = Character("images/dk_droite.png", "images/dk_gauche.png",
		"images/dk_haut.png", "images/dk_bas.png", level)


	# TODO: Create game loop
	while carry_on_game:

		# limit loop speed
		pygame.time.Clock().tick(30)

		for event in pygame.event.get():

			# if user quit game then turn carry_on_game & carry_on to 0 to close display window
			if event.type == QUIT:
				carry_on_game = 0
				carry_on = 0

			elif event.type == KEYDOWN:
				# if user press ESCAPE = return to Game_Menu
				if event.key == K_ESCAPE:
					carry_on_game = 0
					carry_on = 1

				# if user use arrow keys then move DK
				elif event.key == K_RIGHT:
					dk.move('right')
				elif event.key == K_LEFT:
					dk.move('left')
				elif event.key == K_UP:
					dk.move('up')
				elif event.key == K_DOWN:
					dk.move('down')

		# displaying new positions
		display.blit(background, (0,0))
		level.display(display)
		display.blit(dk.direction, (dk.x, dk.y)) # dk.direction = DK avatar pic in the good direction
		pygame.display.flip()

		# victory = Game_Menu
		if level.grid[dk.sprite_y][dk.sprite_x] == 'a':
			carry_on_game = 0
			carry_on = 1