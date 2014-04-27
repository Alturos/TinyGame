import os, sys
import pygame

class Sprite(pygame.sprite.Sprite):
    """Defines a base Sprite."""
    PlayerFrames = []
    MonsterFrames = []
    FBFrames = []
    spriteSheet = None
    
    def __init__(self, image, xPosition, yPosition, speed):
        pygame.sprite.Sprite.__init__(self)
        if(Sprite.spriteSheet == None):
            Sprite.spriteSheet = image
        self.image = pygame.Surface((32,32))
        self.Left = False
        self.Right = False
        self.Firing = False
        self.LastFired = 0.0
        self.XPosition = xPosition
        self.YPosition = yPosition
        self.Speed = speed
        self.Frame = 0
        self.Score = 0
        self.FrameTicks = 0
        self.Frame = 0
        self.rect = pygame.Rect(0,0,32,32)

    def update(self):
        """Updates the player"""
        self.LastFired += 1
        self.FrameTicks += 1
        if(self.Left):
            self.XPosition -= self.Speed
        if(self.Right):
            self.XPosition += self.Speed
        if(self.FrameTicks >= 10):
            self.Frame += 1
            self.FrameTicks = 0
            if(self.Frame > 1):
                self.Frame = 0
        self.rect.x = self.XPosition
        self.rect.y = self.YPosition

    def draw(self, screen):
        screen.blit(self.image, (self.XPosition, self.YPosition))
