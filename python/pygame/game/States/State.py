class State:
    
    def __init__(self, app):
        self.app = app
        self.prev_state = None
        
    def update(self, dt):
        pass
    
    def render(self, surface):
        pass
    
    def enterState(self):
        if len(self.app.state_stack) > 1:
            self.prev_state = self.app.state_stack[-1]
        self.app.state_stack.append(self)
    
    def exitState(self):
        self.app.state_stack.pop()
    