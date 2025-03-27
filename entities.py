import pygame 
list = []

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Texture:
    def __init__(self, source, size: Vector2 = None):
        if size is None: 
            raise ValueError("You should provide the size when creating texture")
        self.size = size
        self.changeSurface(source)

    def changeSurface(self, source):
        if isinstance(source, str):
            try:
                self.surface = pygame.image.load(source).convert_alpha()
            except(e):
                raise ValueError(f"Error while loading '{source}'!")
        elif isinstance(source, (tuple, list)):
            self.surface = pygame.Surface(self.size, pygame.SRCALPHA)
            self.surface.fill(source)


class Renderable:
    def __init__(self, layer: int = 0, texture:Texture = None):
        self.layer = layer
        self.scale = 1.0
        self.rotation = 0.0
        self.texture = texture

class Movable:
    def __init__(self, speed = 10, acceleration = 0.1):
        self.acceleration = 0.1
        self.speedBuffer = 1
        self.speed = speed
    
    

class Alive:
    def __init__(self, life: int = 100, canDead: bool = True, defense: int = 0):
        self.life = life
        self.canDead = canDead
        self.defense = defense
        self.inventory = []

    def addItemToInventory(self, item):
        self.inventory.append(item)

    def takeDamage(self, damage: int = 0):
        self.life -= damage/self.defense

class Entity:
    _UID = 0

    def __init__(self, name: str = "Entity", position:pygame.Vector2 = None, components: dict = {}):
        self.name = name
        self.position = position
        self.components = components
        Entity._UID += 1
        list.append(self)
   
    def get(self, component):
        return self.components.get(component)
    
    def checkComponent(self, component):
        return component in self.components

