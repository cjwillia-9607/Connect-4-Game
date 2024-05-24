import pygame
from connect_four import ConnectFour
RESOLUTION = (800, 700)
class Game:
    def __init__(self):
        self.pieces = ('RED', "BLUE")
        self.game = ConnectFour(width=7, height=6, connect=4, pieces=self.pieces)
        self.game_width = self.game.width
        self.game_height = self.game.height
    
        pygame.init()
        self.screen = pygame.display.set_mode(RESOLUTION)
        pygame.display.set_caption('Hello World')
        self.clock = pygame.time.Clock()
        self.running = True
        
        self.current_piece = 0

    def run(self):
        while self.running:
            self._handle_events()
            self._update()
            self._draw()
            self.clock.tick(60)  # limits FPS to 60

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                row = None
                if event.key == pygame.K_1:
                    row = 0
                if event.key == pygame.K_2:
                    row = 1
                if event.key == pygame.K_3:
                    row = 2
                if event.key == pygame.K_4: 
                    row = 3
                if event.key == pygame.K_5:     
                    row = 4
                if event.key == pygame.K_6:
                    row = 5
                if event.key == pygame.K_7:
                    row = 6

                
                if row is not None:
                    try:
                        self.game.insert(row, self.pieces[self.current_piece])
                        self.current_piece = (self.current_piece + 1) % len(self.pieces)
                    except ValueError:
                        print('Column is full')
                
                if self.game.state != 'UNFINISHED':
                    print(self.game.state)
                        
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                

    def _update(self):
        pass

    def _draw(self):
        self.screen.fill((255, 255, 255))
        pygame.draw.rect(self.screen, (0, 0, 0), (50, 50, 700, 600), 5)
        for row in range(self.game_height):
            for col in range(self.game_width):
                piece = self.game.board[row * self.game_width + col]
                if piece != ' ':
                    color = (255, 0, 0) if piece == self.pieces[0] else (0, 0, 255)
                    pygame.draw.circle(self.screen, color, (100 + col * 100, row * 100 + 100), 40)
        pygame.display.flip()

    def quit(self):
        pygame.quit()

if __name__ == '__main__':
    connect_four = Game()
    connect_four.run()