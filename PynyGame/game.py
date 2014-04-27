import os, sys
import re
import pygame
import pygame._view
from pygame.locals import *
from random import randint
from Player import Player
from Monster import Monster
if not pygame.font: print('Fonts disabled.')
if not pygame.mixer: print('Sound disabled.')

spriteSheet= None
monsters = None
bullets = None
player = None
spells = None
scoreText = None
text = None

def reset(gameOver = True):
    global monsters
    global spells
    global bullets
    if(gameOver):
        player.XPosition = 300
        player.Score = 0
        renderText()
    monsters.empty()
    bullets.empty()
    spells.empty()
    for i in range(0, randint(9,16)):
        mstr = Monster(spriteSheet)
        monsters.add(mstr)

def playerCollide(a, b):
    if(pygame.sprite.collide_rect(a,b)):
        reset()
        return True
    return False

def spellCollide(a,b):
    if(pygame.sprite.collide_rect(a,b)):
        player.Score += a.Score
        renderText()
        return True
    return False

def renderText():
    global scoreText
    scoreText = text.render("Score: " + str(player.Score), True, (255,255,255))

def main():
    global monsters
    global player
    global bullets
    global spriteSheet
    global spells
    global text
    pygame.init()
    size = (800, 600)
    screen = pygame.display.set_mode(size)
    text = pygame.font.SysFont(None, 24)
    pygame.display.set_caption("Pyny Game!")
    spriteSheet = pygame.image.load("Sprites.png").convert_alpha()
    monsters = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    spells = pygame.sprite.Group()
    player = Player(spriteSheet)
    renderText()
    reset()
    done = False
    gameTime = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    while not done:
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                done = True
            elif(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_ESCAPE):
                    done = True
                player.HandleKeyDown(event.key)
            elif(event.type == pygame.KEYUP):
                player.HandleKeyUp(event.key)
        screen.fill((0,130,15))
        if(not monsters):
            reset(False)
        player.update(spells)
        monsters.update(bullets)
        bullets.update()
        spells.update()
        pygame.sprite.spritecollide(player, bullets, True, playerCollide);
        pygame.sprite.groupcollide(monsters, spells, True, True, spellCollide);
        monsters.draw(screen)
        bullets.draw(screen)
        spells.draw(screen)
        player.draw(screen)
        screen.blit(scoreText, (0,0))
        pygame.display.flip()
        gameTime.tick(30)
    pygame.quit()

main()
