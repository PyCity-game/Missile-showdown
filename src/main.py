import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.flip()
pygame.display.set_caption('Missile showdown')
icon=pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)

rocket1 = pygame.image.load('images/rocket.png').convert_alpha()
base_red1 = pygame.image.load('images/base_red.png').convert()
base_green1 = pygame.image.load('images/base_green.png').convert()
base_red=pygame.transform.scale(base_red1,(50,50))
base_green=pygame.transform.scale(base_green1,(50,50))
rocket=pygame.transform.scale(rocket1,(50,50))
rocket2 = pygame.transform.rotate(rocket, 180)
bg1 = pygame.image.load("images/bg.png")
bg = pygame.transform.scale(bg1,(500,500))
explosion1=pygame.image.load('images/expolision.png').convert_alpha()
explosion2=pygame.transform.scale(explosion1,(50,50))

red=(255,0,0)
black=(3,168,244)
green=(8, 168, 64)
blue=(0,0,255)
collided=1
a=0
b=0
global c
c=0
health=100
health2=100
times=0
times2=0
w, h = pygame.display.get_surface().get_size()
nx=0
ny=0
x2=240
y2=75
ex=0
ey=0
running = True

pygame.font.init()
myfont = pygame.font.SysFont('Arial', 30)


def explosion(ex,ey):
    rect4=explosion2.get_rect()
    rect4.center=(ex,ey)
    screen.blit(explosion2, rect4)


while running:
    x,y=pygame.mouse.get_pos()
    clock = pygame.time.Clock()
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            running2=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q and x>=(w//2-25) and x<=(w//2-25)+50 and y>=450 and y<=500:
                collided=0
                times=0
                times2=0
            if event.key == pygame.K_e and b==1:
                b=0
                health=100
                health2=100

    if b==0:
        screen.fill(black)
        pygame.draw.rect(screen, green, (0,0, 500, 50))
        pygame.draw.rect(screen, green, (0,450, 500, 50))

        textsurface = myfont.render('HP:'+str(health), False, (255, 255, 255))
        textsurface2 = myfont.render('HP:'+str(health2), False, (255, 255, 255))
        textsurface3 = myfont.render('Red won!', False, (255, 255, 255))
        textsurface4 = myfont.render('Green won!', False, (255, 255, 255))
        textsurface5 = myfont.render('Draw!', False, (255, 255, 255))
        textsurface6 = myfont.render('Press E to continue', False, (255, 255, 255))

        screen.blit(textsurface,(400,10))
        screen.blit(textsurface2,(400,450))

        if collided==0:
            rect=rocket.get_rect()
            rect.center=(x,y)
            direction = pygame.math.Vector2(w//2-25, 0) - rect.center
            angle = direction.angle_to((0, -1))
            image = pygame.transform.rotate(rocket, angle)
            screen.blit(image, rect)#rect=pygame.draw.rect(screen, blue, (x-10,y-10, 20, 20))

        rect2=base_red.get_rect()
        rect2.topleft=(w//2-25,0)
        screen.blit(base_red, rect2)#pygame.draw.rect(screen, red, (w//2-25,0, 50, 50))
        #base=pygame.draw.rect(screen, green, (w//2-25,450, 50, 50))
        base=base_green.get_rect()
        base.topleft=(w//2-25,450)
        screen.blit(base_green, base)

        if y2<=450:
            y2=y2+0.2*dt
            missle=rocket2.get_rect()
            missle.topleft=(x2-25,y2-25)
            screen.blit(rocket2, missle)

        collide = rect2.collidepoint(x,y)
        if collide:
            collided=1
            if health>0 and times==0:
                health=health-10
                times=1
                explosion(rect2.x+25,rect2.y+25)


        if x2>=base.x and x2<=base.x+50 and y2>=base.y and y2<=base.y+50 and times2==0 and health2>0:
            health2=health2-10
            times2=0
            x2=240
            y2=75
            explosion(base.x+25,base.y+25)

        if x>=missle.x and x<=missle.x+25 and y>=missle.y and y<=missle.y+10 and collided==0:
            collided=1
            times2=0
            x2=240
            y2=75
            explosion(x,y)

    if health2==0 and health>health2:
        b=1
        screen.fill(black)
        screen.blit(textsurface3,(w//2-50,h//2))
        screen.blit(textsurface6,(w//2-50,h//2+30))
    elif health==0 and health2>health:
        b=1
        screen.fill(black)
        screen.blit(textsurface4,(w//2-50,h//2))
        screen.blit(textsurface6,(w//2-50,h//2+30))
    elif health==0 and health2==0:
        b=1
        screen.fill(black)
        screen.blit(textsurface5,(w//2-50,h//2))
        screen.blit(textsurface6,(w//2-50,h//2+30))

    pygame.display.update()
