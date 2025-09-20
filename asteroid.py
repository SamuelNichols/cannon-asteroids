import pygame
import random
import constants
import assets.asteroids_ss as a_ss
from spritesheet import SpriteSheet, Sprite
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        r = radius // constants.ASTEROID_MIN_RADIUS
        kind = random.randint(1, constants.ASTEROID_KINDS)
        asteroid_sprite_rect = a_ss.ASTEROID_SPRITE_LIST[((r-1) * constants.ASTEROID_KINDS) + (kind - 1)]
        self.sprite = a_ss.ASTEROID_SS.create_sprite(asteroid_sprite_rect, 1)
        self.show_hitbox = True

    def draw(self, screen):
        self.sprite.blit(screen, self.position)
        super().draw(screen)
    
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

