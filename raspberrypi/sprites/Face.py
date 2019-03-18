import pygame

class Face():
  def __init__(self, width, height, gameDisplay, speed=5):
    self.width = width
    self.height = height
    self.FaceImg = pygame.image.load('assets/face-1.png')
    self.FaceImg = pygame.transform.scale(self.FaceImg, (self.width, self.height))

    self.FaceImg2 = pygame.image.load('assets/face-2.png')
    self.FaceImg2 = pygame.transform.scale(self.FaceImg2, (self.width, self.height))
    
    self.currentFace = self.FaceImg;
    gameDisplay.blit(self.FaceImg, (0, 0))


  def play(self):
    pygame.mixer.music.load('assets/2.mp3')
    pygame.mixer.music.play(-1)

  # def tick(self):
  #   if self.currentFace == self.FaceImg:
  #     self.currentFace = self.FaceImg2;
  #   else:
  #     self.currentFace = self.FaceImg;

  def happy(self, gameDisplay):
    self.currentFace = self.FaceImg2;


  def sad(self, gameDisplay):
    self.currentFace = self.FaceImg;
