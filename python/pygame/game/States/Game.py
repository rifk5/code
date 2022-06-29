import pygame
from States.State import State

class Game(State):
    
    def __init__(self, app):
        State.__init__(self, app)
        
    def update(self, dt):
        pass

    def render(self, display):
        self.mouse_pos = pygame.mouse.get_pos()
        display.fill((0, 0, 0))

        
        self.app.drawText(display, "Hover", self.app.color["WHITE"], 
                          (self.mouse_pos[0], self.mouse_pos[1] - 20),
                          True)
