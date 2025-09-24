import pygame
import constants

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, collision=True):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        self.collision = collision
        self.show_hitbox = constants.DEBUG_ENABLED

    def get_position(self):
        return self.position
    
    def get_rect(self):
        return pygame.Rect(self.position.x, self.position.y, self.radius, self.radius).move(self.position.x, self.position.y)
    
    def is_colliding(self, other):
        distance = self.position.distance_to(other.position)
        return distance < (self.radius + other.radius) and self.collision

    def draw(self, screen):
        if self.show_hitbox:
            pygame.draw.circle(screen, constants.HITBOX_COLOR, self.position, 2)
            pygame.draw.circle(screen, constants.HITBOX_COLOR, self.position, self.radius, width=2)

    def update(self, dt):
        pass


    # returns what edges if any the player has passed (left=True/False, right, top, bottom)
    def is_off_screen(self, left_edge, right_edge, top_edge, bottom_edge):
        return (
            self.position.x < left_edge,
            self.position.x > right_edge,
            self.position.y < top_edge,
            self.position.y > bottom_edge
        )

    def reposition(self, screen_rect):
        (left, top, width, height) = screen_rect
        left_edge = left - constants.SCREEN_EDGE_PADDING
        right_edge = left + width + constants.SCREEN_EDGE_PADDING
        top_edge = top - constants.SCREEN_EDGE_PADDING
        bottom_edge = top + height + constants.SCREEN_EDGE_PADDING

        (past_left, past_right, past_top, past_bottom) = self.is_off_screen(left_edge, right_edge, top_edge, bottom_edge)

        if past_left:
           past = left_edge - self.position.x
           self.position.x = right_edge - past
        elif past_right:
            past = self.position.x - right_edge
            self.position.x = left_edge + past

        if past_top:
            past = top_edge - self.position.y
            self.position.y = bottom_edge - past
        elif past_bottom:
            past = self.position.y - bottom_edge
            self.position.y = top_edge + past