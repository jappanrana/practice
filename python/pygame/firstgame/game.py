#finished at 22/04/2020 took 1 day working 7 hrs total
#last bug fix and feature changes at 24/04/2020
import random
import pygame , sys
from pygame.locals import *

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
AQUA = (0,255,255)
WGREY = (200,200,200)
BGREY = (100,100,100)

pygame.init()

DISPLAYSURF = pygame.display.set_mode((1140,570),0,32)

pygame.display.set_caption("Killer Corona")

#loading images in variables
boy = pygame.image.load("boy.png")
corona = pygame.image.load("corona.png")
vaccine = pygame.image.load("vaccine.png")

#creating list of 5 boys at random position
boys = []
for i in range(5):
	boys.append(boy.get_rect())
	boys[i].centerx = random.randint(35,1000)
	boys[i].centery = random.randint(50,400)
vaccines = []
for i in range(1):
	vaccines.append(vaccine.get_rect())
	vaccines[i].centerx = 500
	vaccines[i].centery = 300
#setting player info
player = corona.get_rect()
player.centerx = 120
player.centery = 100

score = 0

#defining font to use later
fontObj = pygame.font.Font("freesansbold.ttf", 32)

speed = 15
FPS = speed
fpsClock = pygame.time.Clock()
tmp = 0
tmpfsped = 0
while True:
	fpsClock.tick(speed)
	
	DISPLAYSURF.fill(BGREY)
	#displaying updated score
	text1SurfaceObj = fontObj.render("Score:- %d" % score, True, WHITE, BLACK)
	text1RectObj = text1SurfaceObj.get_rect()
	text1RectObj.center = (90, 20)
	
	DISPLAYSURF.blit(text1SurfaceObj, text1RectObj)

	if speed < 80 and score > 4:
		if score%5 == 0 and tmpfsped == 0:
			speed += 5
			tmpfsped += 1
		if score%7 == 0:
			tmpfsped = 0

	
	keyinput = pygame.key.get_pressed()
	
	#getting inputs to move player
	if keyinput[pygame.K_LEFT] or keyinput[pygame.K_a]:
		player.centerx -= 10
	elif keyinput[pygame.K_RIGHT] or keyinput[pygame.K_d]:
		player.centerx += 10
	elif keyinput[pygame.K_UP] or keyinput[pygame.K_w]:
		player.centery -= 10
	elif keyinput[pygame.K_DOWN] or keyinput[pygame.K_s]:
		player.centery += 10
	
	elif keyinput[pygame.K_ESCAPE]:
		pygame.quit()
		sys.exit()
	
	elif keyinput[pygame.K_p]:
		while True:
			pygame.draw.rect(DISPLAYSURF,YELLOW,(200,100,700,300))
			pygame.draw.rect(DISPLAYSURF,BLACK,(200,100,700,300),5)
			
			pauseSurfaceObj = fontObj.render("Game Paused", True, WHITE, BLACK)
			pauseRectObj = pauseSurfaceObj.get_rect()
			pauseRectObj.center = (550, 130)
			DISPLAYSURF.blit(pauseSurfaceObj, pauseRectObj)

			text2SurfaceObj = fontObj.render("Press R to Resume", True, WHITE, BLACK)
			text2RectObj = text2SurfaceObj.get_rect()
			text2RectObj.center = (380, 270)
			DISPLAYSURF.blit(text2SurfaceObj, text2RectObj)

			text3SurfaceObj = fontObj.render("Your Score:- %d" % score, True, WHITE, BLACK)
			text3RectObj = text3SurfaceObj.get_rect()
			text3RectObj.center = (340, 350)
			DISPLAYSURF.blit(text3SurfaceObj, text3RectObj)

			pausekeyinput = pygame.key.get_pressed()
			
			if pausekeyinput[pygame.K_r]:
				break
			elif pausekeyinput[pygame.K_ESCAPE]:
				pygame.quit()
				sys.exit()
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
			pygame.display.update()
	if score%5 == 0 and tmp == 0 and score > 4:
		vaccines.pop()
		for i in range(1):
			vaccines.append(vaccine.get_rect())
			vaccines[i].centerx = random.randint(35,1000)
			vaccines[i].centery = random.randint(50,400)
		tmp = 1
	if score%7 == 0 and tmp == 1:
		tmp = 0
	#detecting contact and removing contacted boy and new in his place and increasing score
	j = 0
	for item in boys[:]:
		if player.colliderect(item):
			soundObj = pygame.mixer.Sound('beep.wav')
			soundObj.play()
			boys[j] = boy.get_rect()
			boys[j].centerx = random.randint(35,1000)
			boys[j].centery = random.randint(50,400)
			score += 1
			speed += 1
		j += 1
	#detectin collision with vaccine
	for item in vaccines[:]:
		if player.colliderect(item) and score%5 != 0:
			while True:
				soundObj = pygame.mixer.Sound('gameoversound.wav')
				soundObj.play()
				pygame.draw.rect(DISPLAYSURF,RED,(200,100,700,300))
				pygame.draw.rect(DISPLAYSURF,BLACK,(200,100,700,300),5)

				quit1SurfaceObj = fontObj.render("You Lose", True, WHITE, BLACK)
				quit1RectObj = quit1SurfaceObj.get_rect()
				quit1RectObj.center = (550, 130)
				DISPLAYSURF.blit(quit1SurfaceObj, quit1RectObj)

				quit2SurfaceObj = fontObj.render("Your Score:- %d" % score, True, WHITE, BLACK)
				quit2RectObj = quit2SurfaceObj.get_rect()
				quit2RectObj.center = (350, 270)
				DISPLAYSURF.blit(quit2SurfaceObj, quit2RectObj)

				quit3SurfaceObj = fontObj.render("Press Q or esc to Quit", True, WHITE, BLACK)
				quit3RectObj = quit3SurfaceObj.get_rect()
				quit3RectObj.center = (400, 370)
				DISPLAYSURF.blit(quit3SurfaceObj, quit3RectObj)

				quitkeyinput = pygame.key.get_pressed()
				if quitkeyinput[pygame.K_ESCAPE] or quitkeyinput[pygame.K_q]:
					pygame.quit()
					sys.exit()

				for event in pygame.event.get():
					if event.type == QUIT:
						pygame.quit()
						sys.exit()
				pygame.display.update()

	#displaying all boys
	for i in range(len(boys)):
		DISPLAYSURF.blit(boy, boys[i])
	
	for i in range(len(vaccines)):
		DISPLAYSURF.blit(vaccine, vaccines[i])
	#displaying player
	DISPLAYSURF.blit(corona, player)
	
	btextSurfaceObj = fontObj.render("Use arrow keys or ASWD to move esc to Quite and P to Pause", True, WHITE, BLACK)
	btextRectObj = btextSurfaceObj.get_rect()
	btextRectObj.center = (600, 550)
	
	DISPLAYSURF.blit(btextSurfaceObj, btextRectObj)
	
	#close event
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
del tmpfsped
del tmp
del speed
del score
#fully patched speed and score 0 game over and will not die while vaccine changes its position