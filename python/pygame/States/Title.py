import pygame
from States.State import State
from Button import Button

class Title(State):

    def __init__(self, app):
        State.__init__(self, app)
        self.newgame_button = Button(self.app, "this is a button", \
                                     self.app.color["BLACK"], \
                                     self.app.settings["width"]//4, \
                                     self.app.settings["height"]//4)

    def update(self, dt):
        if self.newgame_button.hovered:
            self.newgame_button.hoverText("Start!")
        self.newgame_button.update()

    def render(self, display):
        display.fill((255, 255, 255))
        self.newgame_button.render()
        

    def drawButton(self, display, text, color, x, y):
        hovered = False
        button_surface = self.app.font.render(text, False, color)
        rect = button_surface.get_rect()
        rect.center = (x, y)
        if rect.collidepoint(pygame.mouse.get_pos()):
            hovered = True
        display.blit(button_surface, rect)

