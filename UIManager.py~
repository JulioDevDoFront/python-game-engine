import pygame
from settings import controller
import scenes
import library
List = []

def update(scene): 
    for element in scene.UIElements:
        element.update()

class UIElement:
    ID = 0
    def __init__(self, rect, colour=(125, 125, 125), scene: scenes = None):
        UIElement.ID += 1
        self.scene = scene
        self.ID = id(self)
        self.name = "Button" + str(self.ID)
        self.rect = rect
        self.colour = colour
        self.visible = True
        self.alpha = 1
        self.surface = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
        self.surface.fill((self.colour[0],self.colour[1],self.colour[2],255*self.alpha))
        
        List.append(self)
        self.scene.UIElements.append(self)
        print("appending on")
        print(self.scene.name)
        print(self.scene.UIElements)
        #external contact 
        library.events.call("onUIElementCreate", self)
    def handle_event(self, event):
        pass

    def update(self):
        pass

class UIButton(UIElement):
    def __init__(self, rect, colour: tuple = (200, 200, 200), text: str = "Button", scene = None, onClick: callable = lambda:print("you clicked me!")):

        super().__init__(rect, colour, scene)
        self.text = text
        self.fontColour = (0, 0, 0)
        self.onClick = onClick 
        self.fontSize = 30
        self.font = pygame.font.Font(None, self.fontSize)
        self.textSurface = self.font.render(self.text, True, self.fontColour)

        self.surface.blit(self.textSurface, (self.rect.width/2 - self.textSurface.get_width()/2, self.rect.height/2 - self.textSurface.get_height()/2))

        #click manager configs
        library.controller.addProfile(self.ID, self.rect)
        
    def update(self):
        if library.controller.isPressed(self.ID):
         self.onClick()
            
        def onClick(self):
            pass


class UIText(UIElement):
    def __init__(self, rect:pygame.Rect, fontColour: tuple = (200, 200, 200), text: str = "Text", scene = None, fontSize: int = 30, backgroundAlpha: int = 1):
        super().__init__(rect, (255, 255, 1), scene)
        self.fontSize = fontSize
        self.fontColour = fontColour
        self.rect = rect
        self.text = text

        
        self.font = pygame.font.Font(None, self.fontSize)
        self.textSurface = self.font.render(self.text, True, self.fontColour)
        self.surface.blit(self.textSurface, (self.rect.width/2 - self.textSurface.get_width()/2, self.rect.height/2 - self.textSurface.get_height()/2))
        
class UIImage(UIElement):
    def __init__(self, rect: pygame.Rect, source, scene):
        super().__init__(rect, (255, 255, 255), scene)
        self.alpha = 0
        self.image = pygame.image.load(source).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
        self.surface.blit(self.image, (0,0))
  



