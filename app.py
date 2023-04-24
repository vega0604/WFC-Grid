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
        images = loadImages(6)

        self.baseTiles = []
        for i, img in enumerate(images):
            self.baseTiles.append(Tile(0, i, images[i]))

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pygame.display.update()

    def run(self):
        self.running = True
        while self.running:
            self.check_events()
            self.update()

        pygame.quit()
        quit()


if __name__ == '__main__':
    app = App()
    app.run()
