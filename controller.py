import pygame
class InputManager:
    def __init__(self):
        self.keys_pressed = set()
        self.profiles = {}
    

    def update(self, events):
        self._resetClickStatements()
        for event in events:
            
            if event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key)
                self._checkClicked(key)

            if event.type == pygame.KEYUP:
                key = pygame.key.name(event.key)
                self._checkClicked(key, False)

            if event.type == pygame.MOUSEBUTTONDOWN:
                self._checkClicked(event.pos)
            

    def addProfile(self, name, *keys):
        self.profiles[name] = {"pressed": False, "list": list(keys)}


    def subscribeInputAction(self, profile, key):
        self.profiles[profile]["list"].append(key)
    
    
    def isPressed(self, profile):
        return self.profiles[profile]["pressed"]
    
    def _checkClicked(self, key:str, pressing:bool = True):
        for profile in self.profiles:
            profile = self.profiles[profile]   
            if self._keyClicked(key, profile["list"]) or self._objectClicked(key, profile["list"]):
                profile["pressed"] = pressing
                
            
        return not pressing

    def _keyClicked(self, key, keyList): return key in keyList

    def _objectClicked(self, point, keyList):
        try:
            return any(rect.collidepoint(point) for rect in keyList)
        except:
            return False

    def _checkKeyReleased(self, key):
        for name in self.profiles:
            if key in self.profiles[name]["list"]:
                self.profiles[name]["pressed"] = False
                return True
        return False

    def _resetClickStatements(self):
        for item in self.profiles:
            if isinstance(self.profiles[item]["list"][0], pygame.Rect): 
                self.profiles[item]["pressed"] = False



