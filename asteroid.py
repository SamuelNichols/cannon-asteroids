import pygame
import random
import constants
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, constants.ASTEROID_COLOR, pygame.Vector2(self.position.x, self.position.y), self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        
        split_angle = random.uniform(constants.ASTEROID_SPLIT_ANGLE_MIN, constants.ASTEROID_SPLIT_ANGLE_MAX)
        split_ast_1 = Asteroid(self.position.x, self.position.y, self.radius - constants.ASTEROID_MIN_RADIUS)
        split_ast_2 = Asteroid(self.position.x, self.position.y, self.radius - constants.ASTEROID_MIN_RADIUS)
        split_ast_1.velocity = self.velocity.rotate(split_angle) * constants.ASTEROID_SPLIT_SPEED_MULT
        split_ast_2.velocity = self.velocity.rotate(-split_angle) * constants.ASTEROID_SPLIT_SPEED_MULT

