import pygame 
from tilemap import Tilemap
import menu
import game
import importlib
import scenes
import controller
import entities
import settings
import library
import UIManager
#main setup
def init():
    menuScene = scenes.create("menu", "menu")
    gameScene = scenes.create("game", "game")
    settingsS = scenes.create("settings", "settingsScene")
    library.events.addEventListener("onUIElementCreate", onUIElementCreate)
    scenes.getScene("menu").load()
    gameMap = Tilemap("map.json", "mainMap", [0,0])

def onUIElementCreate(*E):
    print("testing UIELements creation")
def onSceneCreate(*e):
    print("Scene"+ e.name+" was created sucessfuly!")



def mainPipeline():
    settings.eventsList = pygame.event.get()
    settings.evs = settings.eventsList 
    library.controller.update(settings.eventsList)
    scenes.update()


init()

while settings.RUNNING:
    mainPipeline()
    pygame.display.update()
    

