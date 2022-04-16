import pygame

class Button:

    def __init__(self, app, text, color, x, y):
        self.hovered = False
        self.app = app
        self.ori_text, self.ori_color = text, color
        self.text, self.color = text, color
        self.x, self.y = x, y
        self.text_surface = self.app.font.render(text, False, color)
        self.size = self.text_surface.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(self.app.color["BLUE"])
        self.surface.blit(self.text_surface, (0, 0))
        self.rect = self.text_surface.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.surface = self.app.font.render(self.text, False, self.color)
        self.rect = self.surface.get_rect()
        self.rect.center = (self.x, self.y)
        if self.rect.collidepoint(pygame.mouse.get_pos()): self.hovered = True
        else: self.hovered = False
        print(self.hovered)

    def render(self):
        self.app.canvas.blit(self.surface, self.rect)

    def hoverText(self, text):
        if self.hovered: self.text = text
        else: self.text = self.ori_text

    def hoverColor(self, color):
        if self.hovered: self.color = color
        else: self.color = self.ori_color
    
    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.change_text(self.feedback, bg="red")