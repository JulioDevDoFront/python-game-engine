import inspect

class Event:
#@public

    events = {}

    def __init__(self):
        print("Starting events manager module!")


    def newEvent(self, name): 
        if self._eventExists(name):
            print("An event with this name already exist!")
            return
        self.events[name] = {"list": []}

    
    def call(self, name, *args):
        if not self._eventExists(name):
            print(f"Error while calling event '{name}', event doesn't exist")
            return

        for event in self.events[name]["list"]:
            if len(inspect.signature(event).parameters)>0: event(*args)
            event()


    def addEventListener(self, name, function): 
        if not self._eventExists(name): 
                print(f"This event '{name}' doesn't exis")
                return
        self.events[name]["list"].append(function)
        print(self.events)

#@protected

    def _eventExists(self, name):
        return name in self.events
