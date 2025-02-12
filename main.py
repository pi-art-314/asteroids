import pygame
from constants import *
from player import *

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
Player.containers = (updatable, drawable)

def main():
	pygame.init
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2
	test_player = Player(x, y)
	game_clock = pygame.time.Clock()
	dt = 0
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		updatable.update(dt)
		screen.fill("black")
		for obj in drawable:
			obj.draw(screen)
		pygame.display.flip()
		dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
	main()
