import pygame
import random
import sys

WHITE = (255,255,255)
SCREEN_WIDTH, SCREEN_HEIGHT = 800,600
BALL_SIZE = 30
STAR_SIZE = 25
score=0

class Ball:
    def __init__(self):
        self.x = random.randrange(BALL_SIZE, SCREEN_WIDTH - BALL_SIZE)
        self.y = random.randrange(BALL_SIZE, SCREEN_HEIGHT - BALL_SIZE)

        self.change_x=0
        while self.change_x == 0 or self.change_y == 0:
            self.change_x = random.randint(-4, 4)
            self.change_y = random.randint(-4, 4)
        
        r = random.randint(1,255)
        g = random.randint(1,255)
        b = random.randint(1,255)
        self.color=(r,g,b)

class Star:
     def __init__(self):
        self.x = random.randrange(STAR_SIZE, SCREEN_WIDTH - STAR_SIZE)
        self.y = random.randrange(STAR_SIZE, SCREEN_HEIGHT - STAR_SIZE)

starimg=pygame.image.load("star.png")
ruleimg=pygame.image.load("rule.png")

pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
pygame.display.set_caption("공 피하기 게임")
clock = pygame.time.Clock()
sysfont = pygame.font.Font(None, 50)

pos_x = 370
pos_y = 220
pos=pygame.image.load("pos.png")
posrect=pos.get_rect()

e=0
firstballs = []
firstballs.append(Ball())

stars = []
stars.append(Star())

i=0
while i < 6:
    firstballs.append(Ball())
    i += 1

done=False
while not done:

    screen.fill(WHITE)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                firstballs.append(Ball())
                score += 10
                
    key_event = pygame.key.get_pressed()
    if key_event[pygame.K_LEFT]:
        pos_x -= 3
    if key_event[pygame.K_RIGHT]:
        pos_x += 3
    if key_event[pygame.K_UP]:
        pos_y -= 3
    if key_event[pygame.K_DOWN]:
        pos_y += 3
        
    if pos_x > SCREEN_WIDTH - 80:
        pos_x = pos_x-3
    if pos_x < 0:
        pos_x = pos_x+3
    if pos_y > SCREEN_HEIGHT - 120:
        pos_y = pos_y-3
    if pos_y <=0:
        pos_y = pos_y+3
             
    for ball in firstballs:
        ball.x += ball.change_x
        ball.y += ball.change_y

        if ball.x > SCREEN_WIDTH - BALL_SIZE or ball.x < BALL_SIZE:
            ball.change_x *= -1
        if ball.y > SCREEN_HEIGHT - BALL_SIZE or ball.y < BALL_SIZE:
            ball.change_y *= -1

    for ball in firstballs:
        pygame.draw.circle(screen,ball.color,[ball.x,ball.y],BALL_SIZE)

    for e in firstballs:
        if pos_x < e.x < pos_x + 83:
            if pos_y < e.y < pos_y + 125:
                score -= 1
                   
    msg1=sysfont.render('Timer',True,(0,0,0))
    screen.blit(msg1,(10,10))

    time=(pygame.time.get_ticks())/1000
    timer=sysfont.render(str(int(32-time)),True,(255,0,0))
    screen.blit(timer,(120,10))

    for star in stars:
        screen.blit(starimg,(star.x,star.y))
          
    for e in stars:
        if pos_x < e.x+5 < pos_x + 83:
            if pos_y < e.y+5 < pos_y + 125:
                score += 20
                stars.append(Star())
                del stars[0]   
      
    msg2=sysfont.render('Score',True,(0,0,0))
    screen.blit(msg2,(10,50))

    scorerect=sysfont.render(str(int(score)),True,(0,0,255))
    screen.blit(scorerect,(120,50))

    msg3=pygame.font.Font(None, 23).render('Game Rule',True,(0,127,0))
    screen.blit(msg3,(710,10))

    if pos_x < 750 < pos_x + 83:
        if pos_y < 10 < pos_y + 125:
            screen.blit(ruleimg,(600,0))

    if time > 32:
        msg=pygame.font.Font(None, 160).render('Game Over!',True,(255,0,0))
        screen.blit(msg,(82,200))
        msg2=sysfont.render('Score',True,(0,0,0))
        screen.blit(msg2,(340,330))
        scorerect=sysfont.render(str(int(score)),True,(0,0,255))
        screen.blit(scorerect,(450,330))
        done=True

    screen.blit(pos,(pos_x, pos_y))
    pygame.display.update()

    clock.tick(60)
    pygame.display.flip()

#pygame.quit()

