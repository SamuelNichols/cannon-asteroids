import pygame
import constants

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        self.show_hitbox = False
    
    def is_colliding(self, other):
        distance = self.position.distance_to(other.position)
        return distance < (self.radius + other.radius)

    def draw(self, screen):
        if self.show_hitbox:
            pygame.draw.circle(screen, constants.HITBOX_COLOR, self.position, self.radius, width=2)

    def update(self, dt):
        pass