import pygame 
import random
import math
from Pieces import *
from Board import *

##Setup game variables
SCREEN_WIDTH, SCREEN_HEIGHT = 300, 600
run = True

pygame.init() 
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
pygame.display.set_caption("Fake Python Tetris") 


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
            if event.key == pygame.K_a:
                board.move(isLeft=True)
            if event.key == pygame.K_d:
                board.move(isLeft=False)
            if event.key == pygame.K_r:
                board.newPiece()


    board.step(deltaTime)
    board.draw(win)
    pygame.display.update()






