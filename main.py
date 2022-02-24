import pygame 
import random
import math
from Pieces import *
from Board import *

##Setup game variables
SCREEN_WIDTH, SCREEN_HEIGHT = 300, 700
run = True

pygame.init() 
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
pygame.display.set_caption("Fake Python Tetris") 

pygame.mixer.music.load('media\Tetris_theme.wav')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

board = Board()
lastTime = pygame.time.get_ticks()
deltaTime = 0

while run:

    deltaTime = pygame.time.get_ticks() - lastTime 
    lastTime = pygame.time.get_ticks()

    # creates time delay of 10ms 
    pygame.time.delay(10)
    keys = pygame.key.get_pressed() 
    # iterate over the list of Event objects 
    # that was returned by pygame.event.get() method. 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                board.rotate()
            if event.key == pygame.K_a or event.key == pygame.K_LEFT :
                board.move(isLeft=True)
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT :
                board.move(isLeft=False)
            if event.key == pygame.K_s or event.key == pygame.K_DOWN :
                board.moveDown()
            if event.key == pygame.K_r and board.gameState == "LOST":
                board = Board()
                pygame.mixer.music.play()


    if board.gameState != "LOST" :
        board.step(deltaTime)
        board.draw(win)
    else:
        board.drawLoseScreen(win)
        pygame.mixer.music.stop()

    pygame.display.update()






