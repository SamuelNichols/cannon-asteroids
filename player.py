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
        self.idle_sprite = a_ss.ASTEROID_SS.create_sprite(a_ss.IDLE_SHIP_RECT, 1, 90)
        self.moving_sprite = a_ss.ASTEROID_SS.create_sprite(a_ss.MOVING_SHIP_RECT, 1, 90)
        self.show_hitbox = constants.DEBUG_ENABLED
        self.velocity = 0

    def draw(self, screen):
        self.idle_sprite.blit(screen, self.position, self.rotation)
        super().draw(screen) 

    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt

    def accelerate(self, forward, speed):
        if forward:
            if not self.velocity >= constants.PLAYER_MAX_SPEED:
                self.velocity += speed
        else:
            if not self.velocity <= -constants.PLAYER_MAX_SPEED:
                self.velocity -= speed

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * self.velocity * dt
    
    def update(self, dt):
        # handling shot rate limit
        self.shoot_cooldown -= dt
        # handling move with current velocity
        self.move(dt)

        # handling key presses
        keys = pygame.key.get_pressed()

        # turn left
        if keys[pygame.K_a]:
            self.rotate(-dt)
        
        # turn right
        if keys[pygame.K_d]:
            self.rotate(dt)
        
        if keys[pygame.K_w]: # move up
            self.accelerate(True, constants.PLAYER_ACCELERATE_SPEED) 
        else: # decelerate in opposite direction
            if self.velocity > 0:
                self.accelerate(False, constants.PLAYER_DECELERATE_SPEED)
            elif self.velocity < 0:
                self.accelerate(True, constants.PLAYER_DECELERATE_SPEED)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)

    def shoot(self, dt):
        if self.shoot_cooldown <= 0:
            velocity = pygame.Vector2(0, 1).rotate(self.rotation) * (constants.PLAYER_SHOOT_SPEED + self.velocity)
            s = Shot(self.position.x, self.position.y, velocity=velocity, shot_distance=constants.MAX_SHOT_DISTANCE)
            self.shoot_cooldown = constants.PLAYER_SHOOT_COOLDOWN

