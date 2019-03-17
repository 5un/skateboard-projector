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

"""Initialize the app"""
appState = AppState()

"""Initialize connection with arduino"""
sensorHelper = SensorHelper(appState)

"""Initialize BLE"""
bleHelper = BLEHelper(appState)

while True:
  print('sensors:', appState.acceleration, appState.pressure)
  sensorHelper.tick(0.5)
  time.sleep(0.5)

bleHelper.stop()
quit()

