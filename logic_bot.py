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
    def __init__(self, piece, max_depth=3):
        self.piece = piece
        self.max_depth = max_depth

    def evaluate(self, game):
        opponent_piece = game.pieces[(game.pieces.index(self.piece) + 1) % len(game.pieces)]
        if game.is_winner(self.piece):
            return 1000
        elif game.is_winner(opponent_piece):
            return -1000
        return 0

    def minimax(self, depth, alpha, beta, maximizingPlayer, game):
        opponent_piece = game.pieces[(game.pieces.index(self.piece) + 1) % len(game.pieces)]
        possible_moves = [c for c in range(game.width) if game.board[c] == ' ']
        score = self.evaluate(game)

        if score == 1000 or score == -1000:
            return score
        if game.is_full():
            return 0
        if depth == self.max_depth:
            # print("used heuristic")
            # return self.heuristic(game)
            return 0

        if maximizingPlayer:
            best = -float('inf')
            for col in possible_moves:
                game_copy = game.copy_gamestate()
                game_copy.insert(col, self.piece)
                value = self.minimax(depth + 1, alpha, beta, False, game_copy)
                best = max(best, value)
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
            return best
        else:
            best = float('inf')
            for col in possible_moves:
                game_copy = game.copy_gamestate()
                game_copy.insert(col, opponent_piece)
                value = self.minimax(depth + 1, alpha, beta, True, game_copy)
                best = min(best, value)
                beta = min(beta, best)
                if beta <= alpha:
                    break
            return best
    
    def choose_column(self, game):
        possible_moves = [c for c in range(game.width) if game.board[c] == ' ']
        best_val = -float('inf')
        best_move = -1
        bests = []
        for col in possible_moves:
            game_copy = game.copy_gamestate()
            game_copy.insert(col, self.piece)
            move_val = self.minimax(0, -float('inf'), float('inf'), False, game_copy)

            if move_val > best_val:
                best_move = col
                best_val = move_val
                bests.append((best_move, best_val))
                # print(bests)

        return best_move
    
    def heuristic(self, game):
        opponent_piece = game.pieces[(game.pieces.index(self.piece) + 1) % len(game.pieces)]
        score = 0
        score += self.calculate_exposed_pieces(self.piece, game)
        score -= self.calculate_exposed_pieces(opponent_piece, game)
        return score

    def calculate_exposed_pieces(self, piece, game):
        score = 0
        for row in range(game.height):
            for col in range(game.width):
                if game.board[row * game.width + col] == piece:
                    score += self.exposed_piece_score(row, col, piece, game)
        return score

    def exposed_piece_score(self, row, col, piece, game):
        def next_to(row, col, piece=' '):
            if 0 <= row < game.height and 0 <= col < game.width:
                return game.board[row * game.width + col] == piece
            return False
        score = 0
        directions = [
            (-1, 0),  # Vertical
            (0, 1),  # Horizontal
            (0, -1),  # Horizontal
            (1, 1),  # Diagonal (top-left to bottom-right)
            (-1, -1),  # Diagonal (bottom-right to top-left)
            (1, -1),  # Diagonal (top-right to bottom-left)
            (-1, 1)  # Diagonal (bottom-left to top-right)
        ]
        for dr, dc in directions:
            # Check single exposed pieces
            if next_to(row + dr, col + dc):
                score += 1
            # Check pairs of exposed pieces
            # if self.is_exposed(row + dr, col + dc) and self.is_exposed(row + 2 * dr, col + 2 * dc):
            #     score += 3
            if next_to(row + dr, col + dc, piece) and next_to(row + dr, col + dc, piece):
                score += 3
        return score

    
