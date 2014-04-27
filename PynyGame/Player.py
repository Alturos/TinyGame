import os, sys
import pygame
from random import randint
from Sprite import Sprite
from Fireball import Fireball

class Player (Sprite):
    """Defines the player."""
    SEffect = None

    def __init__(self, image):
        Sprite.__init__(self, image, 300, 568, 3)

        if(Sprite.PlayerFrames == []):
            Sprite.PlayerFrames.append(pygame.Surface((32,32)).convert_alpha())
            Sprite.PlayerFrames.append(pygame.Surface((32,32)).convert_alpha())
            Sprite.PlayerFrames.append(pygame.Surface((32,32)).convert_alpha())
            Sprite.PlayerFrames[0].fill((0,0,0,0))
            Sprite.PlayerFrames[1].fill((0,0,0,0))
            Sprite.PlayerFrames[2].fill((0,0,0,0))
            Sprite.PlayerFrames[0].blit(image,(0,0),(0,0,32,32))
            Sprite.PlayerFrames[1].blit(image,(0,0),(0,32,32,32))
            Sprite.PlayerFrames[2].blit(image,(0,0),(0,64,32,32))
        if(Player.SEffect == None):
            Player.SEffect = pygame.mixer.Sound("Fireball1.wav")
    
    def HandleKeyDown(self, key):
        """Updates the input state"""
        if(key == pygame.K_LEFT):
            self.Left = True
        elif(key == pygame.K_RIGHT):
            self.Right = True
        elif(key == pygame.K_SPACE):
            self.Firing = True
            

    def HandleKeyUp(self, key):
        """Updates the input state"""
        if(key == pygame.K_LEFT):
            self.Left = False
        elif(key == pygame.K_RIGHT):
            self.Right = False
        elif(key == pygame.K_SPACE):
            self.Firing = False
         
    def update(self, bullets):
        """Updates the player"""
        if(self.Firing and self.LastFired > 40):
            self.LastFired = 0
            self.Frame = 2
            self.FrameTicks = 0
            s = Fireball(self.spriteSheet, self.XPosition, self.YPosition, 0)
            bullets.add(s)
            Player.SEffect.play()
        Sprite.update(self)
        self.image = Sprite.PlayerFrames[self.Frame]

    def draw(self, screen):
        
        Sprite.draw(self, screen)
        
        
    
