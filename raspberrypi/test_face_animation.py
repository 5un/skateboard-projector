import pygame
from sprites.Face import *

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height), pygame.FULLSCREEN)

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
# crashed = False

x = (display_width * 0)
y = (display_height * 0)

myFace = Face(800, 600, gameDisplay, speed=20)

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      quit()  
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        myFace.happy(gameDisplay);
      if event.key == pygame.K_RIGHT:
        myFace.sad(gameDisplay);
      if event.key == pygame.K_SPACE:
        pygame.quit()

  gameDisplay.fill(white)
  gameDisplay.blit(myFace.currentFace, (0, 0))
  pygame.display.update()

  clock.tick(60)

