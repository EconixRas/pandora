#!/usr/bin/python

import sys
sys.path.append('../')
import libpyPandora

class Point2DInt(libpyPandora.Point2DIntStub):
	def __init__(self, x, y):
		libpyPandora.Point2DIntStub.__init__(self, x, y)

class SizeInt(libpyPandora.SizeIntStub):
	def __init__(self, width, height):
		libpyPandora.SizeIntStub.__init__(self, width, height)

class RectangleInt(libpyPandora.RectangleIntStub):
	def __init__(self, size, origin = Point2DInt(0,0)):
		libpyPandora.RectangleIntStub.__init__(self, size, origin)
	
	@classmethod
	def fromCoordinates(self, left, top, right, bottom):
		return RectangleInt(SizeInt(1+right-left, 1+bottom-top), Point2DInt(left, top))

class StaticRaster(libpyPandora.StaticRasterStub):
	def __init__(self):
		libpyPandora.StaticRasterStub.__init__(self)

class Raster(libpyPandora.RasterStub):
	def __init__(self):
		libpyPandora.RasterStub.__init__(self)

class Simulation(libpyPandora.SimulationStub):
	def __init__(self, size, numSteps, serializeResolution=1 ):
		libpyPandora.SimulationStub.__init__(self, size, numSteps, serializeResolution )

class Agent(libpyPandora.AgentStub):
	def __init__(self, id):
		libpyPandora.AgentStub.__init__( self, id)
	
	def __str__(self):
		return 'Agent: ' + self.id + ' at position: ' + str(self.position._x) + '/' + str(self.position._y)

class SpacePartition(libpyPandora.SpacePartitionStub):
	def __init__(self, fileName, overlap, finalise ):
		libpyPandora.SpacePartitionStub.__init__(self, fileName, overlap, finalise)

class OpenMPSingleNode(libpyPandora.OpenMPSingleNodeStub):
	def __init__(self, fileName ):
		libpyPandora.OpenMPSingleNodeStub.__init__(self, fileName )

class World(libpyPandora.WorldStub):
	_listOfAgents = []
	def __init__(self, simulation, scheduler = None, allowMultipleAgentsPerCell = True ):
		libpyPandora.WorldStub.__init__( self, simulation, scheduler, allowMultipleAgentsPerCell)

	def addAgent(self, agent):
		self.addAgentStub(agent)
		self._listOfAgents.append(agent)

class SimulationRecord(libpyPandora.SimulationRecordStub):
	def __init__(self, loadedResolution=1, gui=True):
		libpyPandora.SimulationRecordStub.__init__( self, loadedResolution, gui )

class GlobalAgentStats(libpyPandora.GlobalAgentsStatsStub):
	def __init__(self, separator=';'):
		libpyPandora.GlobalAgentsStatsStub.__init__( self, separator )
		
class GlobalRasterStats(libpyPandora.GlobalRasterStatsStub):
	def __init__(self, separator=';'):
		libpyPandora.GlobalRasterStatsStub.__init__( self, separator )

class AgentNum(libpyPandora.AgentNumStub):
	def __init__(self):
		libpyPandora.AgentNumStub.__init__( self)
		
class AgentMean(libpyPandora.AgentMeanStub):
	def __init__(self, attributeName):
		libpyPandora.AgentMeanStub.__init__( self, attributeName)

class AgentStdDev(libpyPandora.AgentStdDevStub):
	def __init__(self, attributeName):
		libpyPandora.AgentStdDevStub.__init__( self, attributeName)

class AgentSum(libpyPandora.AgentSumStub):
	def __init__(self, attributeName):
		libpyPandora.AgentSumStub.__init__( self, attributeName)

class RasterSum(libpyPandora.RasterSumStub):
	def __init__(self):
		libpyPandora.RasterSumStub.__init__( self)

class RasterMean(libpyPandora.RasterMeanStub):
	def __init__(self):
		libpyPandora.RasterMeanStub.__init__( self)

class GeneralState(libpyPandora.GeneralStateStub):
    def __init__(self):
        libpyPandora.GeneralStateStub.__init__(self)

class ShpLoader(libpyPandora.ShpLoaderStub):
    def __init__(self):
        libpyPandora.ShpLoaderStub.__init__(self)

"""
class AgentHDFtoSHP(libpyPandora.AgentHDFtoSHPStub):
	def __init__(self, fileName, numStep ):
		libpyPandora.AgentHDFtoSHPStub.__init__( self, fileName, numStep )
"""

