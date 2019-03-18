import pygame

class Arrow():

  def __init__(self, width, height, speed=5):
    self.width = width
    self.height = height
    self.speed = speed
    
    self.arrowLeftImg = pygame.image.load('assets/arrow_left_wrap.jpg')
    self.arrowLeftImg = pygame.transform.scale(self.arrowLeftImg, (self.width, self.height))

    self.arrowRightImg = pygame.image.load('assets/arrow_right_wrap.jpg')
    self.arrowRightImg = pygame.transform.scale(self.arrowRightImg, (self.width, self.height))

    self.arrowForwardImg = pygame.image.load('assets/arrow_forward_wrap.jpg')
    self.arrowForwardImg = pygame.transform.scale(self.arrowForwardImg, (self.width, self.height))

    self.arrowBackwardImg = pygame.image.load('assets/arrow_backward_wrap.jpg')
    self.arrowBackwardImg = pygame.transform.scale(self.arrowBackwardImg, (self.width, self.height))

    self.x = 0
    self.y = 0
    self.direction = 'left'

  def tick(self, direction):
    self.direction = direction
    if direction == 'left':
      if self.x > -self.width:
        self.x = self.x - self.speed
      else:
        self.x = self.width
      self.y = 0

    elif direction == 'right':
      if self.x < self.width:
        self.x = self.x + self.speed
      else:
        self.x = -self.width
      self.y = 0

    elif direction == 'forward':
      if self.y > -self.height:
        self.y = self.y - self.speed
      else:
        self.y = self.height
      self.x = 0

    elif direction == 'backward':
      if self.y < self.height:
        self.y = self.y + self.speed
      else:
        self.y = -self.height
      self.x = 0

  def draw(self, gameDisplay, direction):
    if direction == 'left':
      gameDisplay.blit(self.arrowLeftImg, (self.x, self.y))
    elif direction == 'right':
      gameDisplay.blit(self.arrowRightImg, (self.x, self.y))
    elif direction == 'forward':
      gameDisplay.blit(self.arrowForwardImg, (self.x, self.y))
    elif direction == 'backward':
      gameDisplay.blit(self.arrowBackwardImg, (self.x, self.y))
