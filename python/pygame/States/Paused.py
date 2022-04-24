from States.State import State

class Paused:
    
    def __init__(self, app):
        State.__init__(self, app)

    def update(self, dt):
        pass
    
    def render(self, display):
        pass