import pygame

class ImageSwitcher():

  def __init__(self, width, height):
    self.width = width
    self.height = height
    # self.speed = speed
    self.sprites = {}
    
    spriteInfo =[
      {"name": "lol", "file": "assets/lol.png"},
      {"name": "eye", "file": "assets/eye.png"},
      {"name": "heart", "file": "assets/heart.png"}
    ]

    for sprite in spriteInfo:
      img = pygame.image.load(sprite["file"]).convert()
      self.sprites[sprite["name"]] = pygame.transform.scale(img, (self.width, self.height))
    
    self.x = 0
    self.y = 0

  def tick(self):
    pass

  def draw(self, gameDisplay, spriteName):
    gameDisplay.blit(self.sprites[spriteName], (self.x, self.y))
