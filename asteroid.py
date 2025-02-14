import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
       
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)


    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        else:
            random_angle = random.uniform(20, 50)
            new_velocity_1 = pygame.math.Vector2.rotate(self.velocity, random_angle) * 1.4
            new_velocity_2 = pygame.math.Vector2.rotate(self.velocity, - random_angle) * 1.4
            new_radius_1 = self.radius - ASTEROID_MIN_RADIUS
            new_radius_2 = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius_1)
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius_2)
            asteroid_1.velocity = new_velocity_1
            asteroid_2.velocity = new_velocity_2




            



