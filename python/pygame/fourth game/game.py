#completed 26/04/2020 2 days ttl 8 hrs
#feature:- missile damage varies
#			health bar and coin from astroid
#last changes 26/04/2020
#blast and collision sounds
import pygame , sys
import random
from pygame.locals import *

pygame.init()

fps = 20

fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((1000,500))

pygame.display.set_caption("Space Explorer")

#pygame.mixer.music.load("ignite.mp3")
#pygame.mixer.music.play(-1, 0.0)

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
AQUA = (0,255,255)
WGREY = (200,200,200)
BGREY = (25,25,25)
GREEN2 = (0,245,0)
GREEN3 = (0,235,0)
GREEN4 = (0,225,0)
GREEN5 = (0,215,0)
GREEN6 = (0,205,0)
GREEN7 = (0,195,0)
GREEN8 = (0,185,0)
GREEN9 = (0,175,0)
GREEN10 = (0,165,0)


DISPLAYSURF.fill(BGREY)
#for points of stars
x = 5
starlist = []
for i in range(40):
	starRpoint = []
	if i%2 == 0:
		y = 5
		for j in range(12):
			starRpoint.append(x)
			starRpoint.append(y)
			y += 50
			starlist.append(starRpoint)
	else:
		y = 30
		for j in range(10):
			starRpoint.append(x)
			starRpoint.append(y)
			y += 50
			starlist.append(starRpoint)
	x += 25
astronaut = pygame.image.load("astronaut.png")
rocket = pygame.image.load("rocket.png")
asteroid1 = pygame.image.load("asteroid1.png")
asteroid2 = pygame.image.load("asteroid2.png")
asteroid3 = pygame.image.load("asteroid3.png")
missile = pygame.image.load("missile.png")
blast = pygame.image.load("blast.png")
coin = pygame.image.load("coin.png")

coinobj = coin.get_rect()

helper = astronaut.get_rect()
helper.centerx = 200
helper.centery = 200

player = rocket.get_rect()
player.centerx = 100
player.centery = 250

obstacle1 = asteroid1.get_rect()
obstacle1.centerx = 900
obstacle1.centery = 180

obstacle2 = asteroid2.get_rect()
obstacle2.centerx = 900
obstacle2.centery = 80

obstacle3 = asteroid3.get_rect()
obstacle3.centerx = 900
obstacle3.centery = 390

obstacle4 = asteroid1.get_rect()
obstacle4.centerx = 800
obstacle4.centery = 300

obstacle5 = asteroid1.get_rect()
obstacle5.centerx = 700
obstacle5.centery = 90

bullet = missile.get_rect()
bullet.centerx = 200
bullet.centery = 250

blasted = blast.get_rect()

score = 0
attack = False
bframe = 0
obst1shw = True
obst2shw = True
obst3shw = True
obst4shw = True
obst5shw = True
health = 10
speed = 5
start = True
coinavlbl = False
font1Obj = pygame.font.Font("freesansbold.ttf",28)
while True:
	fpsClock.tick(fps)
	while start:
		DISPLAYSURF.blit(astronaut,helper)
		start1SurfaceObj = font1Obj.render("Welcome", True, WHITE, BGREY)
		start1RectObj = start1SurfaceObj.get_rect()
		start1RectObj.center = (450, 80)
		DISPLAYSURF.blit(start1SurfaceObj, start1RectObj)

		start2SurfaceObj = font1Obj.render("use arrow keys to move and P to pause", True, WHITE, BGREY)
		start2RectObj = start2SurfaceObj.get_rect()
		start2RectObj.center = (580, 130)
		DISPLAYSURF.blit(start2SurfaceObj, start2RectObj)
		
		start3SurfaceObj = font1Obj.render("use space key to launch a missile", True, WHITE, BGREY)
		start3RectObj = start3SurfaceObj.get_rect()
		start3RectObj.center = (545, 170)
		DISPLAYSURF.blit(start3SurfaceObj, start3RectObj)

		start4SurfaceObj = font1Obj.render("One missile at a time can destroy", True, WHITE, BGREY)
		start4RectObj = start4SurfaceObj.get_rect()
		start4RectObj.center = (545, 210)
		DISPLAYSURF.blit(start4SurfaceObj, start4RectObj)

		pygame.draw.rect(DISPLAYSURF,RED,(310,230,535,130))
		pygame.draw.rect(DISPLAYSURF,BLACK,(310,230,535,130),5)

		start5SurfaceObj = font1Obj.render("Small asteroid with 100% accuracy", True, BLACK, RED)
		start5RectObj = start5SurfaceObj.get_rect()
		start5RectObj.center = (570, 250)
		DISPLAYSURF.blit(start5SurfaceObj, start5RectObj)

		start6SurfaceObj = font1Obj.render("Medium asteroid with 80% accuracy", True, BLACK, RED)
		start6RectObj = start6SurfaceObj.get_rect()
		start6RectObj.center = (570, 290)
		DISPLAYSURF.blit(start6SurfaceObj, start6RectObj)
		
		start7SurfaceObj = font1Obj.render("Large asteroid with 60% accuracy", True, BLACK, RED)
		start7RectObj = start7SurfaceObj.get_rect()
		start7RectObj.center = (570, 330)
		DISPLAYSURF.blit(start7SurfaceObj, start7RectObj)

		start8SurfaceObj = font1Obj.render("Press Spacebar to start", True, WHITE, BGREY)
		start8RectObj = start8SurfaceObj.get_rect()
		start8RectObj.center = (540, 390)
		DISPLAYSURF.blit(start8SurfaceObj, start8RectObj)

		startkeyinput = pygame.key.get_pressed()
		if startkeyinput[pygame.K_SPACE]:
			del helper
			start = False
		#close event
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		pygame.display.update()
	DISPLAYSURF.fill(BGREY)
	#to move astroids
	obstacle1.centerx -= speed
	obstacle1.centery = random.randint(obstacle1.centery-3,obstacle1.centery+3)
	obstacle2.centerx -= speed
	obstacle2.centery = random.randint(obstacle2.centery-3,obstacle2.centery+3)
	obstacle3.centerx -= speed
	obstacle3.centery = random.randint(obstacle3.centery-3,obstacle3.centery+3)
	obstacle4.centerx -= speed
	obstacle4.centery = random.randint(obstacle4.centery-3,obstacle4.centery+3)
	obstacle5.centerx -= speed
	obstacle5.centery = random.randint(obstacle5.centery-3,obstacle5.centery+3)
	#to increase speed
	if score >= 50:
		speed = 8
	if score >= 150:
		speed = 10
	#to keep missile in rocket
	if not(attack):
		bullet.centerx = player.centerx + 30
		bullet.centery = player.centery + 30
	#to display stars
	for item in starlist:
		i = 0
		while i < len(item)-1:
			pygame.draw.circle(DISPLAYSURF, WHITE, (item[i],item[i+1]),1)
			i += 2
	
	scoreboardSurfaceObj = font1Obj.render("Score:- %d" % score, True, WGREY, BGREY)
	scoreboardRectObj = scoreboardSurfaceObj.get_rect()
	scoreboardRectObj.center = (890, 30)
	DISPLAYSURF.blit(scoreboardSurfaceObj, scoreboardRectObj)

	keyinput = pygame.key.get_pressed()
	#to move player
	if keyinput[pygame.K_p]:
		while True:
			pygame.draw.rect(DISPLAYSURF,RED,(150,100,700,300))
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
					pygame.quit()
					sys.exit()
			pygame.display.update()
	elif keyinput[pygame.K_UP] or keyinput[pygame.K_w]:
		if player.centery > 50:
			player.centery -= 10
	elif keyinput[pygame.K_DOWN] or keyinput[pygame.K_s]:
		if player.centery < 450:
			player.centery += 10
	elif keyinput[pygame.K_RIGHT] or keyinput[pygame.K_d]:
		if player.centerx < 700:
			player.centerx += 10
	elif keyinput[pygame.K_LEFT] or keyinput[pygame.K_a]:
		if player.centerx > 60:
			player.centerx -= 10
	elif keyinput[pygame.K_ESCAPE]:
		pygame.quit()
		sys.exit()
	elif keyinput[pygame.K_SPACE]:
		attack = True
		soundObj = pygame.mixer.Sound('missilelaunch.wav')
		soundObj.play()
	#to show blast for 5 frame
	if bframe != 0:
		DISPLAYSURF.blit(blast,blasted)
		bframe -= 1
	#to show astroids again after blast is over
	if bframe == 0:
		obst1shw = True
		obst2shw = True
		obst3shw = True
		obst4shw = True
		obst5shw = True
	#to move missile
	if attack:
		blastprob = random.randint(0,5)
		bullet.centerx += 30
		if bullet.colliderect(obstacle1):
			soundObj = pygame.mixer.Sound('blast.wav')
			soundObj.play()
			blasted.centerx = obstacle1.centerx
			blasted.centery = obstacle1.centery
			if not(coinavlbl):
				coinobj.centerx = obstacle1.centerx
				coinobj.centery = obstacle1.centery
				coinavlbl = True
			bullet.centerx = player.centerx
			bullet.centery = player.centery
			obstacle1.centerx = random.randint(800,950)
			obstacle1.centery = random.randint(100,450)
			obst1shw = False
			bframe = 3
			score += 1
			attack = False
		elif bullet.colliderect(obstacle2):
			blasted.centerx = obstacle2.centerx
			blasted.centery = obstacle2.centery
			if blastprob != 3:
				soundObj = pygame.mixer.Sound('blast.wav')
				soundObj.play()
				bullet.centerx = player.centerx
				bullet.centery = player.centery
				obstacle2.centerx = random.randint(800,950)
				obstacle2.centery = random.randint(100,450)
				obst2shw = False
				bframe = 3
				score += 2
			attack = False
		elif bullet.colliderect(obstacle3):
			blasted.centerx = obstacle3.centerx
			blasted.centery = obstacle3.centery
			if blastprob != 3 and blastprob != 2:
				soundObj = pygame.mixer.Sound('blast.wav')
				soundObj.play()
				bullet.centerx = player.centerx
				bullet.centery = player.centery
				obstacle3.centerx = random.randint(800,950)
				obstacle3.centery = random.randint(100,450)
				obst3shw = False
				bframe = 3
				score += 3
			attack = False
		elif bullet.colliderect(obstacle4):
			soundObj = pygame.mixer.Sound('blast.wav')
			soundObj.play()
			blasted.centerx = obstacle4.centerx
			blasted.centery = obstacle4.centery
			bullet.centerx = player.centerx
			bullet.centery = player.centery
			obstacle4.centerx = random.randint(800,950)
			obstacle4.centery = random.randint(100,450)
			obst4shw = False
			bframe = 3
			score += 1
			attack = False
		elif bullet.colliderect(obstacle5):
			soundObj = pygame.mixer.Sound('blast.wav')
			soundObj.play()
			blasted.centerx = obstacle5.centerx
			blasted.centery = obstacle5.centery
			bullet.centerx = player.centerx
			bullet.centery = player.centery
			obstacle5.centerx = random.randint(800,950)
			obstacle5.centery = random.randint(100,450)
			obst5shw = False
			bframe = 3
			score += 1
			attack = False
		if bullet.centerx >= 975:
			attack = False
	#to reduce health
	if player.colliderect(obstacle1):
		health -= 1
		obstacle1.centerx = random.randint(700,950)
	if player.colliderect(obstacle2):
		health -= 1
		obstacle2.centerx = random.randint(700,950)
	if player.colliderect(obstacle3):
		health -= 2
		obstacle3.centerx = random.randint(700,950)
	if player.colliderect(obstacle4):
		health -= 1
		obstacle4.centerx = random.randint(700,950)
	if player.colliderect(obstacle5):
		health -= 1
		obstacle5.centerx = random.randint(700,950)
	#you lose box
	if health <= 0:
		soundObj = pygame.mixer.Sound('lose.wav')
		soundObj.play()
		while True:
			pygame.draw.rect(DISPLAYSURF,GREEN,(150,100,700,300))
			pygame.draw.rect(DISPLAYSURF,BLACK,(150,100,700,300),5)
			
			quitSurfaceObj = font1Obj.render("You Lose", True, WHITE, BLACK)
			quitRectObj = quitSurfaceObj.get_rect()
			quitRectObj.center = (500, 130)
			DISPLAYSURF.blit(quitSurfaceObj, quitRectObj)

			quit2SurfaceObj = font1Obj.render("Press Q or esc to Exit", True, WHITE, BLACK)
			quit2RectObj = quit2SurfaceObj.get_rect()
			quit2RectObj.center = (330, 270)
			DISPLAYSURF.blit(quit2SurfaceObj, quit2RectObj)

			quit3SurfaceObj = font1Obj.render("Your Score:- %d" % score, True, WHITE, BLACK)
			quit3RectObj = quit3SurfaceObj.get_rect()
			quit3RectObj.center = (290, 350)
			DISPLAYSURF.blit(quit3SurfaceObj, quit3RectObj)

			quitkeyinput = pygame.key.get_pressed()

			if quitkeyinput[pygame.K_q] or quitkeyinput[pygame.K_ESCAPE]:
				pygame.quit()
				sys.exit()

			#close event
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
			pygame.display.update()
	#to create asteroids again if they by pass frame
	if obstacle1.centerx <= 10:
		obstacle1.centerx = random.randint(700,950)
	if obstacle2.centerx <= 10:
		score += 1
		obstacle2.centerx = random.randint(700,950)
	if obstacle3.centerx <= 10:
		score += 1
		obstacle3.centerx = random.randint(700,950)
	if obstacle4.centerx <= 10:
		obstacle4.centerx = random.randint(700,950)
	if obstacle5.centerx <= 10:
		obstacle5.centerx = random.randint(700,950)
	if player.colliderect(coinobj):
		score += 1
		coinobj.centerx = 990
		coinavlbl = False
	#close event
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	#to display player
	DISPLAYSURF.blit(rocket,player)
	if coinavlbl:
		coinobj.centerx -= 20
		DISPLAYSURF.blit(coin,coinobj)
		if coinobj.centerx <= 10:
			coinavlbl = False
	#health bar
	pygame.draw.rect(DISPLAYSURF,BLACK,(player.centerx-50,player.centery-80,100,30),3)
	if health > 0:
		pygame.draw.rect(DISPLAYSURF,GREEN10,(player.centerx-50,player.centery-80,10,30))
		if health > 1:
			pygame.draw.rect(DISPLAYSURF,GREEN9,(player.centerx-40,player.centery-80,10,30))
			if health > 2:
				pygame.draw.rect(DISPLAYSURF,GREEN8,(player.centerx-30,player.centery-80,10,30))
				if health > 3:
					pygame.draw.rect(DISPLAYSURF,GREEN7,(player.centerx-20,player.centery-80,10,30))
					if health > 4:
						pygame.draw.rect(DISPLAYSURF,GREEN6,(player.centerx-10,player.centery-80,10,30))
						if health > 5:
							pygame.draw.rect(DISPLAYSURF,GREEN5,(player.centerx,player.centery-80,10,30))
							if health > 6:
								pygame.draw.rect(DISPLAYSURF,GREEN4,(player.centerx+10,player.centery-80,10,30))
								if health > 7:
									pygame.draw.rect(DISPLAYSURF,GREEN3,(player.centerx+20,player.centery-80,10,30))
									if health > 8:
										pygame.draw.rect(DISPLAYSURF,GREEN2,(player.centerx+30,player.centery-80,10,30))
										if health > 9:
											pygame.draw.rect(DISPLAYSURF,GREEN,(player.centerx+40,player.centery-80,10,30))
	#to display player
	if obst1shw:
		DISPLAYSURF.blit(asteroid1,obstacle1)
	if obst2shw:
		DISPLAYSURF.blit(asteroid2,obstacle2)
	if obst3shw:
		DISPLAYSURF.blit(asteroid3,obstacle3)
	if obst4shw:
		DISPLAYSURF.blit(asteroid1,obstacle4)
	if obst5shw:
		DISPLAYSURF.blit(asteroid1,obstacle5)
	#to display missile
	if attack:
		DISPLAYSURF.blit(missile,bullet)
	pygame.display.update()
"""#to move stars
	for item in starlist:
		i = 0
		while i < len(item)-1:
			item[i] -= 1
			i += 2"""