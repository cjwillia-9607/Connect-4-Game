STATES = ['UNFINISHED', 'X_WON', 'O_WON', 'DRAW']

class ConnectFour:
    # if given board, assumes unfinished game
    def __init__(self, width=7, height=6, connect=4, pieces=('X', 'O'), board=None):
        self.width = width
        self.height = height
        self.connect = connect
        self.pieces = pieces
        if board:
            self.board = board
        else:
            self.board = [' ' for _ in range(self.width * self.height)]
        self.state = 'UNFINISHED'
        self.current_piece = pieces[0]
    
    def insert(self, col, piece):
        if col < 0 or col >= self.width:
            raise ValueError('Invalid column')
        if self.board[col] != ' ':
            raise ValueError('Column is full')
        
        for row in range(self.height-1, -1, -1):
            if self.board[row * self.width + col] == ' ':
                self.board[row * self.width + col] = piece
                self.update_state(piece)
                break
    
    def is_full(self):
        return ' ' not in self.board
    
    def update_state(self, piece):
        if self.is_winner(piece):
            self.state = '{p}_WON'.format(p=piece)
        elif self.is_full():
            self.state = 'DRAW'
        self.current_piece = self.pieces[(self.pieces.index(piece) + 1) % len(self.pieces)]
    
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
    
    # make a string representation of the board
    def __str__(self):
        # print(self.board)
        result = ''
        for row in range(self.height):
            for col in range(self.width):
                result += self.board[row * self.width + col] + '|'
            result += '\n'
        return result

if __name__ == '__main__':
    c4 = ConnectFour()
    c4.insert(0, 'X')
    c4.insert(1, 'O')
    c4.insert(1, 'X')
    c4.insert(2, 'O')
    c4.insert(2, 'X')
    c4.insert(2, 'X')
    c4.insert(3, 'X')
    c4.insert(3, 'O')
    c4.insert(3, 'X')
    c4.insert(3, 'X')
    # c4.insert(4, 'X')
    # c4.insert(4, 'O')
    # c4.insert(4, 'X')
    # c4.insert(4, 'O')
    # c4.insert(5, 'X')
    print(c4)
    print(c4.state)