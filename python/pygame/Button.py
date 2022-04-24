import pygame

class Button:
    def __init__(self, surface, image, scale, x, y):
        width = image.get_width()
        height = image.get_height()
        self.surface = surface
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    
    def update(self) -> bool:
        action = False
        pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return action
     
    def render(self, display):
        display.blit(self.image, (self.rect.x, self.rect.y))