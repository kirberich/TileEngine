#!/usr/bin/python
# Graphics handling
import debug

try: import pygame
except Exception, e: debug.debugMsg(e, debug.CRITICAL)

def initGraphics(x = 640, y = 480, caption = "DisplayTest", textureDirectory = "/home/robert/Dropbox/Bilder/nevergonnawork"):
	pygame.init()
	screen = pygame.display.set_mode((x,y))
	pygame.display.set_caption(caption)
	
	background = pygame.Surface(screen.get_size())
	background.fill((255, 255, 255))
	
	screen.blit(background, (0, 0))
	pygame.display.flip()
	
	display = {"screen":screen, "viewPort":(0,0), "textureDirectory":textureDirectory}
	return display

def getChunks(world, display):
	return world.chunks

def drawWorld(world, display):
	for chunk in getChunks(world, display).flat:
		for tile in chunk.tiles.flat:
			for layer in tile.layers:
				image = pygame.image.load(display["textureDirectory"]+"/"+layer.texture)
				display["screen"].blit(image, (20,20))
	
	pygame.display.flip()