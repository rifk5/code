import pygame, os

class Board:
    
    def __init__(self):
        self.loadConfig()
        self.loadImages()
        self.square_size = 63.6
        self.board = [
            ["black_rook", "black_knight", "black_bishop", "black_queen", "black_king", "black_bishop", "black_knight", "black_rook"],
            ["black_pawn", "black_pawn", "black_pawn", "black_pawn", "black_pawn", "black_pawn", "black_pawn", "black_pawn"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "white_pawn", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["white_pawn", "white_pawn", "white_pawn", "white_pawn", "--", "white_pawn", "white_pawn", "white_pawn"],
            ["white_rook", "white_knight", "white_bishop", "white_queen", "white_king", "white_bishop", "white_knight", "white_rook"]]
        self.white_move = True
        self.move_log = []
        self.sq_selected = ()
        self.player_clicks = []
        
    def loadImages(self):
        self.images = {}
        self.pieces = ["white_king", "white_queen", "white_rook", "white_bishop", "white_knight", "white_pawn",
                       "black_king", "black_queen", "black_rook", "black_bishop", "black_knight", "black_pawn"]
        assets_dir = f"assets/{self.color_scheme}/"
        self.board_img = pygame.image.load(os.path.join(assets_dir, "board_alt.png"))

        for piece in self.pieces:
            self.images[piece] = pygame.image.load(os.path.join(assets_dir, f"{piece}.png"))
    
    def loadConfig(self):
        file_name = "assets/settings.ini"

        if os.path.exists(file_name) == False:
            with open(file_name, "w") as f:
                f.write("dark")

        if os.path.exists(file_name):
            with open(file_name, "r") as f:
                self.color_scheme = f.readline()

    def calcBoardCoords(self):
        for x in range(8):
            row = []
            for y in range(8):
                row.append((116 + self.square_size * y, 116 + self.square_size * x))
            self.grid.append(row)
    
    def selectPiece(self):
        location = pygame.mouse.get_pos()
        col = location[0] / (120 + self.square_size)
        row = location[1] / (120 + self.square_size)

        if self.sq_selected == (row, col):
            self.sq_selected = ()
            self.player_clicks = []
        else:
            self.sq_selected = (row, col)
            self.player_clicks.append(self.sq_selected)

        if len(self.player_clicks) == 2:
            
    
    def update(self):
        pass

    def render(self, window: pygame.display):
        window.blit(pygame.transform.scale(self.board_img, (740, 740)), (0, 0))
        # self.drawSquares(window)
        self.drawPieces(window)
    
    def drawPieces(self, window: pygame.display):
        for r in range(8):
            for c in range(8):
                piece = self.board[r][c]
                if piece != "--":
                    window.blit(pygame.transform.scale(self.images[piece], (self.square_size - 10, self.square_size - 10)), 
                                pygame.Rect(120 + self.square_size * c, 120 + self.square_size * r, 64, 64))

    def drawSquares(self, window: pygame.display):
        for x in range(8):
            for y in range(8):
                pygame.draw.rect(window, (0, 100, 255), (116 + self.square_size * y, 116 + self.square_size * x, 64, 64), 1)
            
        