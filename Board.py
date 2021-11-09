from typing import List, Tuple
import pygame
import random
from Pieces import *


STEP_TIMER = 200

class Board():

    def __init__(self) -> None:
        self.nextStepTimer = STEP_TIMER #miliseconds

        self.lockedPieces = dict() #Pieces that are already locked on the board { (x,y) : color }

        self.currentPiecePosition = (5,3) #Position Rotation
        self.currentPieceRotation = 0
        self.currentPiece =  random.choice(list(PieceType))
        self.nextPiece = random.choice(list(PieceType))
        #List of cells that the current piece occupies
        self.pieceCells = occupied_positions(self.currentPiece,self.currentPiecePosition, self.currentPieceRotation)

        self.gameState = "PLAYING" #Used strings because of simplicity
        self.score = 0

    def newPiece(self):
        self.currentPiece = self.nextPiece
        self.currentPiecePosition = (5,3)
        self.currentPieceRotation = 0
        self.nextPiece = random.choice(list(PieceType))
        self.pieceCells = occupied_positions(self.currentPiece,self.currentPiecePosition, self.currentPieceRotation)

        # for idx, cell in self.pieceCells:
        #     if cell in self.lockedPieces:
        #         print("lost")
        #         self.gameState == "LOST"


    def rotate(self):
        self.currentPieceRotation = (self.currentPieceRotation + 1) % len(PieceDictionary[self.currentPiece])
        self.pieceCells = occupied_positions(self.currentPiece,self.currentPiecePosition, self.currentPieceRotation)

    def moveDown(self):
        self.nextStepTimer = 0 #Moving down is the same as doing a new step down

    def move(self ,isLeft: bool):
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

    
    def WillCollide(self,position:  Tuple[int, int])-> bool:
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

    def checkCompleteRows(self)-> List[int]:

        complete_rows = []

        for i in range(20):
            counter = 0
            for j in range(10):
                if (j,i) in self.lockedPieces:
                    counter += 1

            if counter == 10:
                complete_rows.append(i)
        return complete_rows

    def removeRow(self, row: int):
        for j in range(10):
            self.lockedPieces.pop((j,row))
        
    def pullDown(self, row: int):
        #in reverse to avoid putting two pieces in the same place momentarily
        for i in reversed(range(row)):
            for j in range(10):
                #Do nothing if the piece to pull down is black
                if (j,i) not in self.lockedPieces:
                    continue         
                else: #remove the current locked piece and replace it one  cell bellow
                    color = self.lockedPieces[(j,i)]
                    self.lockedPieces.pop((j,i))
                    self.lockedPieces[(j,i+1)] = color

    def checkScore(self):
        complete_rows = self.checkCompleteRows()

        #For all full rows: delete the row and pull down all rows above
        for idx, row in enumerate(complete_rows):
            self.removeRow(row)
            self.pullDown(row)
            self.score += 1


    def step(self, deltaTime):
        x,y = self.currentPiecePosition
        
        if self.WillCollide((x,y+1)):
            self.lockPiece(self.pieceCells)
            self.newPiece()

        self.checkScore()

        if self.nextStepTimer <= 0:
            y += 1
            self.currentPiecePosition = (x,y)
            self.pieceCells = occupied_positions(self.currentPiece,self.currentPiecePosition, self.currentPieceRotation)
            self.nextStepTimer = STEP_TIMER
        else:
            self.nextStepTimer -= deltaTime


    def draw(self, win: pygame.Surface):
        #Fill screen with black
        win.fill((0,0,0))

        #Draw Locked Pieaces
        for idx, val in enumerate(self.lockedPieces):
            pygame.draw.rect(win, self.lockedPieces[(val[0], val[1])] ,(val[0]*30,val[1]*30,30,30),0)

        #Draw Current Piece
        for idx, val in enumerate(self.pieceCells):
            pygame.draw.rect(win,PieceColors[self.currentPiece.value],(val[0]*30,val[1]*30,30,30),0)

      