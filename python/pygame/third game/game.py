#completed 3hr simple game
import random
import pygame,sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((1000,500))

pygame.display.set_caption("ping-pong-ball")

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
AQUA = (0,255,255)
WGREY = (200,200,200)
BGREY = (100,100,100)

DISPLAYSURF.fill(BLACK)

speed = 50

fpsClock = pygame.time.Clock()

font1Obj = pygame.font.Font("freesansbold.ttf", 28)

ball = pygame.image.load("ball.png")
ballobj = ball.get_rect()
ballobj.centerx = 500
ballobj.centery = 300
balldirection = "left"
ballydirection = "up"
angle = 0

player1y = 150
player2y = 150

scoreA = 0
scoreB = 0
while True:
	fpsClock.tick(speed)

	DISPLAYSURF.fill(BLACK)
	player1 = pygame.draw.rect(DISPLAYSURF,RED,(10,player1y,20,100))
	player2 = pygame.draw.rect(DISPLAYSURF,BLUE,(960,player2y,20,100))
	
	if balldirection == "left":
		ballobj.centerx -= 5
	else:
		ballobj.centerx += 5

	if ballydirection == "up":
		ballobj.centery -= angle
	else:
		ballobj.centery += angle
	
	if ballobj.centery <= 15:
		ballydirection = "down"
	if ballobj.centery >= 485:
		ballydirection = "up"
	
	if ballobj.centerx <= 5:
		scoreB += 1
		ballobj.centerx = 200
		balldirection = "right"
	if ballobj.centerx >= 995:
		scoreA += 1
		ballobj.centerx = 800
		balldirection = "left"

	keyinput = pygame.key.get_pressed()
	
	#key inputs
	if keyinput[pygame.K_p]:
		while True:
			pygame.draw.rect(DISPLAYSURF,BGREY,(150,100,700,300))
			pygame.draw.rect(DISPLAYSURF,BLACK,(150,100,700,300),5)
			
			pauseSurfaceObj = font1Obj.render("Game Paused", True, WHITE, BLACK)
			pauseRectObj = pauseSurfaceObj.get_rect()
			pauseRectObj.center = (500, 130)
			DISPLAYSURF.blit(pauseSurfaceObj, pauseRectObj)

			text2SurfaceObj = font1Obj.render("Press R to Resume", True, WHITE, BLACK)
			text2RectObj = text2SurfaceObj.get_rect()
			text2RectObj.center = (500, 270)
			DISPLAYSURF.blit(text2SurfaceObj, text2RectObj)

			text3SurfaceObj = font1Obj.render("Player 1 Score:- %d" % scoreA, True, WHITE, RED)
			text3RectObj = text3SurfaceObj.get_rect()
			text3RectObj.center = (290, 350)
			DISPLAYSURF.blit(text3SurfaceObj, text3RectObj)

			text3SurfaceObj = font1Obj.render("Player 2 Score:- %d" % scoreB, True, WHITE, BLUE)
			text3RectObj = text3SurfaceObj.get_rect()
			text3RectObj.center = (690, 350)
			DISPLAYSURF.blit(text3SurfaceObj, text3RectObj)

			pausekeyinput = pygame.key.get_pressed()

			if pausekeyinput[pygame.K_r]:
				break
			#close event
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
			pygame.display.update()
	elif keyinput[pygame.K_ESCAPE]:
		pygame.quit()
		sys.exit()
	elif keyinput[pygame.K_DOWN]:
		if player2y < 390:
			player2y += 5
	elif keyinput[pygame.K_UP]:
		if player2y > 10:
			player2y -= 5
	elif keyinput[pygame.K_s]:
		if player1y < 390:
			player1y += 5
	elif keyinput[pygame.K_w]:
		if player1y > 10:
			player1y -= 5

	if player1.colliderect(ballobj):
		balldirection = "right"
		if ballydirection == "up":
			tmp = random.randint(0,1)
			if tmp == 1:
				ballydirection = "down"
		elif ballydirection == "down":
			tmp = random.randint(0,1)
			if tmp == 1:
				ballydirection = "up"
		angle = random.randint(0,5)
	if player2.colliderect(ballobj):
		balldirection = "left"
		if ballydirection == "down":
			tmp = random.randint(0,1)
			if tmp == 1:
				ballydirection = "up"
		elif ballydirection == "up":
			tmp = random.randint(0,1)
			if tmp == 1:
				ballydirection = "down"
		angle = random.randint(0,5)
	
	if scoreA == 5:
		while True:
			pygame.draw.rect(DISPLAYSURF,BGREY,(150,100,700,300))
			pygame.draw.rect(DISPLAYSURF,BLACK,(150,100,700,300),5)

			quit1SurfaceObj = font1Obj.render("Red Player Won", True, WHITE, RED)
			quit1RectObj = quit1SurfaceObj.get_rect()
			quit1RectObj.center = (490, 230)
			DISPLAYSURF.blit(quit1SurfaceObj, quit1RectObj)
			
			quit1aSurfaceObj = font1Obj.render("Press esc or q to exit", True, WHITE, BLACK)
			quit1aRectObj = quit1aSurfaceObj.get_rect()
			quit1aRectObj.center = (490, 330)
			DISPLAYSURF.blit(quit1aSurfaceObj, quit1aRectObj)
			

			quit1keyinput = pygame.key.get_pressed()

			if quit1keyinput[pygame.K_ESCAPE] or quit1keyinput[pygame.K_q]:
				pygame.quit()
				sys.exit()

			#close event
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
			pygame.display.update()
	if scoreB == 5:
		while True:
			pygame.draw.rect(DISPLAYSURF,BGREY,(150,100,700,300))
			pygame.draw.rect(DISPLAYSURF,BLACK,(150,100,700,300),5)

			quit2SurfaceObj = font1Obj.render("Blue Player Won", True, WHITE, BLUE)
			quit2RectObj = quit2SurfaceObj.get_rect()
			quit2RectObj.center = (490, 230)
			DISPLAYSURF.blit(quit2SurfaceObj, quit2RectObj)
			
			quit2aSurfaceObj = font1Obj.render("Press esc or q to exit", True, WHITE, BLACK)
			quit2aRectObj = quit2aSurfaceObj.get_rect()
			quit2aRectObj.center = (490, 330)
			DISPLAYSURF.blit(quit2aSurfaceObj, quit2aRectObj)
			

			quit2keyinput = pygame.key.get_pressed()

			if quit2keyinput[pygame.K_ESCAPE] or quit2keyinput[pygame.K_q]:
				pygame.quit()
				sys.exit()

			#close event
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
			pygame.display.update()
	#close event
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	
	score1SurfaceObj = font1Obj.render("Score:- %d" % scoreA, True, WHITE, RED)
	score1RectObj = score1SurfaceObj.get_rect()
	score1RectObj.center = (90, 30)
	DISPLAYSURF.blit(score1SurfaceObj, score1RectObj)

	score2SurfaceObj = font1Obj.render("Score:- %d" % scoreB, True, WHITE, BLUE)
	score2RectObj = score2SurfaceObj.get_rect()
	score2RectObj.center = (890, 30)
	DISPLAYSURF.blit(score2SurfaceObj, score2RectObj)

	DISPLAYSURF.blit(ball,ballobj)
	pygame.display.update()