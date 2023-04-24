from constants import WIDTH, HEIGHT
import pygame

class App:
    def __init__(self) -> None:
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Wave Function Collapse(Grid)")

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
