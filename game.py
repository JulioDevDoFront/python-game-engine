import pygame
import settings
import UIManager
import scenes
from entities import Entity, Renderable, Texture, Alive, Movable

def onUpdate():
    UIManager.update(thisScene)
    settings.screen.fill((255, 125, 125))
    settings.screen.blit(menuButton.surface, (menuButton.rect.x, menuButton.rect.y))
    settings.screen.blit(character.get("Renderable").texture.surface, (character.position[0], character.position[1]))
    settings.screen.blit(rat.get("Renderable").texture.surface, (rat.position.x, rat.position.y))

def onClickMenu():
    scenes.getScene("menu").load()

def onFirstLoad():
    global menuButton
    global thisScene
    global character
    global rat


    character = Entity("Player01", pygame.Vector2(190, 200), {
        "Renderable": Renderable(0, Texture("hero.png", (150, 150))),
        "Alive": Alive(10, True, 0),
        "Movable": Movable(10, 0.2)

    })
    rat = Entity("rat", pygame.Vector2(140,50), {
        "Renderable": Renderable(0, Texture("rat.png", (50, 50))),
        "Alive": Alive(1, True, 0),
        "Movable": Movable(5)
    })

    thisScene = scenes.getScene("game")
    menuButton = UIManager.UIButton(pygame.Rect(125, 175, 150, 50), (0, 255, 0), "Main Menu", thisScene)
    menuButton.onClick = onClickMenu
    print("scene being load for the fisrt time")

def onClose():
    print("closing scene game.py") 
