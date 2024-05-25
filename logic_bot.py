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

class MinMaxBot:
    def __init__(self, piece):
        self.piece = piece

    def evaluate(self, game):
        opponent_piece = game.pieces[(game.pieces.index(self.piece) + 1) % len(game.pieces)]
        if game.is_winner(self.piece):
            return 1000
        elif game.is_winner(opponent_piece):
            return -1000
        return 0

    def minimax(self, depth, maximizingPlayer, game):
        opponent_piece = game.pieces[(game.pieces.index(self.piece) + 1) % len(game.pieces)]
        possible_moves = [c for c in range(game.width) if game.board[c] == ' ']
        score = self.evaluate(game)

        if score == 1000 or score == -1000:
            return score
        if game.is_full():
            return 0

        if maximizingPlayer:
            best = -float('inf')
            for col in possible_moves:
                game_copy = game.copy_gamestate()
                game_copy.insert(col, self.piece)
                best = max(best, self.minimax(depth + 1, False, game_copy))
            return best
        else:
            best = float('inf')
            for col in possible_moves:
                game_copy = game.copy_gamestate()
                game_copy.insert(col, opponent_piece)
                best = min(best, self.minimax(depth + 1, True, game_copy))
            return best
    
    def choose_column(self, game):
        possible_moves = [c for c in range(game.width) if game.board[c] == ' ']
        best_val = -float('inf')
        best_move = -1

        for col in possible_moves:
            game_copy = game.copy_gamestate()
            game_copy.insert(col, self.piece)
            move_val = self.minimax(0, False, game_copy)

            if move_val > best_val:
                best_move = col
                best_val = move_val

        return best_move
