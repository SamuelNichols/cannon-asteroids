import pygame
import constants

class Game:
    def __init__(self):
        pygame.init()
        self.__running = False
        self.__screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

    def run(self):
        self.__running = True
        while self.__running:
            self.__screen.fill("black")
            pygame.display.flip()
            self.handle_event()

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
