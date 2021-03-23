import pygame
#Standard lib
# import os
# import sys
# import time
# import random
# import math
#Own Files
import map
import minigame
import minigameContainer
import player
import mapController
import minigameController
import playerController
import gameDisplay
#import dataTypes

# pygame.init()
# height = 320
# width = 320
# window = pygame.display.set_mode((height,width),pygame.RESIZABLE)
# pygame.display.set_caption('AMazeInGame!')
# screen = pygame.display.get_surface()
# screen.convert_alpha()
# clock = pygame.time.Clock()

class GameController():
	def __init__(self):
		self.inMap = True
		self.minigameNum = -1
		self.pause = False

		self.md = map.MapData()
		self.pd = player.PlayerData()
		self.mgd = minigameContainer.MinigameData()

		print("here")

		self.mc = mapController.MapController()
		print("how")
		self.pc = playerController.PlayerController()
		self.mgc = minigameController.MinigameController()

		print("why")

		self.disp = gameDisplay.GameDisplay()

		print("there")

	def startGame(self):
		self.mc.set(self)
		self.pc.set(self)
		self.mc.startMap()
		print("vvmm")
		self.pc.startPlayer()
		print("aaa")

	def exitGame(self):
		self.mc.exitMap()
		self.pc.exitPlayer()
		self.mgc.exitMinigame()

	def pauseGame(self):
		self.pause = not(self.pause)
		self.mc.pauseMap()
		self.pc.pausePlayer()
		self.mgc.pauseMinigame()

	def sendPlayerData(self, playerData):
		self.pd = playerData

		if self.inMap:
			self.md = self.mc.fetchMapData()
			self.pmInteraction()
		else:
			self.mgd = self.mgc.fetchMinigameData(self.minigameNum)
			self.pmgInteraction()

	def sendMapData(self, mapData):
		self.md = mapData
		self.pd = self.pc.fetchPlayerData()

		self.pmInteraction()

	def sendMinigameData(self, minigameData):
		self.mgd = minigameData
		self.pd = self.pc.fetchPlayerData()

		self.pmgInteraction()

	def pmInteraction(self):
		self.playerInteraction()
		self.mapInteraction()

		self.mc.updateMapData(self.md)
		self.pc.updatePlayerData(self.pd)

		if self.inMap:
			self.disp.displayMap(self.pd, self.md)
		else:
			self.mgc.startMinigame(self.minigameNum)

	def pmgInteraction(self):
		self.playerInteraction()
		self.minigameInteraction()

		self.mgc.updateMinigameData(self.minigameNum, self.mgd)
		self.pc.updatePlayerData(self.pd)

		self.disp.displayMinigame(self.pd, self.mgd)


		#if not(self.inMap):
		#	self.mgc.exitMinigame()

	def mapInteraction(self):
		if self.pd.x == 2 and self.pd.y == 2 and self.inMap:
			print("enter minigame")
			self.inMap = False
			self.minigameNum = 0
		pass

	def minigameInteraction(self):
		if self.pd.x == 0 and self.pd.y == 0 and not(self.inMap):
			print("exit minigame")
			self.inMap = True
			self.minigameNum = -1
		pass
	def playerInteraction(self):
		pass
