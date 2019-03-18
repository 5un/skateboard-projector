import time
import pygame
from BLEHelper import *
from SensorHelper import *
from sprites.Arrow import *
from sprites.Cat import *
from sprites.Face import *
from sprites.FrameAnimation import *
from sprites.ImageSwitcher import *

"""Global Params"""
useSensor = True
useBle = True

"""Defines the state of the app"""
class AppState():
  def __init__(self):
    self.displayMode = 'sleep' 
      # displayModes: sleep, sad, happy, navigation_start, navigation_eta
      #                 navigation_left, navigation_right, navigation_forward, navigation_backward,
      #                 lol, heart
    self.direction = 'left'
    self.acceleration = (0.0, 0.0, 0.0)
    self.pressure = (0.0, 0.0)
    self.isUserOnBoard = False

"""Initialize the app"""
appState = AppState()
previousDisplayMode = 'sleep'
timeStateUnchanged = 0

"""Initialize connection with arduino"""
if useSensor:
  sensorHelper = SensorHelper(appState)

"""Initialize BLE"""
if useBle:
  bleHelper = BLEHelper(appState)

"""Initialize Pygame"""
pygame.init()
display_width = 640
display_height = 480

gameDisplay = pygame.display.set_mode((display_width,display_height), pygame.FULLSCREEN)
pygame.display.set_caption('Moving On')

arrow = Arrow(display_width, display_height, speed=20)
arrow.direction = 'right'

cat = Cat(display_width,display_height, speed=20)
cat.direction = 'left'

face = Face(display_width, display_height, gameDisplay, speed=20)

navigationStartFrames = ['assets/map-zoom0.png',
  'assets/map-zoom1.png',
  'assets/map-zoom2.png',
  'assets/map-zoom3.png',
  'assets/map-zoom4.png']
navigationStart = FrameAnimation(display_width, display_height, frames=navigationStartFrames)

navigationEtaFrames = ['assets/text-display-15.png',
  'assets/text-display-mins.png',
  'assets/text-display-eta.png']
navigationEta = FrameAnimation(display_width, display_height, frames=navigationEtaFrames)

imageSwitcher = ImageSwitcher(display_width, display_height)

# Sound
beepEffect = pygame.mixer.Sound('assets/beep-05.wav')
navigationStartSpeech = pygame.mixer.Sound('audio/map_state.wav')
sadFaceSpeech1 = pygame.mixer.Sound('audio/sad_face_state.wav')
sadFaceSpeech2 = pygame.mixer.Sound('audio/sad_face_state_2.wav')
navigationDirectionSpeech = pygame.mixer.Sound('audio/navigation_state.wav')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
timeElapsed = 0
crashed = False

x = (display_width * 0)
y = (display_height * 0)

# Main loop
while not crashed:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      crashed = True
    elif event.type == pygame.KEYDOWN:
      # Close on escape button
      if event.key == pygame.K_ESCAPE:
        pygame.quit()

  gameDisplay.fill(white)

  # Display
  if appState.displayMode == 'sleep':
    cat.draw(gameDisplay)
    cat.tick()

  if appState.displayMode in ['sad', 'happy']:
    if appState.displayMode == 'sad':
      face.sad(gameDisplay)
    elif appState.displayMode == 'happy':
      face.happy(gameDisplay)
    gameDisplay.blit(face.currentFace, (0, 0))

  if appState.displayMode == 'navigation_start':
    navigationStart.draw(gameDisplay)
    navigationStart.tick(clock.get_time())

  if appState.displayMode == 'navigation_eta':
    navigationEta.draw(gameDisplay)
    navigationEta.tick(clock.get_time())

  if appState.displayMode in ['navigation_left', 'navigation_right', 'navigation_forward', 'navigation_backward']:
    direction = appState.displayMode.split('_')[1]
    arrow.draw(gameDisplay, direction)
    arrow.tick(direction)

  if appState.displayMode in ['lol', 'eye', 'heart']:
    imageSwitcher.draw(gameDisplay, appState.displayMode)

  # Sound
  if appState.displayMode != previousDisplayMode:
    if appState.displayMode == 'sad':
      sadFaceSpeech2.play()
    if appState.displayMode == 'navigation_start':
      navigationStartSpeech.play()
    if appState.displayMode == 'navigation_right':
      navigationDirectionSpeech.play()
    if appState.displayMode == 'navigation_backward':
      beepEffect.play()
    timeStateUnchanged = 0
  else:
    timeStateUnchanged += clock.get_time()
    if appState.displayMode == 'sad':
      if timeStateUnchanged > 3000:
        sadFaceSpeech1.play()
        timeStateUnchanged = 0

  previousDisplayMode = appState.displayMode

  # Time
  pygame.display.update()
  clock.tick(60)

  # Sensors
  if timeElapsed < 500: 
    timeElapsed = timeElapsed + 30
  else:
    if useSensor:
     sensorHelper.tick(0.5)
    timeElapsed = 0
  

pygame.quit()
if useBle:
  bleHelper.stop()
quit()

