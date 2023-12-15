import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Hello World')
        self.running = True

    def run(self):
        while self.running:
            self._handle_events()
            self._update()
            self._draw()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def _update(self):
        pass

    def _draw(self):
        pass

    def quit(self):
        pygame.quit()

if __name__ == '__main__':
    connect_four = Game()
    connect_four.run()