import os, sys
import pygame
from pygame.locals import *
from Sprite import Sprite

class Fireball(Sprite):
    """Defines a fireball"""
    def __init__(self, image, xPos, yPos, index):
        pygame.sprite.Sprite.__init__(self)
        Sprite.__init__(self, image, 0, 0, 0)
        self.image = pygame.Surface((32,32))
        self.Index = index
        self.XPosition = xPos
        self.YPosition = yPos
        self.Left = False
        self.Right = False
        if(Sprite.FBFrames == []):
            Sprite.FBFrames.append(pygame.Surface((32,32)).convert_alpha())
            Sprite.FBFrames.append(pygame.Surface((32,32)).convert_alpha())
            Sprite.FBFrames.append(pygame.Surface((32,32)).convert_alpha())
            Sprite.FBFrames.append(pygame.Surface((32,32)).convert_alpha())
            Sprite.FBFrames[0].fill((0,0,0,0))
            Sprite.FBFrames[1].fill((0,0,0,0))
            Sprite.FBFrames[2].fill((0,0,0,0))
            Sprite.FBFrames[3].fill((0,0,0,0))
            Sprite.FBFrames[0].blit(image,(0,0),(96,0,32,32))
            Sprite.FBFrames[1].blit(image,(0,0),(96,32,32,32))
            Sprite.FBFrames[2].blit(image,(0,0),(128,0,32,32))
            Sprite.FBFrames[3].blit(image,(0,0),(128,32,32,32))

    def update(self):
        Sprite.update(self)
        if(self.Index == 0):
            self.YPosition -= 6
        else:
            self.YPosition += 4
        self.image = Sprite.FBFrames[self.Frame + self.Index * 2]

