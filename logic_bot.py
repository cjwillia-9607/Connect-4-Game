import random
from connect_four import ConnectFour

class LogicBot:
    def __init__(self, piece):
        self.piece = piece
        self.opp_piece = 'X' if piece == 'O' else 'O'
        self.blocked_columns = set()
    
    def choose_column(self, game):
        available_columns = set([c for c in range(game.width) if game.board[c] == ' ']) - self.blocked_columns

        block = self.should_block(game, available_columns)
        # print(block, available_columns)
        return block if block != -1 else random.choice(list(available_columns))
    
    def should_block(self, game, available_columns):
        board = game.board
        width = game.width
        height = game.height
        for col in list(available_columns):
            hypothetical_game = ConnectFour(width=width, height=height, connect=4, pieces=('X', 'O'), board=board[:])
            hypothetical_game.insert(col, self.opp_piece)
            if hypothetical_game.is_winner(self.opp_piece):
                return col
        
        return -1