import pygame
import constants
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, velocity, shot_distance):
        super().__init__(x, y, constants.SHOT_RADIUS)
        self.velocity = velocity
        self.time = 0
        
        self.show_hitbox = constants.DEBUG_ENABLED

    def draw(self, screen):
        pygame.draw.circle(screen, constants.SHOT_COLOR, pygame.Vector2(self.position.x, self.position.y), self.radius)

    def update(self, dt):
        self.time += dt
        if self.time > constants.MAX_SHOT_DISTANCE:
            self.kill()
        elif self.time == constants.MAX_SHOT_DISTANCE:
            self.position += self.velocity * dt
            self.kill()
        else:
            self.position += self.velocity * dt

