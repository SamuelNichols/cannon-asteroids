import pygame
import constants
import assets.asteroids_ss as a_ss
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y, color=constants.PLAYER_COLOR, lw=constants.PLAYER_LINE_WIDTH):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown = 0
        self.color = color
        self.line_width = lw
        self.idle_sprite = a_ss.ASTEROID_SS.create_sprite(a_ss.IDLE_SHIP_RECT, 1, 90)
        self.moving_sprite = a_ss.ASTEROID_SS.create_sprite(a_ss.MOVING_SHIP_RECT, 1, 90)
        self.show_hitbox = True

    def set_color(self, color):
        self.color = color

    def set_line_width(self, lw):
        self.line_width = lw

    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, self.triangle(), self.line_width)
        self.idle_sprite.blit(screen, self.position, self.rotation)
        super().draw(screen)

    def update(self, dt):
        # handling shot rate limit
        self.shoot_cooldown -= dt

        # handling key presses
        keys = pygame.key.get_pressed()

        # turn left
        if keys[pygame.K_a]:
            self.rotate(-dt)
        
        # turn right
        if keys[pygame.K_d]:
            self.rotate(dt)
        
        # move up
        if keys[pygame.K_w]:
            self.move(dt)

        # move down
        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            self.shoot(dt)

    def shoot(self, dt):
        if self.shoot_cooldown <= 0:
            s = Shot(self.position.x, self.position.y)
            s.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * constants.PLAYER_SHOOT_SPEED
            self.shoot_cooldown = constants.PLAYER_SHOOT_COOLDOWN
