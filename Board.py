from typing import Tuple
import pygame
import random
from Pieces import *


STEP_TIMER = 200

class Board():

    def __init__(self) -> None:
        self.grid = [[(0,0,0) for x in range(10)] for x in range(20)]
        self.lockedPieces = dict()
        self.currentPiecePosition = (5,3) #Position Rotation
        self.currentPieceRotation = 0
        self.currentPiece = PieceType.HERO # random.choice(list(PieceType))
        self.nextPiece = random.choice(list(PieceType))
        self.pieceCells = occupied_positions(self.currentPiece,self.currentPiecePosition, self.currentPieceRotation)
        self.nextStepTimer = STEP_TIMER #miliseconds

    def newPiece(self):
        self.currentPiece = self.nextPiece
        self.currentPiecePosition = (5,3)
        self.currentPieceRotation = 0
        self.nextPiece = random.choice(list(PieceType))
        self.pieceCells = occupied_positions(self.currentPiece,self.currentPiecePosition, self.currentPieceRotation)


    def rotate(self):
        self.currentPieceRotation = (self.currentPieceRotation + 1) % len(PieceDictionary[self.currentPiece])
        self.pieceCells = occupied_positions(self.currentPiece,self.currentPiecePosition, self.currentPieceRotation)


    def move(self ,isLeft):
        x,y = self.currentPiecePosition
        new_x = 0
        if isLeft:
            new_x = x - 1
        else:
            new_x = x + 1

        if self.WillCollide((new_x,y)):
            return
        else:
            self.currentPiecePosition = (new_x,y)
            self.pieceCells = occupied_positions(self.currentPiece,self.currentPiecePosition, self.currentPieceRotation)

    
    def WillCollide(self,position)-> bool:
        newCells = occupied_positions(self.currentPiece, position, self.currentPieceRotation)

        for idx, val in enumerate(newCells):
            x,y = val
            ##Check against boundaries
            sidesBoundarie =  x < 0 or x >= 10
            reachedBottom =  y >= 20
            collided_with_peace = (x,y) in self.lockedPieces
            if sidesBoundarie or reachedBottom or collided_with_peace:
                return True

        return False


    def lockPiece(self, positions: Tuple[int, int]):
        for idx, val in enumerate(positions):
            self.lockedPieces[(val[0], val[1])] = PieceColors[self.currentPiece.value]

    # def checkScore(self):

    #     for i in range(20):
    #         for j in range(10):
    #             if (j,i) not in self.lockedPieces:
    #                 return False


    def increaseScore(self):
        print("SCORE")

    def step(self, deltaTime):
        x,y = self.currentPiecePosition
        
        if self.WillCollide((x,y+1)):
            self.lockPiece(self.pieceCells)
            self.newPiece()

        # if self.checkScore():
        #     self.increaseScore()

        if self.nextStepTimer <= 0:
            y += 1
            self.currentPiecePosition = (x,y)
            self.pieceCells = occupied_positions(self.currentPiece,self.currentPiecePosition, self.currentPieceRotation)
            self.nextStepTimer = STEP_TIMER
        else:
            self.nextStepTimer -= deltaTime


    def draw(self,win):
        #Fill screen with black
        win.fill((0,0,0))

        #Draw Locked Pieaces
        for idx, val in enumerate(self.lockedPieces):
            pygame.draw.rect(win, self.lockedPieces[(val[0], val[1])] ,(val[0]*30,val[1]*30,30,30),0)

        #Draw Current Piece
        for idx, val in enumerate(self.pieceCells):
            pygame.draw.rect(win,PieceColors[self.currentPiece.value],(val[0]*30,val[1]*30,30,30),0)

      