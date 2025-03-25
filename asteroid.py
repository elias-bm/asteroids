import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
       super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        degree = random.uniform(20, 50)
        velocity_one = self.velocity.rotate(degree)
        velocity_two = self.velocity.rotate(-degree)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        split_one = Asteroid(self.position.x, self.position.y, new_radius)
        split_two = Asteroid(self.position.x, self.position.y, new_radius)
        split_one.velocity = velocity_one * 1.2
        split_two.velocity = velocity_two * 1.2