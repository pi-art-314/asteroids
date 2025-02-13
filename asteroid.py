import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen, "green", self.position, self.radius, 2)

	def update(self, dt):
		self.position += (self.velocity * dt)

	def split(self):
		self.kill()
		if(self.radius <= ASTEROID_MIN_RADIUS):
			return
		else:
			angle = random.uniform(20, 50)
			rot1 = self.velocity.rotate(angle)
			rot2 = self.velocity.rotate(-angle)
			new_radius = self.radius - ASTEROID_MIN_RADIUS
			new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
			new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
			new_asteroid_1.velocity = rot1 * 1.2
			new_asteroid_2.velocity = rot2 * 1.2
