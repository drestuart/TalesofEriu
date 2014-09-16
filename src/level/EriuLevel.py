'''
Created on Sep 3, 2014

@author: dstuart

Eriu-specific subclasses of the wang-tile map generators and associated classes
'''

import os
import random

import DungeonFeatureClass as F
from LevelClass import DungeonLevel, TownLevel, WildernessLevel
from RoomClass import Room
import Util as U
from WangTileClass import SquareWangTile, HorzWangTile, VertWangTile, \
    SquareWangTileSet, RectWangTileSet
from WangTileMap import SquareWangTileMap, HerringboneWangTileMap


os.chdir("/Users/dstuart/workspace/ChroniclesofEriu")

class TownWangTile(SquareWangTile):
    defaultConstraint = None

class dungeonHTile(HorzWangTile):
    pass

class dungeonVTile(VertWangTile):
    pass

class TownMap(SquareWangTileMap):
    tileset = SquareWangTileSet(TownWangTile)
    tileset.readFromFile(os.path.join("data", "templates", "towntiles.txt"))
        
    def __init__(self, *args):
        super(TownMap, self).__init__(*args)
        
        
class DungeonMap(HerringboneWangTileMap):
    tileset = RectWangTileSet(dungeonVTile, dungeonHTile)
    tileset.readFromFile(os.path.join("data", "templates", "dungeon_vtiles.txt"))
    
    def __init__(self, *args, **kwargs):
        super(DungeonMap, self).__init__(*args, **kwargs)
        
class EriuTownLevel(TownLevel):
    __mapper_args__ = {'polymorphic_identity': 'eriu town level'}
    MapBuilderType = TownMap

class EriuDungeonLevel(DungeonLevel):
    __mapper_args__ = {'polymorphic_identity': 'eriu dungeon level'}
    MapBuilderType = DungeonMap

class EriuWildernessLevel(WildernessLevel):
    __mapper_args__ = {'polymorphic_identity': 'eriu wilderness level'}
    
    templates = U.readTemplateFile(os.path.join("data", "templates", "dungeon_entrances.txt"));
    
    def placeDungeonEntrance(self):
        
        template = random.choice(self.templates)
        
        tileDict = {'.' : self.defaultFloorType,
                    '#' : self.buildingWallType,
                    ',' : self.buildingFloorType}
        
        entranceHeight = len(template)
        entranceWidth = len(template[0])
        
        templateX = random.choice(range(1, self.width - entranceWidth - 1))
        templateY = random.choice(range(1, self.height - entranceHeight - 1))
        
        entranceRoom = Room()
        
        for y in range(entranceHeight):
            for x in range(entranceWidth):
                tileX, tileY = x + templateX, y + templateY
                symb = template[y][x]
                tileType = tileDict[symb]
                
                newTile = tileType(tileX, tileY)
                oldTile = self.getTile(tileX, tileY)
                self.replaceTile(oldTile, newTile)
                
                # Is this tile in the entry room?
                if tileType == self.buildingFloorType:
                    entranceRoom.addTile(newTile)
                
        self.addRoom(entranceRoom)
    

class ForestLevel(EriuWildernessLevel):
    
    __mapper_args__ = {'polymorphic_identity': 'forest level'}
    
    treeChance = 0.4
    
    def __init__(self, **kwargs):
        super(ForestLevel, self).__init__(**kwargs)

    def buildLevel(self):
        # Initialize self.hasTile
        self.hasTile = U.twoDArray(self.width, self.height, False)
        
        for y in range(self.height):
            for x in range(self.width):
                newTile = self.defaultFloorType(x, y)
                
                if random.uniform(0, 1) <= self.treeChance:
                    tree = F.Tree(tile = newTile)
                    newTile.setFeature(tree)
                    
                self.tiles.append(newTile)
                self.hasTile[x][y] = True
        
        print "Building tile array"    
        self.buildTileArray()    
        
        print "Finding entry point"
        self.findEntryPoint()
        
        print "Saving open tiles"
#         db.saveDB.save(self)
        
        print "Setting up FOV"
        self.computeFOVProperties()
    
        



def main():
    townMap = TownMap(3, 3)
    townMap.printMap()

    print
    
    dungeonMap = DungeonMap(3, 3, margin = 1)
    dungeonMap.printMap()
    
if __name__ == "__main__":
    main()