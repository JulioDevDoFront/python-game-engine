import json
import pygame 
import math

list = []

def loadJSONFile(file):
    try:
        with open(file) as loadedFile:
            mapFile = json.load(loadedFile)
            return mapFile
            
    except FileNotFoundError:
        print("This file was not found, aborting load!")
    except json.JSONDecodeError:
        print("Invalid map JSON file, plz check that and try again!")
    except:
        print("Error!")
    
    
class Tilemap:
    def __init__(self, file, position):
        mapFile = loadJSONFile(file)
        if not mapFile: return

        self.layers = mapFile["layers"]
        self.spritesheets = mapFile["tilesets"]
        self.canvas = mapFile["canvas"]
        self.position = position
        
        for e in self.spritesheets:
        
            try:
                e["image"] = pygame.image.load(e["image"])
            except:
                e["image"] = pygame.image.load("decoration.png")
                print("eror while loading img")
                return
            

    def searchSpritesheetByName(self, name):
        spritesheet =  [item for item in self.spritesheets if item['name'] == name]

        if spritesheet: return spritesheet[0]
        else: return None
    
    def splitMap(self, data, columns):
        return [data[i:i + columns] for i in range(0, len(data), columns)]

    def getTile(self, tileset, x, y, w, h):
        return tileset.subsurface(pygame.Rect(x, y, w, h))

    def render(self, surface):
        finalLayer = pygame.Surface((self.canvas['width'], self.canvas['height']))

        for layer in self.layers:
            spritesheet = self.searchSpritesheetByName(layer['tileset'])
            
            tileWidth = spritesheet['tilewidth']
            tileHeight = spritesheet['tileheight']
            tilesetName = spritesheet['name']
            layerSurface = pygame.Surface((self.canvas['width']+1, self.canvas['height']+1), pygame.SRCALPHA)
            layerData = layer['data']
            columns = math.floor(self.canvas['width'] / tileWidth)
            rows = math.floor(self.canvas['height'] / tileHeight)
            mapSplited = self.splitMap(layerData, columns)
            tileset = spritesheet["image"]
            x = 1
            y = 1

            for row in mapSplited:
            
                for column in row:
                    if (not column == -1):
                    
                    
                        tilePosition = str(float(column)).split(".")
                        tileX = int(tilePosition[0])*tileWidth
                        tileY = int(tilePosition[1])*tileHeight
                        layerSurface.blit(self.getTile(tileset, tileX, tileY, tileWidth, tileHeight), (x, y))
                    
                    x += tileWidth
                y += tileHeight
                x=1
            

            surface.blit(layerSurface, self.position)
            

