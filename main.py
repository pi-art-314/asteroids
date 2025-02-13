import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()
Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable)
Shot.containers = (shots, updatable, drawable)

def main():
	pygame.init
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2
	test_player = Player(x, y)
	asteroidfield = AsteroidField()
	game_clock = pygame.time.Clock()
	dt = 0
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		updatable.update(dt)
		for asteroid in asteroids:
			if asteroid.collide(test_player) == True:
				print("Game over!")
				return
		screen.fill("black")
		for obj in drawable:
			obj.draw(screen)
		pygame.display.flip()
		dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
	main()
