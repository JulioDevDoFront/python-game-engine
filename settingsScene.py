import pygame
import settings
import UIManager
import scenes

def onUpdate():
    UIManager.update(thisScene)
    settings.screen.fill((190, 255, 190))
    settings.screen.blit(menuButton.surface, (menuButton.rect.x, menuButton.rect.y))

def onClickMenu():
     
    scenes.getScene("menu").load()

def onFirstLoad():
    global thisScene
    global menuButton
    thisScene = scenes.getScene("settings")
    menuButton = UIManager.UIButton(pygame.Rect(125, 175, 150, 50), (0, 255, 0), "Main Menu", thisScene)
    menuButton.onClick = onClickMenu
