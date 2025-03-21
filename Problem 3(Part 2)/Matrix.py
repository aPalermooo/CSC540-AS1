########################################
#   Name:           Matrix.py
#   Description:    AS1 : Problem 3(Part 1)
#                       Creates an object representation of a Matrix that can be used to simulate a gameboard
#   Author:         Xander Palermo <ajp2s@missouristate.edu>
#   Date:           16 March 2025
#
#   Class:          CSC 540 - Introduction to Artificial Intelligence
#   Teacher:        Dr. Rahul Dubey
########################################
from typing import Optional
import numpy



class Matrix:
    PLACEHOLDER = None

    def __init__(self, LENGTH : int):
        self.LENGTH = LENGTH

        self._clearBoard()

    def _clearBoard(self):
        self.__matrix = numpy.array([[self.PLACEHOLDER] * self.LENGTH for _ in range(self.LENGTH)])

    '''--- Getter Methods ---'''
    def getLength(self) -> int:
        return self.LENGTH

    def _getMatrix(self) -> numpy.array:
        return self.__matrix

    def getCoordinateValue(self, x: int, y: int) -> Optional[int]:
        return self.__matrix[y][x]

    def isValidCoordinate(self, x:int, y: int) -> bool:
        return x <= self.LENGTH and y <= self.LENGTH
    '''----------------------'''

    '''--- Setter Methods ---'''
    def setValue(self, value, x:int, y:int, Override : bool = False) -> int:
        """

        :param value: The value to be placed into the Matrix
        :param x:       The x coordinate within the Matrix that is desired to be set
        :param y:       The y coordinate within the Matrix that is desired to be set
        :param Override: If set to True, will not check if there is already a value set in the coordinate and will overwrite it.
        :return:        If the value is set in the coordinate, returns 1, else returns 0. If Override == True, will always return 1
        """
        if Override or self.getCoordinateValue(x,y) is None:
            self.__matrix[y][x] = value
            return 1
        else:
            return 0
    '''----------------------'''

    def checkHorizontal(self):
        """
        Checks the matrix to see if for any row, all the values are the same
        :return: the value that repeats, but if the values are different for all rows returns None
        """
        for y in range(self.LENGTH):
            token = self.getCoordinateValue(0,y)
            if token is self.PLACEHOLDER:
                continue
            elif all(value == token for value in self.__matrix[y]):
                return token
        return None

    def checkVertical(self):
        """
        Checks the matrix to see if for any columns, all the values are the same
        :return: the value that repeats, but if the values are different for all column returns None
        """
        for x in range(self.LENGTH):
            token = self.getCoordinateValue(x, 0)
            if token is self.PLACEHOLDER:
                continue
            if all(self.getCoordinateValue(x,y) for y in range(self.LENGTH)):
                return token
        return None

    def checkNegativeDiagonal(self):
        """
        Checks the matrix to see if for the diagonal (Top Left -> Bottom Right), all the values are the same
        :return: the value that repeats, but if the values are different with the diagonal returns None
        """
        token = self.getCoordinateValue(0,0)
        if (token is not self.PLACEHOLDER and
                all(self.getCoordinateValue(i,i) == token for i in range(self.LENGTH))):
            return token
        return None

    def checkPositiveDiagonal(self):
        """
        Checks the matrix to see if for the diagonal (Top Left -> Bottom Right), all the values are the same
        :return: the value that repeats, but if the values are different with the diagonal returns None
        """
        token = self.getCoordinateValue(self.LENGTH - 1, 0)  # Bottom-left corner
        if token is not self.PLACEHOLDER and all(
                self.getCoordinateValue(self.LENGTH - 1 - i, i) == token for i in range(self.LENGTH)):
            return token
        return None

    def checkAll(self):
        """
        runs all check value methods
        :return: the value that repeats for any check method, but if none find a repeating value, returns None
        """
        token = self.checkHorizontal()
        if token is not None:
            return token

        token = self.checkVertical()
        if token is not None:
            return token

        token = self.checkNegativeDiagonal()
        if token is not None:
            return token

        token = self.checkPositiveDiagonal()
        if token is not None:
            return token

        return None                         # All checks Failed

    def print(self, fill = "N/A") -> None:
        for y in range(self.getLength()-1,-1,-1):
            for x in range(self.getLength()):
                value = self.getCoordinateValue(x,y)
                if value is self.PLACEHOLDER:
                    print(fill,end="\t")
                else:
                    print(value,end="\t")
            print(end="\n")

def main():
    tester = Matrix(8)
    tester.setValue(1, 0,0)
    tester.print()
    print(tester.checkAll())

if __name__ == "__main__":
    main()