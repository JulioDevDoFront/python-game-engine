import events
import controller
import scenes as sc
import pygame
import library


game = pygame.init()

screen = pygame.display.set_mode((400, 400))
eventsList = []
evs = []
RUNNING = True


library.events.newEvent("onUIElementCreate")
library.events.newEvent("onEntityCreate")
library.events.newEvent("onSceneCreated")


