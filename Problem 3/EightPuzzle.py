import random
from random import randint

from Matrix import Matrix

COORDINATES =  [(0,2), (1,2), (2,2),
                (0,1), (1,1), (2,1),
                (0,0), (1,0),(2,0)]

class EightPuzzle:
    def __init__(self):
        self.__board = Matrix(3)
        self.__emptySpace = self.randomizeBoard()
        # print(self.__emptySpace)

    def getState(self):
        state = []
        for coord in COORDINATES:
            state.append(self.__board.getCoordinateValue(coord[0], coord[1]))
        return state

    def randomizeBoard(self):
        validCoordinates = COORDINATES.copy()
        for i in range(1,9):
            success = 0
            while not success:
                choice = random.choice(validCoordinates)
                success = self.__board.setValue(i,choice[0], choice[1])
                validCoordinates.remove(choice)
        return validCoordinates[0]

    def setBoard(self, state):
        self.__board = Matrix(3)
        for coord in COORDINATES:
            self.__board.setValue(state.pop(0), coord[0], coord[1])

    def __atomicExchange(self, selected: tuple[int, int]) -> int:
        """
        Swaps the empty tile in the matrix with a pre-established coordinate
        :param selected: the coordinate that the value being placed into the empty tile will be taken from.
        :post: The tile that is selected becomes the new empty tile of the matrix
        :return: -1 if the move cannot be completed, 1 if otherwise
        """
        if selected not in COORDINATES:
            return -1
        self.__board.setValue(self.__board.getCoordinateValue(selected[0], selected[1]), #Place selected tile in empty place
                              self.__emptySpace[0], self.__emptySpace[1])
        self.__emptySpace = (selected[0], selected[1])
        self.__board.setValue(None, self.__emptySpace[0], self.__emptySpace[1], Override=True)     #Set the tile that was selected to None
        return 1

    def moveUp(self):
        selected = (self.__emptySpace[0], self.__emptySpace[1] - 1)
        return self.__atomicExchange(selected)

    def moveDown(self):
        selected = (self.__emptySpace[0], self.__emptySpace[1] + 1)
        return self.__atomicExchange(selected)

    def moveLeft(self):
        selected = (self.__emptySpace[0] - 1, self.__emptySpace[1])
        return self.__atomicExchange(selected)

    def moveRight(self):
        selected = (self.__emptySpace[0] + 1, self.__emptySpace[1])
        return self.__atomicExchange(selected)

    def __checkBoard(self):
        if self.__board.getCoordinateValue(0, 2) is not None:
            return
        for num in range(1,9):
            coord = COORDINATES[num-1]
            if self.__board.getCoordinateValue(coord[0], coord[1]) != num:
                return False
        return True

    def print(self):
        self.__board.print(fill="_")

def main():
    puz = EightPuzzle()
    puz.print()
    state = puz.getState()
    puz = EightPuzzle()
    print()
    puz.print()
    puz.setBoard(state)
    print()
    puz.print()

if __name__ == '__main__':
    main()
