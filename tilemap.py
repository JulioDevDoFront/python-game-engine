import json
import pygame 

class Tilemap:
    def __init__(self, file, name, position):
        try:
            with open(file) as loadFile:
                mapFile = json.load(loadFile)
        except FileNotFoundError:
            print("Map file was not found!")
        except json.JSONDecodeError:
            print("Invalid json map file, check that!")
        else:
            print("Sucess opening json map file!")
        
        if not name in mapFile:
            print(f"Map {name} was not found!")
            return
    
        
        self.map = mapFile[name] 
        self.name = name
        self.position = position
        self.zIndex = self.map["zIndex"]
        self.size = self.map["size"]
        self.visible = self.map["visible"]
        

    def render(self):
        pass
