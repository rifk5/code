import pygame

from Board import Board 

class Game():
    
    def __init__(self, title):
        pygame.init()
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.width, self.height = 740, 740
        self.window = pygame.display.set_mode((self.width, self.height))
        self.running = True
        self.board = Board()
        
    def update(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.board.selectPiece()

        self.board.update()
    
    def render(self) -> None:
        self.board.render(self.window)
        pygame.display.flip()
        
    def start(self) -> None:
        while self.running:
            self.update()
            self.render()
            self.clock.tick(30)
        pygame.quit()
        quit()

if __name__ == "__main__":
    app = Game("Chess in Python")
    app.start()