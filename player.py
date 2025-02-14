import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.PLAYER_SHOOT_COOLDOWN = 0


        # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        self.PLAYER_SHOOT_COOLDOWN = max(0, self.PLAYER_SHOOT_COOLDOWN - dt)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rotate(dt * -1)
        if keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_DOWN]:
            self.move(dt * -1)

    def shoot(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            if self.PLAYER_SHOOT_COOLDOWN == 0:
                # Create velocity vector
                forward = pygame.Vector2(0, 1).rotate(self.rotation)
                velocity = forward * PLAYER_SHOOT_SPEED
            
                # Create new shot at player's position with calculated velocity
                Shot(self.position.x, self.position.y, velocity)

                #SHOT COOLDOWN
                self.PLAYER_SHOOT_COOLDOWN = PLAYER_SHOOT_COOLDOWN