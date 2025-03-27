import controller as inputManager
import pygame
import scenes
import events
import UIManager as UiManager
from settings import screen, events
from library import controller
import settings
from entities import Entity, Vector2, Renderable, Texture, Movable, Alive

def onUpdate():
    UiManager.update(thisScene)
    screen.fill((244, 244, 244))
    screen.blit(pauseButton.surface, (pauseButton.rect.x, pauseButton.rect.y))
    screen.blit(textUI.surface, (textUI.rect.x, textUI.rect.y))

def onFirstLoad():
    #test area
    global thisScene 
    global imageUI
    global pauseButton
    global textUI
    global button
    global controller

    thisScene = scenes.getScene("menu")
    print("first loading" + thisScene.name)
    pauseButton = UiManager.UIButton(pygame.Rect(125,130,150,50), (24, 4, 200), "Play", thisScene)
    pauseButton.onClick = onClickPlay

    textUI = UiManager.UIButton(pygame.Rect(125, 200, 150, 50), (170,50,0), "Settings", thisScene)
    textUI.onClick = onClickSettings

    controller.addProfile("DOWN", "s")
    controller.addProfile("UP", "w")
    controller.addProfile("LEFT", "d")
    controller.addProfile("RIGHT", "a")
    print("this scene is being load for the first time")

def onLoad():
    print("this scene is being loaded")
    
def onClose():
    pass

def onClickPlay():
    scenes.getScene("game").load() 
def onClickSettings():
    scenes.getScene("settings").load()



