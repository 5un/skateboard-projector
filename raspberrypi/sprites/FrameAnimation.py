import pygame

class FrameAnimation():

  def __init__(self, width, height, frames=[], frameDuration=1000, lastFrameDuration=3000):
    self.width = width
    self.height = height

    self.frameImages = []

    for frame in frames: 
      img = pygame.image.load(frame)
      img = pygame.transform.scale(img, (self.width, self.height))
      self.frameImages.append(img)

    self.x = 0
    self.y = 0
    self.currentFrameIndex = 0
    self.timeElapsed = 0
    self.frameDuration = frameDuration
    self.currentFrameDuration = frameDuration
    self.lastFrameDuration = lastFrameDuration

  def tick(self, duration):
    if self.timeElapsed < self.currentFrameDuration:
      self.timeElapsed += duration
    else:
      if(self.currentFrameIndex == len(self.frameImages) - 1): 
        self.currentFrameIndex = 0
        self.currentFrameDuration = self.frameDuration
      elif(self.currentFrameIndex == len(self.frameImages) - 2): 
        self.currentFrameIndex += 1
        self.currentFrameDuration = self.lastFrameDuration
      else:
        self.currentFrameIndex += 1
        self.currentFrameDuration = self.frameDuration
      self.timeElapsed = 0

  def draw(self, gameDisplay):
    gameDisplay.blit(self.frameImages[self.currentFrameIndex], (self.x, self.y))
