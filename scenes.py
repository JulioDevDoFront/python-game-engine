#author: Julio cesar 
#description: this module serves as flow controller on main program pipeline, it also delimites and call the right script for some scene, that is simple but so many efficient
#dependencies: pip install importlib
#last edition date: feb. 02/2025

from library import events
import importlib
import sys

scenesList = [] 
activeScene = None 

def update():
    if hasattr(activeScene, "update"): activeScene.update()

def create(name, path):
   return Scene(name, path)
   
def getScene(name):
    scene = None
    for s in scenesList:
        title = s["name"]
        if name == title: 
            scene = s["scene"]
        
    return scene

class Scene:
    state = "unload"
    UIElements = []
    entities = []

    def __init__(self, name, path):
        events.call("onSceneCreated", self)
        self.name = name
        self.path = path
        self.UIElements = []
        try:
            self.script = importlib.import_module(path)
            
        except():
            raise ValueError("Scene script don't exist")

        scenesList.append({"name": name, "scene": self})



    def load(self):
        print(self.UIElements)
        global activeScene
        if 'onFirstLoad' in dir(self.script) and self.state == "unload": self.script.onFirstLoad()
        if 'onLoad' in dir(self.script): self.script.onLoad()

        if not activeScene is self:
            if activeScene: activeScene.close()
            activeScene = self    
            activeScene.state = "running"
           
    def close(self):
        global activeScene
        activeScene.state = "stop"

        if hasattr(self.script, "onBeforeClose"):
            self.script.onBeforeClose()

    def update(self):
        if hasattr(self.script, "onUpdate"):
            self.script.onUpdate()
        else:
            pass


