import random
import pygame
import circleshape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        velocity_one = self.velocity.rotate(random_angle)
        velocity_two = self.velocity.rotate(-random_angle)

        asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_one = Asteroid(self.position.x, self.position.y, asteroid_radius)
        asteroid_two = Asteroid(self.position.x, self.position.y, asteroid_radius)

        asteroid_one.velocity = velocity_one * 1.2
        asteroid_two.velocity = velocity_two * 1.2