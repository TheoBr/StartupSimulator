#! /usr/bin/env python

import pygame, sys, time, string
from pygame.locals import *
from companyState import *

pygame.init()
blue = 0, 0, 255
background = 0,0,0
font = pygame.font.Font(None, 36)

def header(screen, companyState):

	screen.fill(background)

	width = screen.get_width()
	height = screen.get_height()

	# Draw header line
	point1 = 0, 30
	point2 = screen.get_width(), 30
	pygame.draw.line(screen, blue, point1, point2)

	# Draw company name in header text
	text = font.render(companyState.companyName, 1, blue)
	screen.blit(text, (2, 5))

	# Draw day in header text
	text = font.render(str(companyState.day), 1, blue)
	screen.blit(text, (width-30, 5))

	return screen


def main():

	company = CompanyState("Tinder")

	screen = pygame.display.set_mode((640, 400))
	running = True
	screen.fill((0, 0, 0))

	while running:
        # events for txtbx
		events = pygame.event.get()
        # process other events
		for event in events:
			# close it x button si pressed
			if event.type == QUIT: return

		screen = header(screen, company)
		pygame.display.flip()

		company.tickTime()
		time.sleep(2)

if __name__ == '__main__':
	main()
