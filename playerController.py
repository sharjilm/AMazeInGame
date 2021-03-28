# import pygame
#Standard lib
# import os
# import sys
# import time
# import random
# import math
#Own Files
#import GameController
import player
import movementReader
#import dataTypes

# pygame.init()
# height = 320
# width = 320
# window = pygame.display.set_mode((height,width),pygame.RESIZABLE)
# pygame.display.set_caption('AMazeInGame!')
# screen = pygame.display.get_surface()
# screen.convert_alpha()
# clock = pygame.time.Clock()

class PlayerController():
	def __init__(self):
		self.pd = player.PlayerData()
		self.p = player.Player()
		self.gc = 0
		self.m = movementReader.MovementReader()

		self.pause = False

	def set(self, gameController):
		self.gc = gameController

	def startPlayer(self):
		self.m.set(self)

	def exitPlayer(self):
		pass

	def pausePlayer(self):
		self.pause = not(self.pause)

	def fetchPlayerData(self):
		self.pd = self.p.readPlayer()

		return self.pd

	def updatePlayerData(self, playerData):
		self.pd = playerData
		self.p.writePlayer(self.pd)

	def timeUpPlayer(self):
		self.m.read()
		self.pd = self.p.readPlayer()
		self.pd.time += 1
		self.playerChange()

	def move(self, key):
		self.pd = self.p.readPlayer()
		if key == 'U':
			self.pd.ys = -1
		elif key == 'D':
			self.pd.ys = 1
		elif key == 'L':
			self.pd.xs = -1
		elif key == 'R':
			self.pd.xs = 1

		#modify movement
		self.playerChange()

	def playerChange(self):
		#CHANGE

		#print(self.pd.x, self.pd.y)

		self.p.writePlayer(self.pd)
		self.gc.sendPlayerData(self.pd)