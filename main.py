import pygame as pg 
from pygame.locals import *
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(

#send to frame buffer
os.environ["SDL_FBDEV"] = "/dev/fb1"
#to be activated later
#import pibrella as pib

#Setup class for pibrella pinout

class Pibrella: 
   
      
   PB_PIN_LIGHT_AMBER = 17
   PB_PIN_LIGHT_GREEN = 4
# Inputs
   PB_PIN_INPUT_A = 9
   PB_PIN_INPUT_B = 7
   PB_PIN_INPUT_C = 8
   PB_PIN_INPUT_D = 10
# Outputs
   PB_PIN_OUTPUT_A = 22
   PB_PIN_OUTPUT_B = 23
   PB_PIN_OUTPUT_C = 24
   PB_PIN_OUTPUT_D = 25
# Onboard button
   PB_PIN_BUTTON = 11
# Onboard buzzer
   PB_PIN_BUZZER = 18
   
   
   def __init__(self):
      self.ledRed = PB_PIN_LIGHT_RED
      self.ledAmber = PB_PIN_LIGHT_AMBER
      self.ledGreen = PB_PIN_LIGHT_GREEN
      GPIO.setup(ledRed,GPIO.OUT)
      GPIO.setup(ledAmber,GPIO.OUT)
      GPIO.setup(ledGreen,GPIO.OUT)
      
   def light(self, colour, toggle):
      GPIO.output(colour,toggle)
      
      
   

class Settings:
   #Golbal Window Settings
   version = 0.1
   winx = 0
   winy = 0
   displayFlags = pg.FULLSCREEN
   refreshFPS = 50
   winRes = (winx ,winy)
   title = 'Pibrella GUI   ' + str(version)
   #Logo Settings
   logoImg = 'pibrella-logo.png'
   logoSize = (200,85)
   logoPos = (10,0)
   #Led Possitions
   redPos = (112,100)
   greenPos = (112,210)
   amberPos = (112,155)
   ledtouchsize = 20
   #buzzer position
   buzzPos = (180 ,155)
   buzztouchsize = 20
   


#Setting Colour for pygame
class Colour:
   white = pg.Color(255,255,255)
   black = pg.Color(0,0,0)
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
  # pibleds = pib.light
  # greenon = pibleds.green.on()
  # greenoff = pibleds.green.off()
   def ledControl(self, color , location):
      pg.draw.circle(mainWin,color,location,20,0)
   
   
class PibImg:
   pibImg = 'pibrella-pcb.png'
   pibX = 230
   pibY = 300
   pibSize = (pibX , pibY)
   pibPos = (0,30)

#Pibrella Instance

pib = Pibrella()
   
#Setting up window
mainWin = pg.display.set_mode(Settings.winRes,Settings.displayFlags)
pg.display.set_caption(Settings.title)

#Simplifiy fuction 
showSprite = mainWin.blit

#Create instance for led control
leds = Leds()

#Start pyGame
pg.init()

#Start Frame clock
fpsClock= pg.time.Clock()

#Setup Font
pibFont = pg.font.SysFont("monospace", 15)
infotxt = pibFont.render(('Pibrella GUI version: ' + str(Settings.version)+ '  ' + str(fpsClock)),1,(0,0,0))

#Setting up Background sprites
logo = pg.image.load(Settings.logoImg)
logo = pg.transform.scale(logo, Settings.logoSize)
board = pg.image.load(PibImg.pibImg)
board = pg.transform.scale(board, PibImg.pibSize)



def checkMouse(cordsx, cordsy):
   if(((Settings.redPos[0] - Settings.ledtouchsize) < cordsx <(Settings.redPos[0] + Settings.ledtouchsize)) and (Settings.redPos[1] - Settings.ledtouchsize) < cordsy <(Settings.redPos[1] + Settings.ledtouchsize)):
      leds.redStat = not leds.redStat
      #change Pibrella Leds
      pib.light(pib.ledRed,leds.redStat)
   if(((Settings.greenPos[0] - Settings.ledtouchsize) < cordsx <(Settings.greenPos[0] + Settings.ledtouchsize)) and (Settings.greenPos[1] - Settings.ledtouchsize) < cordsy <(Settings.greenPos[1] + Settings.ledtouchsize)):
      leds.greenStat = not leds.greenStat

   if(((Settings.amberPos[0] - Settings.ledtouchsize) < cordsx <(Settings.amberPos[0] + Settings.ledtouchsize)) and (Settings.amberPos[1] - Settings.ledtouchsize) < cordsy <(Settings.amberPos[1] + Settings.ledtouchsize)):
      leds.amberStat = not leds.amberStat

   if(((Settings.buzzPos[0] - Settings.buzztouchsize) < cordsx <(Settings.buzzPos[0] + Settings.buzztouchsize)) and (Settings.buzzPos[1] - Settings.buzztouchsize) < cordsy <(Settings.buzzPos[1] + Settings.buzztouchsize)):
      print('BUZZZZZZ!') 
      #leds.ledsSprite()
      #print('click')
      return
     


    
while 1:
   #fps display
   infotxt = pibFont.render(('Pibrella GUI version: ' + str(Settings.version)+ '  ' + str(fpsClock)),1,(0,0,0))

#Filling Window with background Stuff
   mainWin.fill(Colour.white)
   showSprite(board, PibImg.pibPos)
   showSprite(logo,Settings.logoPos)
   showSprite(infotxt,(0,360))

#Led control
   if(leds.redStat == 0):
      leds.ledControl(Colour.redoff,Settings.redPos)
   else:
      leds.ledControl(Colour.redon,Settings.redPos)
   if(leds.greenStat == 0):
      leds.ledControl(Colour.greenoff,Settings.greenPos)
   else:
      leds.ledControl(Colour.greenon,Settings.greenPos)
   if(leds.amberStat == 0):
      leds.ledControl(Colour.amberoff,Settings.amberPos)
   else:
      leds.ledControl(Colour.amberon,Settings.amberPos)

      
   
   #leds.ledsSprite()
   #pg.draw.circle(mainWin, Colour.greenoff, (162,230), 20, 0)
#Update Page
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
   

