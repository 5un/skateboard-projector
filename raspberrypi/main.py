import time
import pygame
from BLEHelper import *
from SensorHelper import *

"""Defines the state of the app"""
class AppState():
  def __init__(self):
    self.direction = 'left'
    self.acceleration = (0.0, 0.0, 0.0)
    self.isUserOnBoard = False

  def setDirection(self, newDirection):
    self.direction = newDirection

"""Initialize the app"""
appState = AppState()

"""Initialize connection with arduino"""
sensorHelper = sensorHelper(appState)

"""Initialize BLE"""
bleHelper = BLEHelper(appState)

"""Initialize Pygame"""
pygame.init()
myArrow = Arrow(800, 600, speed=20)
myArrow.direction = 'right'

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height), pygame.FULLSCREEN)
pygame.display.set_caption('Moving On')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
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
  
  myArrow.direction = appState.direction
  myArrow.draw(gameDisplay)  

  pygame.display.update()
  clock.tick(60)
  sensorHelper.tick(0.060)

pygame.quit()
bleHelper.stop()
quit()

