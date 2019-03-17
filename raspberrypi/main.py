import time
import pygame
from BLEHelper import *
from SensorHelper import *
from sprites.Arrow import *
from sprites.Cat import *

"""Defines the state of the app"""
class AppState():
  def __init__(self):
    self.direction = 'left'
    self.acceleration = (0.0, 0.0, 0.0)
    self.pressure = (0.0, 0.0)
    self.isUserOnBoard = False

"""Initialize the app"""
appState = AppState()

"""Initialize connection with arduino"""
sensorHelper = SensorHelper(appState)

"""Initialize BLE"""
bleHelper = BLEHelper(appState)

"""Initialize Pygame"""
pygame.init()
display_width = 640
display_height = 480

gameDisplay = pygame.display.set_mode((display_width,display_height), pygame.FULLSCREEN)
pygame.display.set_caption('Moving On')

myArrow = Arrow(640, 480, speed=20)
myArrow.direction = 'right'

cat = Cat(640,480, speed=20)
cat.direction = 'left'

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
timeElapsed = 0
crashed = False

x = (display_width * 0)
y = (display_height * 0)


while not crashed:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      crashed = True
    elif event.type == pygame.KEYDOWN:
      # Close on escape button
      if event.key == pygame.K_ESCAPE:
        pygame.quit()

  gameDisplay.fill(white)
  
  # myArrow.direction = appState.direction
  # myArrow.draw(gameDisplay)  

  cat.direction = appState.direction
  cat.draw(gameDisplay)

  pygame.display.update()
  clock.tick()
  myArrow.tick()

  if timeElapsed < 500: 
    timeElapsed = timeElapsed + 30
  else:
    sensorHelper.tick(0.5)
    timeElapsed = 0
  

pygame.quit()
bleHelper.stop()
quit()

