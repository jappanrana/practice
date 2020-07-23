"""
Fractal Tree
Made by jappan rana
time -2hrs
took time to figure out how to give angle
got angle formula from net used it in my code
"""
#importing pygame to display and draw things
#importing math to calculate angle
#Random for getting random angles
import pygame, sys
import math
import random
from pygame.locals import *

pygame.init()

FPS = 1
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((1000, 700))
pygame.display.set_caption('Fractal Tree')

White = (255, 255, 255)
Black = (0, 0, 0)
Green = (  0, 128,   0)
Maroon = (128,  0,   0)

branch = 11
size = 23
sx = 500
sy = 650
angle = -90
def drawline(sx, sy, angle, branch, size):
	#will stop recursion at branch 0 since all branches will be drawn already
	if branch:
		#formula from net which gives exact coordinates for ending point
		ex = sx + int(math.cos(math.radians(angle)) * branch * 10.0)
		ey = sy + int(math.sin(math.radians(angle)) * branch * 10.0)
		#draw leaves on last branch
		if branch != 1:
			pygame.draw.line(DISPLAYSURF, Maroon, (sx, sy), (ex, ey), size)
		else:
			pygame.draw.line(DISPLAYSURF, Green, (sx, sy), (ex, ey), size)
		#reduce size of stem and branches
		size -= 2
		#getting random values to add and subtract from angle
		mang = random.randint(20,60)
		pang = random.randint(20,60)
		#recursion for drawing right and left branch of each parent branch
		drawline(ex, ey, angle - mang, branch - 1,size)
		drawline(ex, ey, angle + pang, branch - 1,size)
#loop to start pygame screen
while True:
	#bg color
	DISPLAYSURF.fill(Black)
	#calling function every second to change desing for each frame
	drawline(sx, sy, angle, branch, size)
	#pygame event
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()
	fpsClock.tick(FPS)