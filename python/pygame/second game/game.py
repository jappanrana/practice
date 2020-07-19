#finished at 24/04/2020 took 2 days working 12 hrs total
#last bug fix and feature changes at 26/04/2020
import random
import pygame , sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((1000,500))

pygame.display.set_caption("Godzilla Runner")

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
AQUA = (0,255,255)
WGREY = (200,200,200)
BGREY = (100,100,100)

speed = 20
FPS = 20
fpsClock = pygame.time.Clock()

DISPLAYSURF.fill(BLACK)

pygame.mixer.music.load("godzilla.mp3")
pygame.mixer.music.play(-1, 0.0)

#for ground points
valuexa = 0
valuexb = 0
ix = 50
ex = 100

points = []
for i in range(19):
	points.append(ix - valuexa)
	ix += 50
pointe = []
for i in range(19):
	pointe.append(ex - valuexb)
	ex += 50
#to draw ground
for i in range(19):
	pygame.draw.aaline(DISPLAYSURF,BLACK,(int(points[i]),305),(int(pointe[i]),295),4)

dino = pygame.image.load("godzilla.png")
tree = pygame.image.load("hurdle.png")
plan = pygame.image.load("airhurdle.png")

player = dino.get_rect()
player.centerx = 300
player.centery = 250

hurdle = tree.get_rect()
hurdle.centerx = 940
hurdle.centery = 280

airhurdle = plan.get_rect()
airhurdle.centerx = 900
airhurdle.centery = 170

isJump = False
jumpCount = 11

font1Obj = pygame.font.Font("freesansbold.ttf", 28)
font2Obj = pygame.font.Font("freesansbold.ttf", 18)

airfSurfaceObj = font2Obj.render("Airforce:- Stand by", True, BLACK, WGREY)
airfRectObj = airfSurfaceObj.get_rect()
airfRectObj.center = (850, 100)
DISPLAYSURF.blit(airfSurfaceObj,airfRectObj)

score = 0
tmpfsped = 0
rand = 0
randair = 0
airforce = False

while True:
	fpsClock.tick(speed)

	pygame.draw.rect(DISPLAYSURF,WGREY,(50,50,900,400))
	
	textSurfaceObj = font1Obj.render("score:- %d" % score, True, BLACK, WGREY)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (140, 80)
	#to increase speed
	if speed < 60 and score > 1:
		if score%5 == 0 and tmpfsped == 0:
			speed += 5
			tmpfsped += 1
		if score%7 == 0:
			tmpfsped = 0
	#to print ground
	for i in range(19):
		pygame.draw.aaline(DISPLAYSURF,BLACK,(int(points[i]),305),(int(pointe[i]),295),4)

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
			text2RectObj.center = (330, 270)
			DISPLAYSURF.blit(text2SurfaceObj, text2RectObj)

			text3SurfaceObj = font1Obj.render("Your Score:- %d" % score, True, WHITE, BLACK)
			text3RectObj = text3SurfaceObj.get_rect()
			text3RectObj.center = (290, 350)
			DISPLAYSURF.blit(text3SurfaceObj, text3RectObj)

			pausekeyinput = pygame.key.get_pressed()

			if pausekeyinput[pygame.K_r]:
				break
			#close event
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.mixer.music.stop()
					pygame.quit()
					sys.exit()
			pygame.display.update()
	elif keyinput[pygame.K_ESCAPE]:
		pygame.mixer.music.stop()
		pygame.quit()
		sys.exit()
	elif keyinput[pygame.K_RIGHT]:
		if player.centerx < 500:
			player.centerx += 5
	elif keyinput[pygame.K_LEFT]:
		if player.centerx > 150:
			player.centerx -= 5
	#to land the jump once any key is pressed
	if not(isJump):
		if keyinput[pygame.K_SPACE] or keyinput[pygame.K_w] or keyinput[pygame.K_UP]:
			isJump = True
	else:
		if jumpCount >= -11:
			player.centery -= (jumpCount * abs(jumpCount)) * 0.25
			jumpCount -= 1
		else:
			jumpCount = 11
			player.centery = 250
			soundObj = pygame.mixer.Sound('beep.wav')
			soundObj.play()
			isJump = False
	#spawns tree when old tree is going out of frame
	hurdle.centerx = hurdle.centerx - 5
	if hurdle.centerx < 70:
		hurdle.centerx = 700 + rand
		rand = random.randint(0,250)
	#to change the airforce status
	if airforce:
		airfSurfaceObj = font2Obj.render("Airforce:- Active", True, BLACK, WGREY)
		airfRectObj = airfSurfaceObj.get_rect()
		airfRectObj.center = (850, 100)
	#to activate airforce
	if airforce == False and score > 150 and hurdle.centerx <= 400:
		airforce = True
	#to spawn...
	if airforce:
		airhurdle.centerx = airhurdle.centerx - 4
		airhurdle.centery = random.randint(airhurdle.centery-3,airhurdle.centery+2)
		if airhurdle.centerx < 70:
			airhurdle.centerx = 800 + randair
			randair = random.randint(0,50)
	#close event
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.mixer.music.stop()
			pygame.quit()
			sys.exit()
	#to add and remove lines
	if points[0] == 5:
		del points[0]
		del pointe[0]
		points.append(950)
		pointe.append(1000)
		score += 1
	#to move ground
	for item in range(len(points)):
		points[item] -= 5 
	for item in range(len(pointe)):
		pointe[item] -= 5
	#quite event
	if player.colliderect(hurdle) or player.colliderect(airhurdle):
		pygame.mixer.music.stop()
		soundObj = pygame.mixer.Sound('gameover.wav')
		soundObj.play()
		while True:
			pygame.draw.rect(DISPLAYSURF,BGREY,(150,100,700,300))
			pygame.draw.rect(DISPLAYSURF,BLACK,(150,100,700,300),5)
			
			quitSurfaceObj = font1Obj.render("You Lose", True, WHITE, BLACK)
			quitRectObj = quitSurfaceObj.get_rect()
			quitRectObj.center = (500, 130)
			DISPLAYSURF.blit(quitSurfaceObj, quitRectObj)

			quit2SurfaceObj = font1Obj.render("Press Q or esc to Exit", True, WHITE, BLACK)
			quit2RectObj = quit2SurfaceObj.get_rect()
			quit2RectObj.center = (340, 270)
			DISPLAYSURF.blit(quit2SurfaceObj, quit2RectObj)

			quit3SurfaceObj = font1Obj.render("Your Score:- %d" % score, True, WHITE, BLACK)
			quit3RectObj = quit3SurfaceObj.get_rect()
			quit3RectObj.center = (290, 350)
			DISPLAYSURF.blit(quit3SurfaceObj, quit3RectObj)

			pausekeyinput = pygame.key.get_pressed()

			if pausekeyinput[pygame.K_q] or pausekeyinput[pygame.K_ESCAPE]:
				pygame.mixer.music.stop()
				pygame.quit()
				sys.exit()
			#close event
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.mixer.music.stop()
					pygame.quit()
					sys.exit()
			pygame.display.update()
	#displaye score
	DISPLAYSURF.blit(textSurfaceObj,textRectObj)
	#display
	DISPLAYSURF.blit(dino,player)
	DISPLAYSURF.blit(tree, hurdle)
	DISPLAYSURF.blit(plan,airhurdle)
	DISPLAYSURF.blit(airfSurfaceObj,airfRectObj)
	pygame.display.update()