import random
from typing import List


class Game:

    BLANK = "_"
    PLAYER_ONE_TOKEN = "X"
    PLAYER_TWO_TOKEN = "O"
    BOARD_LENGTH = 3

    class __CoordinatePair:
        def __init__(self, x:int, y:int) -> None:
            self.x = x
            self.y = y

        def print(self) -> None:
            print(f"({self.x},{self.y})")

    def __init__(self):
        self.__boardState = [[self.BLANK] * self.BOARD_LENGTH for _ in range(self.BOARD_LENGTH)]
        self.__turn = 0

    def getBoardStateDep(self):
        return self.__boardState

    def getBoardState(self) -> list[str]:
        # return self.__boardState
        output = []
        for y in range(self.BOARD_LENGTH):
            for x in range(self.BOARD_LENGTH):
                output.append(self.__boardState[y][x])
        return output

    def printBoardState(self) -> None:
        for i in self.__boardState:
            for j in i:
                print(j, end=" ")
            print()

    def isPlayerOneTurn(self) -> bool:
        return self.__turn % 2 == 0

    def getCurrentPlayerToken(self):
        if self.isPlayerOneTurn():
            return self.PLAYER_ONE_TOKEN
        return self.PLAYER_TWO_TOKEN

    def getLastPlayerToken(self):
        if self.isPlayerOneTurn():
            return self.PLAYER_TWO_TOKEN
        return self.PLAYER_ONE_TOKEN

    def __convertToCoordinate(self, index:int) -> __CoordinatePair:
        index = index - 1
        y = index // self.BOARD_LENGTH
        x = index % self.BOARD_LENGTH
        return self.__CoordinatePair(x,y)

    def __isSpaceEmpty(self, coord:__CoordinatePair):
        return self.BLANK == self.__boardState[coord.y][coord.x]

    def __isTerminalState(self, playerToken) -> bool:

        ##Terminal condition is reached when there exists 3 in a row of a players token anywhere on the board

        #check row for terminal condition
        for row in self.__boardState:
            if all(space == playerToken for space in row):
                # print("row")           # Dbug
                return True

        #check columns for terminal condition
        for col in range(self.BOARD_LENGTH):
            if all(self.__boardState[row][col] == playerToken for row in range(self.BOARD_LENGTH)):
                # print("col")        #Dbug
                return True

        #check L -> R Diagonal for terminal condition
        if all(self.__boardState[space][space] == playerToken for space in range(self.BOARD_LENGTH)):
            # print("dia")           #Dbug
            return True

        #check R -> L Diagonal for terminal condition
        x = self.BOARD_LENGTH - 1
        y = 0
        while x>=0:
            if not self.__boardState[y][x] == playerToken:
                return False
            x -= 1
            y += 1
        # print("anti-dia")       #Dbug
        return True

    def doTurn(self, index : int) -> int:
        terminal = 0
        coordinate = self.__convertToCoordinate(index)
        isEmpty = self.__isSpaceEmpty(coordinate)
        if not isEmpty:     #Space is occupied
            return -1

        if self.isPlayerOneTurn():
            self.__boardState[coordinate.y][coordinate.x] = self.PLAYER_ONE_TOKEN
            if self.__isTerminalState(self.PLAYER_ONE_TOKEN):
                terminal = 1
        else:
            self.__boardState[coordinate.y][coordinate.x] = self.PLAYER_TWO_TOKEN
            if self.__isTerminalState(self.PLAYER_TWO_TOKEN):
                terminal = 2

        self.__turn +=1

        # self.printBoardState()
        print()
        return terminal

def main():
    test = Game()
    test.printBoardState()
    print()
    notTerminal = 0
    it = 0
    while notTerminal <= 0 and it < 9:
        # notTerminal = test.doTurn(random.randint(1,9))
        notTerminal = test.doTurn(int(input()))
        it += 1

if __name__ == "__main__":
    main()
