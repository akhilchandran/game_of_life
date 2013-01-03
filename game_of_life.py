#!/usr/bin/python
#import pygame library
import pygame
from pygame.locals import*

b = []
c = []
windo = x,y =1300,700
for i in range(0,x/50+2):
  a = []
  for j in range(0,y/50+2):
    a =a + [0]
  b = b[:] + [a[:]]
  c = c[:] + [a[:]]

pygame.init()
# set up the window
DISPLAYSURF = pygame.display.set_mode(windo)
pygame.display.set_caption('Game Of Life')

# set up the colors
BLACK = ( 0,0,0)
WHITE = (255, 255, 255)
RED= (255,0,0)
GREEN = ( 0, 255,0)
BLUE = ( 0,0, 255)
fpsClock = pygame.time.Clock()
sype = pygame.image.load('/home/akhil/a.png')

# draw on the surface object
DISPLAYSURF.fill(WHITE)
c[5][5]= c[4][5]=c[3][5]=1
c[9][4]= c[10][4]=c[10][5]=c[9][5]=1
c[11][8]=c[11][9]=c[11][7]=c[12][8]=c[12][7]=c[12][9]=c[13][9]=c[13][8]=c[13][7]=1
# run the game loop

while True:
  for i in range(1,x/50+1):
    for j in range(1,y/50+1):
      b[i][j] = c[i][j]
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  
  for i in range(1,x/50+1):
      for j in range(1,y/50+1):
        s = (i-1)*50+1,(j-1)*50+1
        if c[i][j] == 1:
          pygame.draw.rect(DISPLAYSURF, GREEN, (s +(48,48)))
          DISPLAYSURF.blit(sype,s)
        else:
          pygame.draw.rect(DISPLAYSURF, BLACK, (s +(48,48)))
  
  pygame.display.update()
  fpsClock.tick(25)  
  
  for i in range(1,x/50+1):
      for j in range(1,y/50+1):
        a = (b[i-1][j-1]+b[i][j-1]+b[i+1][j-1]+b[i-1][j]+b[i+1][j]+b[i-1][j+1]+b[i][j+1]+b[i+1][j+1])
        if a != 2 and a != 3 and b[i][j] :
          c[i][j] = 0
        if (a == 3) and (b[i][j] == 0):
          c[i][j] = 1
