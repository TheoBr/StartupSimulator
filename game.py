#! /usr/bin/env python

import pygame, sys
from pygame.locals import *
from companyState import *


def main():
	company = CompanyState("Tinder")

	# Initialise screen
	pygame.init()
	screen = pygame.display.set_mode((640, 400))
	pygame.display.set_caption('Startup Simulator')

	# Fill background
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((250, 250, 250))

	# Display some text
	font = pygame.font.Font(None, 36)
	text = font.render(company.companyName, 1, (10, 10, 10))
	textpos = text.get_rect()
	textpos.centerx = background.get_rect().centerx
	background.blit(text, textpos)

	# Blit everything to the screen
	screen.blit(background, (0, 0))
	pygame.display.flip()



	# Event loop
	while 1:
		for event in pygame.event.get():
			if event.type == QUIT:
				return

		screen.blit(background, (0, 0))
		pygame.display.flip()


if __name__ == '__main__':
	main()




