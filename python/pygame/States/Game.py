import pygame
from States.State import State

class Game(State):
    
    def __init__(self, app):
        State.__init__(self, app)
        
    def update(self, dt):
        pass
    
    def render(self, display):
        display.fill((0, 0, 0))
        self.app.drawText(display, "Game State", self.app.color["WHITE"], self.app.screen_center[0], self.app.screen_center[1])

        