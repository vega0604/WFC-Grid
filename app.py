from constants import WIDTH, HEIGHT, GRID_SIZE
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

        # Grid Setup
        self.grid = []
        for y in range(GRID_SIZE**2):
            self.grid.append(Tile())

    def check_events(self):
        '''
        Description:

            called every main event loop iteration
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # if close button pressed
                self.running = False

    def draw(self):
        '''
        Description:


        '''
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                tile = self.grid[x + GRID_SIZE*y]
                if tile.type == None:
                    continue

                self.win.blit(tile.img,(x * (WIDTH/GRID_SIZE), y * (WIDTH/GRID_SIZE)))

    def update(self):
        '''
        Description:

            event loop update method
        '''
        # self.next()
        self.draw()
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
