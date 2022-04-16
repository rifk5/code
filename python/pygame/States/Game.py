import pygame
from States.State import State

class Game(State):
    
    def __init__(self, app):
        State.__init__(self, app)
        
    def update(self, dt):
        pass
    
    def render(self, display):
        mouse_pos = pygame.mouse.get_pos()
        display.fill((0, 0, 0))
        self.app.drawText(display, "Game State", (255, 255, 255), self.app.settings["width"]//4, self.app.settings["height"]//4)
        # self.app.drawText(display, "Mouse", (255, 255, 255), mouse_pos[0], mouse_pos[1])

        