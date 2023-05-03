from constants import WIDTH, HEIGHT, GRID_SIZE
from tile import Tile
from random import randint
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
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                self.grid.append(Tile(x, y))

        self.grid[randint(0, GRID_SIZE**2-1)].type = 1
        # self.grid[randint(0, GRID_SIZE**2-1)].type = randint(0, len(TYPES)-1)

    def handleKeydown(self, e):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RETURN]:
            # self.win.fill((0, 0, 0))
            self.win.fill((randint(0, 255), randint(0, 255), randint(0, 255)))
            self.setup()

    def check_events(self):
        '''
        Description:

            called every main event loop iteration
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # if close button pressed
                self.running = False
            if event.type == pygame.KEYDOWN:
                self.handleKeydown(event)

    def draw(self):
        '''
        Description:

            draws tiles to window
        '''
        for tile in self.grid:
            if not tile.collapsed:
                continue

            self.win.blit(tile.img,(tile.x * (WIDTH/GRID_SIZE), tile.y * (HEIGHT/GRID_SIZE)))

    def next(self):
        uncollapsed = list(filter(lambda t: not t.collapsed, self.grid))
        collapsed = list(filter(lambda t: t.collapsed, self.grid))
        if len(uncollapsed) < 1:
            return
        
        for tile in uncollapsed:
            tile.calcEnt(collapsed)

        nextTile = min(uncollapsed, key=lambda t: t.entropy)
        # print(f'x: {nextTile.x}, y: {nextTile.y}, entropy: {nextTile.entropy}')

        nextTile.collapse()

    def update(self):
        '''
        Description:

            event loop update method
        '''
        self.next()
        self.draw()
        pygame.display.update()

    def run(self):
        '''
        Description:

            main event loop
        '''
        clock = pygame.time.Clock()
        self.running = True
        while self.running:
            clock.tick(60)
            self.check_events()
            self.update()

        pygame.quit()
        quit()


if __name__ == '__main__':
    app = App()
    app.run()
