########################################
#   Name:           EightQueen.py
#   Description:    AS1 : Problem 3(Part 1)
#                       An object representation of a 8x8 board with 8 queens placed upon it.
#                           The goal is to arrange them in such a way that none of the queens can complete a legal move
#                           that would capture another queen.
#   Author:         Xander Palermo <ajp2s@missouristate.edu>
#   Date:           16 March 2025
#
#   Class:          CSC 540 - Introduction to Artificial Intelligence
#   Teacher:        Dr. Rahul Dubey
########################################
from random import randint
from Matrix import Matrix
import numpy as np

QUEEN_TOKEN = 'Q'

class EightQueen(Matrix):
    def __init__(self):
        LENGTH = 8
        super().__init__(LENGTH)


    '''--- Getter Methods ---'''
    def getState(self) -> list[int]:
        """
        :return: a list representing at what y level each queen is placed at for each column
        """
        state = []
        for x in range(self.getLength()):
            for y in range(self.getLength()):
                token = self.getCoordinateValue(x,y)
                if token == QUEEN_TOKEN:
                    state.append(y)
                    break
        return state
    '''----------------------'''

    '''--- Setter Methods ---'''
    def randomize(self):
        """
        Sets the board to a randomized state
        Ever queen token is placed on the x-axis with a y amount of displacement
        :return:
        """
        self._clearBoard()
        for x in range(self.LENGTH):
            y = randint(0,self.LENGTH-1)
            self.setValue(QUEEN_TOKEN,x,y)

    def setBoard(self,state:list[int]) -> int:
        """
        Sets the board to a predetermined state
        :return: 0 if the state is invalid
        """
        self._clearBoard()
        if len(state) < self.LENGTH:
            return 0
        for x in range(self.LENGTH):
            self.setValue(QUEEN_TOKEN,x,state[x])
        return 1
    '''----------------------'''


    def checkHorizontal(self) -> list[int]:
        """
        Checks if any queen can capture another along the horizontal axis
        :return: the number of queens that violate the rule
        """
        summation = []

        for y in range(self.LENGTH):
            summation.append(
                sum([+1 for x in range(self.LENGTH) if self.getCoordinateValue(x,y) == QUEEN_TOKEN]))

        return summation

    def checkPositiveDiagonal(self):
        """
        Checks if any queen can capture another along a diagonal axis (bottom left -> top right)
        :return: the number of queens that violate the rule
        """
        summation = []
        for diagonalIndex in range(-self.getLength()+1,self.getLength(),1):
            summation.append(sum(+1 for token in np.diagonal(self._getMatrix(),offset=diagonalIndex) if token == QUEEN_TOKEN))
        return summation

    def checkNegativeDiagonal(self):
        """
        Checks if any queen can capture another along a diagonal axis (bottom right -> top left)
        :return: the number of queens that violate the rule
        """
        summation = []
        for diagonalIndex in range(-self.getLength()+1,self.getLength(),1):
            # print(np.diagonal(np.fliplr(self._getMatrix()),offset=diagonalIndex))
            summation.append(sum(+1 for token in np.diagonal(np.fliplr(self._getMatrix()),offset=diagonalIndex) if token == QUEEN_TOKEN))
        return summation

    def print(self, fill = "N/A") -> None:
        """calls parent function with special parameters"""
        super().print(fill = "_")

def main():
    board = EightQueen()
    board.setBoard([0,1,2,3,4,5,6,7])
    # board.randomize()
    board.print()
    # print(board.checkHorizontal())
    # print(board.checkPositiveDiagonal())
    # print(board.checkNegativeDiagonal())
    # print(board.getCoordinateValue(1,1))
    r = board.getState()
    board.randomize()
    print()
    board.print()
    board.setBoard(r)
    print()
    board.print()

if __name__ == "__main__":
    main()


