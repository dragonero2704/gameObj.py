import pygame
from pygame.image import load
class Window:
     def __init__(self, windowSize: tuple[2], caption:str = None, iconPath:str = None):
        self.windowSize = windowSize
        self.caption = caption
        if not pygame.get_init():
                # print("Calling pygame.init()")
                pygame.init()
        if caption is not None:
             pygame.display.set_caption(caption)
        if iconPath is not None:
             pygame.display.set_icon(load(iconPath))
        self.surface = pygame.display.set_mode(self.windowSize)
     
     def gameLoop(self):
         pass
         
     def gameOver(self):
         pass

     def startScreen(self):
          pass
    


        