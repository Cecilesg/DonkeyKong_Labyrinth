#! /usr/bin/env python3
#-*- coding: utf-8 -*-

"""Donkey Kong Labyrinth game classes."""

import pygame
from pygame.locals import *
from constants import *


# TODO: create class Level
class Level:
	"""Class to create a level in the game."""
	def __init__(self, file):
		self.file = file # define attribute file (for lvl)
		self.grid = 0 # define attribute grid
	
	# method 1 = generates a game level from file (like lvl1 + lvl2 file) in an attribute 'structure'
	def generate(self):
		"""Method which generates game level according to file read.
		We create a general list containing a line per line list to display."""
		with open(self.file, 'r') as file: # to open the file and read ('r') it
			grid_level = []
			for line in file: # to run the lines in the file
				line_level = []
				for sprite in line: # to run each sprite (letters) in file
					if line != '\n': # ignore '\n' at the end of each line (not a sprite)
						line_level.append(sprite) # add sprite to lines list
				grid_level.append(line_level) # add line to level list
			self.grid = grid_level # saving the grid

	# method 2 = displays the chosen level
	def display(self, display):
		"""Method which displays game level according to grids list returned by generate()"""
		wall = pygame.image.load(image_wall).convert() # loading images (only end contains some transparency)
		start = pygame.image.load(image_start).convert()
		end = pygame.image.load(image_finish).convert_alpha()

		line_nb = 0
		for line in self.grid: # run level list
			sprite_nb = 0
			for sprite in line: # run lines lists
				x = sprite_nb * sprite_size # calculate real position in pixels for line
				y = line_nb * sprite_size # for column
				if sprite == 'w': # w = wall
					display.blit(wall, (x,y))
				elif sprite == 's': # s = start
					display.blit(start, (x,y))
				elif sprite == 'e': # e = end = bananas
					display.blit(end, (x,y))
				sprite_nb += 1
			line_nb += 1
	



# TODO: create class Character
class Character:
	"""Class to create a character"""
	def __init__(self, right, left, up, down, level): # define character with self attributes =
		# character sprites
		self.right = pygame.image.load(right).convert_alpha() # convert_alpha = transparency
		self.left = pygame.image.load(left).convert_alpha()
		self.up = pygame.image.load(up).convert_alpha()
		self.down = pygame.image.load(down).convert_alpha()
		# character's position in sprites/squares and pixels
		self.sprite_x = 0
		self.sprite_y =0
		self.x = 0
		self.y = 0
		# default direction
		self.direction = self.right
		# game level character is in
		self.level = level


	def move(self, direction):
		"""Method to move character"""
		
		# Moving right
		if direction == 'right':
			if self.sprite_x < (sprite_per_side - 1): # so as not to go past the screen
				if self.level.grid[self.sprite_y][self.sprite_x+1] != 'w': # check destination sprite/square is not a wall
					self.sprite_x += 1 # move one sprite/square
					self.x = self.sprite_x * sprite_size
			self.direction = self.right # puts DK facing in the appropriate direction

		# Moving left
		if direction == 'left':
			if self.sprite_x > 0:
				if self.level.grid[self.sprite_y][self.sprite_x-1] != 'w':
					self.sprite_x -= 1
					self.x = self.sprite_x * sprite_size
			self.direction = self.left

		# Moving up
		if direction == 'up':
			if self.sprite_y > 0:
				if self.level.grid[self.sprite_y-1][self.sprite_x] != 'w':
					self.sprite_y -= 1
					self.y = self.sprite_y * sprite_size
			self.direction = self.up

		# Moving down
		if direction == 'down':
			if self.sprite_y < (sprite_per_side - 1):
				if self.level.grid[self.sprite_y+1][self.sprite_x] != 'w':
					self.sprite_y += 1
					self.y = self.sprite_y * sprite_size
			self.direction = self.down