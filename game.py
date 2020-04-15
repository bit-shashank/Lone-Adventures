import pygame
import random
from settings import *
from player import Player
 

x=10
y=10

pygame.init()
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)
clock=pygame.time.Clock()


player=Player(200,200)
player.loadAsset(pygame)


done=False
dx=0
dy=0
while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True   
    
    
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        dx=-1

    if keys[pygame.K_RIGHT]:
        dx=1

    if keys[pygame.K_UP]:
        dy=-1
    
    if keys[pygame.K_DOWN]:
        dy=1

    screen.fill((0,0,0))
    pygame.draw.rect(screen,(0,255,100),pygame.Rect(x,y,50,50))
    player.update(dx,dy)
    player.draw(screen)
    pygame.display.flip()

    dx=dy=0