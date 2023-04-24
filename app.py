from constants import WIDTH, HEIGHT
from loader import loadImages
from tile import Tile
import pygame


class App:
    def __init__(self) -> None:
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Wave Function Collapse(Grid)")
        
        self.setup()

    def setup(self):
        '''
        Description:

            initializes required variables, etc.
            Called once during initialization
        '''
        images = loadImages(6)

        self.baseTiles = []
        for i, img in enumerate(images):
            self.baseTiles.append(Tile(i, images[i]))

    def check_events(self):
        '''
        Description:

            called every main event loop iteration
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # if close button pressed
                self.running = False

    def update(self):
        '''
        Description:

            event loop update method
        '''
        pygame.display.update()

    def run(self):
        '''
        Description:

            main event loop
        '''
        self.running = True
        while self.running:
            self.check_events()
            self.update()

        pygame.quit()
        quit()


if __name__ == '__main__':
    app = App()
    app.run()
