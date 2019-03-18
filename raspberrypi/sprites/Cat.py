import pygame

class Cat():

  def __init__(self, width, height, speed=5):
    self.width = width
    self.height = height
    self.speed = speed
    self.catImg = pygame.image.load('assets/cat.jpg').convert()
    self.catImg = pygame.transform.scale(self.catImg, (self.width, self.height))
    self.x = 0
    self.y = 0
    self.direction = 'left'

  def tick(self):
    # if self.direction == 'left':
    #   if self.x > -self.width:
    #     self.x = self.x - self.speed
    #   else:
    #     self.x = self.width
    # else:
    #   if self.x < self.width:
    #     self.x = self.x + self.speed
    #   else:
    #     self.x = -self.width
    pass

  def draw(self, gameDisplay):
    if self.direction == 'left':
      gameDisplay.blit(self.catImg, (self.x, self.y))
    elif self.direction == 'right':
      gameDisplay.blit(self.catImg, (self.x, self.y))
