import os, sys
import pygame
from pygame.locals import *
from random import randint
from Sprite import Sprite
from Fireball import Fireball

class Monster(Sprite):

    def __init__(self, image):
        Sprite.__init__(self, image, 0, 0, randint(1,5))
        self.Index = randint(0,1)
        self.XPosition = randint(0, 768)
        self.YPosition = randint(0, 15) * 32
        self.LastFired = randint(0,50)
        self.Score = self.Speed
        if(randint(0,1) == 1):
            self.Left = False
        else:
            self.Left = True

        self.Right = not self.Left
        
        if(Sprite.MonsterFrames == []):
            Sprite.MonsterFrames.append(pygame.Surface((32,32)).convert_alpha())
            Sprite.MonsterFrames.append(pygame.Surface((32,32)).convert_alpha())
            Sprite.MonsterFrames.append(pygame.Surface((32,32)).convert_alpha())
            Sprite.MonsterFrames.append(pygame.Surface((32,32)).convert_alpha())
            Sprite.MonsterFrames[0].fill((0,0,0,0))
            Sprite.MonsterFrames[1].fill((0,0,0,0))
            Sprite.MonsterFrames[2].fill((0,0,0,0))
            Sprite.MonsterFrames[3].fill((0,0,0,0))
            Sprite.MonsterFrames[0].blit(image,(0,0),(32,0,32,32))
            Sprite.MonsterFrames[1].blit(image,(0,0),(32,32,32,32))
            Sprite.MonsterFrames[2].blit(image,(0,0),(64,0,32,32))
            Sprite.MonsterFrames[3].blit(image,(0,0),(64,32,32,32))

    def update(self, bullets):
        Sprite.update(self)
        if(self.Left and self.XPosition <= 0):
            self.Left = False
            self.Right = True
        if(self.Right and self.XPosition >= 768):
            self.Right = False
            self.Left = True
        if(self.LastFired >= 50 and randint(0,25) == 5):
            b = Fireball(self.spriteSheet, self.XPosition, self.YPosition, 1)
            bullets.add(b)
            self.LastFired = 0
        self.image = Sprite.MonsterFrames[2 * self.Index + self.Frame]
            

    def draw(self, screen):
        Sprite.draw(self)
        
