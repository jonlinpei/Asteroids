from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        # self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        # pygame.draw.circle(self.image, (128, 128, 128), (radius, radius), radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (128, 128, 128), (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_angle = random.uniform(20, 50)
            new_velocity_1 = self.velocity.rotate(new_angle)
            new_velocity_2 = self.velocity.rotate(-new_angle)
            new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_1.velocity = new_velocity_1 * 1.2
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_2.velocity = new_velocity_2 * 1.2