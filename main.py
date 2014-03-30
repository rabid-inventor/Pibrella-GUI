import pygame as pg
from pygame.locals import *

class Settings:
   #Golbal Window Settings
   winx = 640
   winy = 480
   refreshFPS = 15
   winRes = (winx ,winy)
   #Logo Settings
   logoImg = 'pibrella-logo.png'
   logoSize = (150,50)
   logoPos = (50,0)

class PibImg:
   pibImg = 'pibrella-pcb.png'
   pibX = 300
   pibY = 200
   pibSize = (pibX , pibY)
   pibPos = (0,50)



   
pg.init()
fpsClock= pg.time.Clock()
#setting up sprites
logo = pg.image.load(Settings.logoImg)
logo = pg.transform.scale(logo, Settings.logoSize)


mainWin = pg.display.set_mode(Settings.winRes)

pg.display.set_caption('Pygame')
colWhite = pg.Color(255,255,255)

    
while 1:
   mainWin.fill(colWhite)
   mainWin.blit(logo,Settings.logoPos)
   pg.display.update()
   



#event handler
   while True:
      for event in pg.event.get():
         if event.type == QUIT:
            pg.quit()
            quit()
            break

#sets frames per second
   fpsClock.tick(Settings.refreshFPS)
   

