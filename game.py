#! /usr/bin/env python

import pygame, sys, time, string
from pygame.locals import *
from companyState import *

pygame.init()
blue = 0, 0, 255
font = pygame.font.Font(None, 36)

def header(screen, companyState):

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
	    event = pygame.event.poll()
	    if event.type== pygame.QUIT:
	    	running = False

	    screen = header(screen, company)
	    pygame.display.flip()

	    company.tickTime()
	    time.sleep(2)

if __name__ == '__main__':
	main()
