from numpy import kaiser
import pygame, os, time

from Configuration import Configuration
from States.Title import Title

class Application:

    def __init__(self, title):
        pygame.init()
        pygame.display.set_caption(title)
        self.loadConfig()
        self.screen_size = (self.settings["width"], self.settings["height"])
        self.screen_center = (self.settings["width"]//2, self.settings["height"]//2)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.screen_size)
        self.canvas = pygame.Surface(self.screen_size)
        self.dt, self.prev_time = 0, time.time()
        self.state_stack = []
        self.loadAssets()
        self.loadStates()
        self.running = True

    def loadConfig(self):
        self.config = Configuration("assets/settings.ini")
        self.settings = {
            "width": self.config.parser.getint("DISPLAY", "width"),     # 700
            "height": self.config.parser.getint("DISPLAY", "height"),   # 500
            "fps": self.config.parser.getint("DISPLAY", "fps")          # 60
        }

    def loadAssets(self):
        self.color = { "WHITE":     (255,255,255),
                       "BLACK":     (0, 0, 0),
                       "RED":       (255, 0, 0),
                       "GREEN":     (0, 255, 0),
                       "BLUE":      (0, 0, 255),
                       "ORANGE":    (230, 97, 29),
        }
        '''
        └── assets/
            │
            ├── settings.ini
            ├── font/
            │     │
            │     └── slkscr.ttf
            └── sprite/
                    │
                    ├── button/
                    │      │
                    │      ├── start_button.png
                    │      └── exit_button.png
                    ├── ...
                    └── ...
        '''
        self.absolute_dir = os.path.join("/home/delarosa/Git/programming/python/pygame/")

        # assets
        self.assets_dir = os.path.join(self.absolute_dir, "assets")
        self.font_dir = os.path.join(self.assets_dir, "fonts")
        self.sprite_dir = os.path.join(self.assets_dir, "sprites")
        self.button_dir = os.path.join(self.sprite_dir, "buttons")

        # font
        self.font = pygame.font.Font(os.path.join(self.font_dir, "slkscr.ttf"), 32)
        self.font_small = pygame.font.Font(os.path.join(self.font_dir, "slkscr.ttf"), 24)

        self.loadConfig()

    def loadStates(self):
        self.title_screen = Title(self)
        self.state_stack.append(self.title_screen)

    def updateDt(self):
        now = time.time()
        self.dt = now - self.prev_time
        self.prev_time = now

    def updateEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def drawText(self, surface, text, color, x, y):
        text_surface = self.font.render(text, False, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_surface, text_rect)

    def update(self):
        self.updateEvents()
        self.state_stack[-1].update(self.dt)

    def render(self):
        self.state_stack[-1].render(self.canvas)
        self.screen.blit(pygame.transform.scale(self.canvas, self.screen_size), (0, 0))
        pygame.display.flip()

    def start(self):
        while self.running:
            self.clock.tick(self.settings["fps"])
            self.update()
            self.render()
        pygame.quit()
        quit()

if __name__== "__main__":
    app = Application("Python Game 2022")
    app.start()
