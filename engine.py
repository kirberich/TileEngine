#!/usr/bin/python
#Semi-general-purpose isometric tiling engine, based on pygame
import graphics
import numpy

class Layer:
	""" A tile layer, saves texture, height and depth data """
	def __init__(self, texture = None, anchorPoint = (0,0), heightMap = [], depthMap = [], layerTransitionPoint = (0,0), useDepthMap = False):
		self.texture = texture
		self.anchorPoint = anchorPoint # Give the coordinate inside the texture that should be mapped to the tile's origin (lower left corner)
		self.heightMap = heightMap # Numpy matrix with height data of tile or Integer for constant height)
		
		self.depthMap = depthMap # Matrix with depth data for occlusion calculation
		self.layerTransitionPoint = layerTransitionPoint # Everything northeast of this point is rendered under the layer, even if it is above (faster occlusion calculation)
		self.useDepthMap = useDepthMap # If true depth map is used for occlusion calculation rather than the simpler ltp

	def boundingBox(self):
		return (26,14)
class Tile:
	""" A single tile """
	def __init__(self, layers = []):
		self.layers = layers # List of layers
	
	def updateLayerOrder():
		for layer in self.layers:
			pass
	
	def boundingBox(self):
		return (26,14)

class Chunk():
	""" An area of the game world, small enough that several of these can be in memory that the same time. """
	def __init__(self, id = 0, tiles = [], heightMap = []):
		self.id = id # Identifier for this chunk
		self.tiles = tiles # Actual map data
		self.heightMap = heightMap #numpy matrix, saves the terrain's height data
		# Position?
	
	def boundingBox(self):
		try: return ( len(self.tiles[0])*26, len(self.tiles)*14 )
		except: return (0,0)

class World:
	""" The world this engine models. """
	def __init__(self, chunks = [], tileSize = (26,14), chunkSize = (1,1)):
		self.chunks = chunks # Chunks are parts of the map of a moderate size, which are loaded into memory when displayed
		self.tileSize = tileSize
		self.chunkSize = chunkSize
		
	def boundingBox(self):
		return (len(self.chunks)*self.chunkSize[0]*self.tileSize[0], len(self.chunks[0])*self.chunkSize[1]*self.tileSize[1])


# Unit test
if __name__ == "__main__":
	display = graphics.initGraphics()
	
	testLayer = Layer(texture = "grass.png")
	testTile = Tile(layers = [testLayer])
	testChunk = Chunk(id = 1, tiles = numpy.matrix( [ [testTile] ] ))
	testWorld = World(chunks = numpy.matrix( [[testChunk]] ))
	
	print testWorld.boundingBox()
	
	graphics.drawWorld(testWorld, display)