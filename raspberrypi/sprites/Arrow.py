import pygame

class Arrow():

  def __init__(self, width, height, speed=5):
    self.width = width
    self.height = height
    self.speed = speed
    self.arrowLeftImg = pygame.image.load('assets/arrow_left.png').convert()
    self.arrowLeftImg = pygame.transform.scale(self.arrowLeftImg, (self.width, self.height))

    self.arrowRightImg = pygame.image.load('assets/arrow_right.png').convert()
    self.arrowRightImg = pygame.transform.scale(self.arrowRightImg, (self.width, self.height))
    self.x = 0
    self.y = 0
    self.direction = 'left'

  def tick(self):
    if self.direction == 'left':
      if self.x > -self.width:
        self.x = self.x - self.speed
      else:
        self.x = self.width
    else:
      if self.x < self.width:
        self.x = self.x + self.speed
      else:
        self.x = -self.width

  def draw(self, gameDisplay):
    if self.direction == 'left':
      gameDisplay.blit(self.arrowLeftImg, (self.x, self.y))
    elif self.direction == 'right':
      gameDisplay.blit(self.arrowRightImg, (self.x, self.y))
