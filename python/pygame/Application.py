import pygame, os, time

from Configuration import Configuration
from States.Title import Title
from States.Game import Game

class Application:

    def __init__(self, title):
        pygame.init()
        pygame.display.set_caption(title)
        self.loadConfig()
        self.clock = pygame.time.Clock()
        self.canvas = pygame.Surface((self.settings["width"]//2, self.settings["height"]//2))
        self.screen = pygame.display.set_mode((self.settings["width"], self.settings["height"]))
        self.dt, self.prev_time = 0, time.time()
        self.state_stack = []
        self.loadAssets()
        self.loadStates()
        self.running = True

    def loadConfig(self):
        self.config = Configuration("assets/settings.ini")
        self.settings = {
            "width": self.config.parser.getint("DISPLAY", "width"),
            "height": self.config.parser.getint("DISPLAY", "height"),
            "fps": self.config.parser.getint("DISPLAY", "fps")
        }

    def loadAssets(self):
        self.color = { "WHITE": (255,255,255),
                        "BLACK": (0, 0, 0),
                        "RED": (255, 0, 0),
                        "GREEN": (0, 255, 0),
                        "BLUE": (0, 0, 255) }
        self.absolute_dir = os.path.join("/home/delarosa/Git/programming/python/pygame/")
        self.assets_dir = os.path.join(self.absolute_dir, "assets")
        self.sprite_dir = os.path.join(self.assets_dir, "sprites")
        self.font_dir = os.path.join(self.assets_dir, "font")
        self.font = pygame.font.Font(os.path.join(self.font_dir, "slkscr.ttf"), 16)
        self.keys = pygame.key.get_pressed()
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

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    game_state = Game(self)
                    game_state.enterState()

            self.title_screen.newgame_button.click(event)
    
    def update(self):
        self.updateEvents()
        self.state_stack[-1].update(self.dt)

    def render(self):
        self.state_stack[-1].render(self.canvas)
        self.screen.blit(pygame.transform.scale(self.canvas, (self.settings["width"], \
                                                              self.settings["height"])), (0, 0))
        pygame.display.flip()

    def drawText(self, surface, text, color, x, y):
        text_surface = self.font.render(text, False, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_surface, text_rect)

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
