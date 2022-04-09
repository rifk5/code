import pygame

from Configuration import Configuration

BLACK   = (0, 0, 0)
WHITE   = (255, 255, 255)
RED     = (255, 0, 0)
GREEN   = (0, 255, 0)
BLUE    = (0, 0, 255)

class Application:

    def __init__(self, title):
        pygame.init()
        pygame.display.set_caption(title)
        self.settings = Configuration("settings.ini")
        self.settings.load()
        self.clock = pygame.time.Clock()
        self.canvas = pygame.display.set_mode((self.settings.parser.getint("DISPLAY", "width"),
                                              self.settings.parser.getint("DISPLAY", "height")))
        self.running = True

    def updateEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.updateEvents()

    def render(self):
        self.canvas.fill(WHITE)
        pygame.draw.rect(self.canvas, RED, [55, 200, 100, 70],0)
        pygame.draw.line(self.canvas, GREEN, [0, 0], [100, 100], 5)
        pygame.draw.ellipse(self.canvas, BLACK, [20,20,250,100], 2)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.update()
            self.render()
            self.clock.tick(60)
        pygame.quit()
