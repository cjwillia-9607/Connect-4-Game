class ConnectFour:
    def __init__(self, width=7, height=6, connect=4, pieces=('X', 'O')):
        self.width = width
        self.height = height
        self.connect = connect
        self.pieces = pieces
        self.board = [' ' for _ in range(self.width * self.height)]
    
    def __str__(self):
        result = ''
        for row in range(self.height):
            for col in range(self.width):
                result += self.board[row * self.width + col] + '|'
            result += '\n'
        return result
    
    def insert(self, col, piece):
        if self.board[col] != ' ':
            raise ValueError('Column is full')
        
        for row in range(self.height - 1, 0, -1):
            if self.board[(row - 1) * self.width + col] != ' ':
                self.board[row * self.width + col] = piece
    
    def is_full(self):
        return ' ' not in self.board
    
    def is_winner(self, piece):
        # Horizontal
        for row in range(self.height):
            for col in range(self.width - self.connect + 1):
                if all(self.board[row * self.width + col + i] == piece for i in range(self.connect)):
                    return True
        
        # Vertical
        for row in range(self.height - self.connect + 1):
            for col in range(self.width):
                if all(self.board[(row + i) * self.width + col] == piece for i in range(self.connect)):
                    return True
        
        # Diagonal (top-left to bottom-right)
        for row in range(self.height - self.connect + 1):
            for col in range(self.width - self.connect + 1):
                if all(self.board[(row + i) * self.width + col + i] == piece for i in range(self.connect)):
                    return True
        
        # Diagonal (bottom-left to top-right)
        for row in range(self.connect - 1, self.height):
            for col in range(self.width - self.connect + 1):
                if all(self.board[(row - i) * self.width + col + i] == piece for i in range(self.connect)):
                    return True
        
        return False