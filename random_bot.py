import random
    
class RandomBot:
    def __init__(self, piece):
        self.piece = piece
    
    def choose_column(self, game):
        available_columns = [c for c in range(game.width) if game.board[c] == ' ']
        return random.choice(available_columns)
