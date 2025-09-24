import pygame
import constants
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from spritesheet import SpriteSheet, Sprite

class Game:
    def __init__(self):
        pygame.init()
        self.running = False
        self.canvas = pygame.Surface((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        self.screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        self.screen_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()
        self.dt = 0

    def tick(self):
        # tick game and update dt to time since last game tick
        self.dt = self.clock.tick(constants.GAME_TICK) / constants.MILLI_TO_SECONDS

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def game_over(self):
        print("Game over!")
        self.running = False

    def run(self):
        # init game world, move this later 
        # create groups
        updatable = pygame.sprite.Group()
        drawable = pygame.sprite.Group()
        asteroids = pygame.sprite.Group()
        shots = pygame.sprite.Group()
        screen_wrap = pygame.sprite.Group()

        Player.containers = (updatable, drawable, screen_wrap)
        Asteroid.containers = (updatable, drawable, asteroids, screen_wrap)
        AsteroidField.containers = (updatable)
        Shot.containers = (updatable, drawable, shots, screen_wrap)

        # create objects
        player = Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
        _asteroid_field = AsteroidField()

        # begin game loop
        self.running = True
        while self.running:
            # TODO: make background spacey
            self.screen.fill("black")


            for i in screen_wrap:
                i.reposition(self.screen_rect)

            for u in updatable:
                u.update(self.dt)

            for d in drawable:
                d.draw(self.screen)

            for a in asteroids:
                if a.is_colliding(player):
                    # self.game_over()
                    pass
                else:
                    for s in shots:
                        if a.is_colliding(s):
                            a.split()
                            s.kill()


            pygame.display.flip()
            # handle events
            self.handle_event()


            # end of current game loop signal game tick
            self.tick()
        
        # all operations over, running set to false, quit
        pygame.quit()