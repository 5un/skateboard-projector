import pygame
from sprites.Arrow import *

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height), pygame.FULLSCREEN)
pygame.display.set_caption('A bit Racey')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False

x = (display_width * 0)
y = (display_height * 0)

myArrow = Arrow(800, 600, speed=20)
myArrow.direction = 'right'

while not crashed:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      crashed = True
    elif event.type == pygame.KEYDOWN:
      # Close on escape button
      if event.key == pygame.key.K_ESCAPE:
        pygame.quit()

  gameDisplay.fill(white)
  myArrow.draw(gameDisplay)  

  pygame.display.update()

  clock.tick(60)
  myArrow.tick()

pygame.quit()
quit()