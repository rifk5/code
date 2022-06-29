import pygame, os

class Entity(pygame.sprite.Sprite):
    
    def __init__(self, app, pos, groups):
        self.image = pygame.image.load(os.path.join(app.player_dir, ""))
        super().__init__(groups)
    