import pygame
#Standard lib
# import os
# import sys
# import time
# import random
# import math
#Own Files
from map import *
from minigame import *
from minigameContainer import *
from player import *
from mapController import *
from minigameController import *
from playerController import *
from gameDisplay import *
import random
#import dataTypes

pygame.init()
height = 320
width = 320
window = pygame.display.set_mode((height,width),pygame.RESIZABLE)
pygame.display.set_caption('AMazeInGame!')
screen = pygame.display.get_surface()
screen.convert_alpha()
clock = pygame.time.Clock()

class GameController():
	def __init__(self):
		self.md = MapData()
		self.pd = PlayerData()
		self.mgd = MinigameData()

		self.mc = MapController()
		self.pc = PlayerController()
		self.mgc = MinigameController()

		self.inMap = True
		self.minigameNum = -1
		self.pause = False

		self.disp = GameDisplay()

	def startGame(self):
		self.mc.set(self)
		self.pc.set(self)
		self.mc.startMap()
		self.pc.startPlayer()

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
		self.playerMInteraction()
		self.mapInteraction()

		self.mc.updateMapData(self.md)
		self.pc.updatePlayerData(self.pd)

		if self.inMap:
			self.disp.displayMap(self.pd, self.md)
		else:
			self.mgc.startMinigame(self.minigameNum)

	def pmgInteraction(self):
		self.playerMgInteraction()
		if self.minigameNum == 0:
			self.minigame0Interaction()
		elif self.minigameNum == 1:
			self.minigame1Interaction()
		elif self.minigameNum == 2:
			self.minigame2Interaction()
		elif self.minigameNum == 3:
			self.minigame3Interaction()
		elif self.minigameNum == 4:
			self.minigame4Interaction()

		self.mgc.updateMinigameData(self.minigameNum, self.mgd)
		self.pc.updatePlayerData(self.pd)

		self.disp.displayMinigame(self.pd, self.mgd)


		if self.inMap:
			self.mgc.exitMinigame()
			temp = []
			for i in self.md.stars:
				if i[1] == self.minigameNum and self.mgd.end == 1:
					self.pd.x = i[0][0]
					self.pd.y = i[0][1]
				elif i[1] == self.minigameNum and self.mgd.end == -1:
					self.pd.x = self.md.start[0]
					self.pd.y = self.md.start[1]

				if i[1] != self.minigameNum or self.mgd.end == -1:
					temp.append(i)
				self.md.stars = temp

			# if self.mgd.end == 1:
			# 	for i in self.md.stars:
			# 		if i[1] != self.minigameNum:
			# 			temp.append(i)
			# 	self.md.stars = temp
			self.minigameNum = -1
			self.pd.score = -1
			self.pd.hp = self.pd.maxHP

	def mapInteraction(self):
		for i in self.md.stars:
			if self.pd.x == i[0][0] and self.pd.y == i[0][1] and self.inMap:
				print("enter minigame ", i[1])
				self.pd.hp = self.pd.maxHP
				self.inMap = False
				self.minigameNum = i[1]
				self.mgd = self.mgc.fetchMinigameData(self.minigameNum)					
				self.pd.x = self.mgd.entrance[0]
				self.pd.y = self.mgd.entrance[1]
				if self.minigameNum == 2:
					self.pd.score = 0
					self.pd.hp = -1

		if self.pd.stars == 5 and self.pd.x == self.md.exit[0] and self.pd.y == self.md.exit[1]:
			print("WIN")
			exit()

	def minigameInteraction(self):

		# exit minigame
		if self.pd.x == 4 and self.pd.y == 4 and not(self.inMap):
			print("exit minigame")
			self.inMap = True
			self.minigameNum = -1

	def playerMInteraction(self):

		#player movement in map
		x = self.pd.x + self.pd.xs
		y = self.pd.y + self.pd.ys
		if x >= 0 and x < self.md.width and y >= 0 and y < self.md.height and self.md.tiles[y][x] != 'w':
			self.pd.x += self.pd.xs
			self.pd.y += self.pd.ys

		self.pd.xs = 0
		self.pd.ys = 0

	def playerMgInteraction(self):

		#exit minigame
		if self.mgd.end != 0 and self.pd.x == self.mgd.exit[0] and self.pd.y == self.mgd.exit[1]:
			print("exit minigame")
			self.inMap = True
			if self.mgd.end == 1:
				self.pd.stars += 1
			# if self.minigameNum == 2:
			# 	print("scorereset")
				# self.pd.score = -1
				# return
				

		#player movement in minigame

		x = self.pd.x + self.pd.xs
		y = self.pd.y + self.pd.ys
		if x >= 0 and x < self.mgd.width and y >= 0 and y < self.mgd.height and self.mgd.tiles[y][x] != 'w':
			self.pd.x += self.pd.xs
			self.pd.y += self.pd.ys
			if self.pd.xs != 0 and self.pd.ys != 0:
				print("move")

		self.pd.xs = 0
		self.pd.ys = 0

		#item pickup

		temp = []
		for i in self.mgd.items:
			if (i.x == self.pd.x and i.y == self.pd.y):
				self.pd.score += i.value
			else:
				temp.append(i)

		self.mgd.items = temp


	def minigame2Interaction(self):

		# end minigame
		if self.mgd.items == []:
			if self.pd.score >= self.mgd.bots[0].score:
				self.mgd.end = 1
			else:
				self.mgd.end = -1
			self.mgd.bots[0].timer = -1

		# run bots

		i = self.mgd.bots[0]

		if i.timer == -1:
			return

		if i.timer == 0:
			x = i.path[0][0]
			y = i.path[0][1]
			p = ((x / abs(x)) if x != 0 else 0, (y / abs(y)) if y != 0 else 0)
			p = (p[0] * i.speed, p[1] * i.speed)
			i.path[0][0] -= p[0]
			i.path[0][1] -= p[1]
			if i.path[0] == [0, 0]:
				del i.path[0]
				# loop track
				# if i.path == []:
				# 	for j in i.track:
				# 		i.path.append(j.copy())
			i.x += p[0]
			i.y += p[1]
			i.timer = i.cd

			temp = []
			for j in self.mgd.items:
				if (j.x == i.x and j.y == i.y):
					i.score += j.value
				else:
					temp.append(j)

			self.mgd.items = temp
		else:
			i.timer -= 1

	def minigame3Interaction(self):

		# assigning player data
		# pd = self.pd

		# can have projectiles go through walls, or not, or break walls !!
		#projectiles = []
		# if timer gets to 0 and alive, end = 1, else -1
		#self.mgd.end = 1

		if self.pd.hp <= 0:
			self.mgd.exit = (self.pd.x, self.pd.y)
			self.mgd.end = -1

		if self.mgd.timer > 0:
			self.mgd.timer -= 1
		# weird edge case where player dies on same frame as timer runs out
		elif self.pd.hp > 0:
			self.mgd.end = 1

		if self.mgd.projTimer == 0:
			self.mgd.projectiles.append(Projectile())
			self.mgd.projTimer = self.mgd.projCD
		else:
			self.mgd.projTimer -= 1

		temp = []

		for i in self.mgd.projectiles:
			if i.timer == 0:
				i.x += i.xs
				i.y += i.ys
				i.dist += 1
				i.timer = i.cd
				print("proj len", len(self.mgd.projectiles))
			else:
				i.timer -= 1

			if i.dist < i.maxDist:
				if self.pd.x == i.x and self.pd.y == i.y:
					self.pd.hp -= 1
				else:
					temp.append(i)

		self.mgd.projectiles = temp

	def minigame0Interaction(self):

		if self.mgd.items == []:
			if self.mgd.timer > 0:
				self.mgd.end = 1
		if self.mgd.timer == 0:
			self.mgd.end = -1

		# if self.mgd.timer == 0:
		# 	self.mgd.exit = (self.pd.x, self.pd.y)
		# 	self.mgd.end = -1

		if self.mgd.timer > 0:
			self.mgd.timer -= 1

	def minigame4Interaction(self):
			
			# timer count down
			if self.mgd.timer > 0:
				self.mgd.timer -= 1

			# items moving left
			for i in self.mgd.items:
				if i.x > 0:
					i.x -= 0.05
				
			# create rockets when space bar is clicked
			if self.pd.spacebar == 1:
				self.pd.spacebar = 0
				self.mgd.rockets.append(Rocket(self.pd.x, self.pd.y))

			# rockets moving right	
			for rocket in self.mgd.rockets:
				rocket.x += 0.3
			
			# Remove rockets and items when they collide
			removed = 0
			for rocket in self.mgd.rockets:
				for item in self.mgd.items:
					if (rocket.x < item.x + item.offset and
					    rocket.x > item.x - item.offset and
					    rocket.y < item.y + item.offset and
						rocket.y > item.y - item.offset):
						self.mgd.items.remove(item)
						removed = 1
						break
				if (removed == 1):
					self.mgd.rockets.remove(rocket)
					yes = 0
			
			# user wins after destroying enemy rockets before count down hits 0
			if not self.mgd.items and self.mgd.timer > 0:
				self.mgd.tiles[4][0] = '0'
				self.mgd.end = 1
			elif self.mgd.timer <= 0:
				self.mgd.tiles[4][0] = '0'
				self.mgd.end = -1
	
	def minigame1Interaction(self):
		if self.mgd.items == []:
			if self.mgd.timer > 0:
				self.mgd.end = 1
			else:
				self.mgd.end = -1

		if self.mgd.timer > 0:
			self.mgd.timer -= 1	