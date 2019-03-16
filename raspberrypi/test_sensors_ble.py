import time
from BLEHelper import *
from SensorHelper import *

"""Defines the state of the app"""
class AppState():
  def __init__(self):
    self.direction = 'left'
    self.acceleration = (0.0, 0.0, 0.0)
    self.pressure = (0.0, 0.0)
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

while True:
  print(appState.acceleration, appState.pressure)
  sensorHelper.tick(0.5)
  sleep(0.5)

bleHelper.stop()
quit()

