import pygame
from BLEHelper import *

"""Defines the state of the app"""
class AppState():
    def __init__(self):
        self.direction = 'left'

    def setDirection(newDirection):
        self.direction = newDirection

"""Initializes the app"""
appState = AppState()
bleHelper = BLEHelper(appState)
pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height), pygame.FULLSCREEN)
pygame.display.set_caption('Moving On')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False
arrowLeftImg = pygame.image.load('assets/arrow_left.png')
arrowLeftImg = pygame.transform.scale(arrowLeftImg, (800, 600))

arrowRightImg = pygame.image.load('assets/arrow_right.png')
arrowRightImg = pygame.transform.scale(arrowRightImg, (800, 600))

def drawArrow(x,y,direction):
  if direction == 'left':
    gameDisplay.blit(arrowLeftImg, (x,y))
  else:
    gameDisplay.blit(arrowRightImg, (x,y))


x = (display_width * 0)
y = (display_height * 0)

while not crashed:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      crashed = True
    elif event.type == pygame.KEYDOWN:
      # Close on escape button
      if event.key == pygame.key.K_ESCAPE:
        pygame.quit()

  gameDisplay.fill(white)
  drawArrow(0,0,appState.direction)

  pygame.display.update()
  clock.tick(60)

pygame.quit()
bleHelper.stop()
quit()