import pygame as pg 
from pygame.locals import *
#to be activated later
#import pibrella as pib

class Settings:
   #Golbal Window Settings
   version = 0.1
   winx = 640
   winy = 480
   refreshFPS = 15
   winRes = (winx ,winy)
   title = 'Pibrella GUI   ' + str(version)
   #Logo Settings
   logoImg = 'pibrella-logo.png'
   logoSize = (200,85)
   logoPos = (60,0)

#Setting up window
mainWin = pg.display.set_mode(Settings.winRes)
pg.display.set_caption(Settings.title)

class Colour:
   white = pg.Color(255,255,255)
   redon = pg.Color(255,0,0)
   redoff = pg.Color(50,0,0)
   amberon = pg.Color(255,255,0)
   amberoff = pg.Color(50,50,0)
   greenon = pg.Color(0,255,0)
   greenoff = pg.Color(0,50,0)


#Setup for later
class Leds():
   redStat = 0
   greenStat = 0
   amberStat = 0
   def __init__(self):
      self.redStat = 0
      self.greenStat = 0
      self.amberStat = 0
   #pibleds = pibrella.light
   #greenon = pibleds.green.on()
   #greenoff = pibleds.green.off()
   
   def ledControl(self, color , location):
      pg.draw.circle(mainWin,color,location,20,0)
   
class PibImg:
   pibImg = 'pibrella-pcb.png'
   pibX = 230
   pibY = 300
   pibSize = (pibX , pibY)
   pibPos = (50,50)


   

leds = Leds()
leds.redStat = 0
#trafficleds = Leds()
leds.ledControl(Colour.redoff,(162,120))
pg.init()
fpsClock= pg.time.Clock()
#setting up sprites
logo = pg.image.load(Settings.logoImg)
logo = pg.transform.scale(logo, Settings.logoSize)
board = pg.image.load(PibImg.pibImg)
board = pg.transform.scale(board, PibImg.pibSize)



showSprite = mainWin.blit

def checkMouse(cordsx, cordsy):
   if((140 < cordsx <182) and (100 < cordsy < 140)):
      leds.redStat = not leds.redStat

   if((140 < cordsx <182) and (220 < cordsy < 250)):
      leds.greenStat = not leds.greenStat

   if((140 < cordsx <182) and (160 < cordsy < 180)):
      leds.amberStat = not leds.amberStat
      
      #leds.ledsSprite()
      #print('click')
      return
     
   

    
while 1:

   mainWin.fill(Colour.white)
   
   showSprite(board, PibImg.pibPos)
   showSprite(logo,Settings.logoPos)
#led control
   if(leds.redStat == 0):
      leds.ledControl(Colour.redoff,(162,120))
   else:
      leds.ledControl(Colour.redon,(162,120))
   if(leds.greenStat == 0):
      leds.ledControl(Colour.greenoff,(162,230))
   else:
      leds.ledControl(Colour.greenon,(162,230))
   if(leds.amberStat == 0):
      leds.ledControl(Colour.amberoff,(162,175))
   else:
      leds.ledControl(Colour.amberon,(162,175))

      
   
   #leds.ledsSprite()
   #pg.draw.circle(mainWin, Colour.greenoff, (162,230), 20, 0)
   pg.display.update()
   



#event handler
   for event in pg.event.get():
      if event.type == pg.MOUSEBUTTONUP:
         pos = pg.mouse.get_pos()
         print(pos)
         checkMouse(pos[0],pos[1])
         
      if event.type == QUIT:
         pg.quit()
         quit()
         break

#sets frames per second
   fpsClock.tick(Settings.refreshFPS)
   

