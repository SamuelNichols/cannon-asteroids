import pygame
import constants
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.SHOT_RADIUS)
        self.origin = pygame.Vector2(x, y)

    def draw(self, screen):
        pygame.draw.circle(screen, constants.SHOT_COLOR, pygame.Vector2(self.position.x, self.position.y), self.radius)

    def update(self, dt):
        new_pos = self.position + (self.velocity * dt)
        new_dest = self.origin.distance_to(new_pos)
        if new_dest > constants.MAX_SHOT_DISTANCE:
            self.kill()
        elif new_dest == constants.MAX_SHOT_DISTANCE:
            self.position = new_pos
            self.kill()
        else:
            self.position = new_pos

