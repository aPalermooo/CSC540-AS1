import heapq
from copy import deepcopy
from typing import Optional

from EightQueen import EightQueen

class HillClimber:
    class Pair:
        def __init__(self, left, right):
            self.left = left
            self.right = right

        def __lt__(self, other):
            return self.left < other.left

    def __init__(self, state: Optional[list[int]] = None):
        self.game = EightQueen()
        if state is None:
            self.game.randomize()
            self.gameState = self.game.getState()
        else:
            self.game.setBoard(state)
            self.gameState = state

        self.__bestBoards = []
        self.game.print()
        for i in range(5000):
            # self.game.setBoard(self.__checkNeighbors())
            state = self.__checkNeighbors()
            # print(state)
            # print(self.game.getState())
            if self.game.getState() == state:
                heapq.heappush(self.__bestBoards, HillClimber.Pair(
                    self.__checkHeuristic(self.game), self.game.getState()
                ))
                self.game.randomize()
                self.gameState = self.game.getState()
            else:
                self.game.setBoard(state)
        if self.__bestBoards:
            self.game.setBoard(self.__bestBoards[0].right)
        print()
        self.game.print()

    @staticmethod
    def __checkHeuristic(game):
        # Calculate the heuristic value (the number of conflicts)
        horizontal = sum([-1 for element in game.checkHorizontal() if element == 1])
        posDiagonal = sum([-1 for element in game.checkPositiveDiagonal() if element == 1])
        negDiagonal = sum([-1 for element in game.checkNegativeDiagonal() if element == 1])
        return horizontal + posDiagonal + negDiagonal

    def __checkNeighbors(self):
        neighborState : list[HillClimber.Pair] = []

        for x in range(len(self.gameState)):
            if self.gameState[x] > 0:
                possibleState = deepcopy(self.gameState)
                possibleState[x] = possibleState[x] - 1
                possibleGame = EightQueen()
                possibleGame.setBoard(possibleState)
                heapq.heappush(neighborState, HillClimber.Pair(self.__checkHeuristic(possibleGame), possibleState))
            if self.gameState[x] < 7:
                possibleState = deepcopy(self.gameState)
                possibleState[x] = possibleState[x] + 1
                possibleGame = EightQueen()
                possibleGame.setBoard(possibleState)
                heapq.heappush(neighborState, HillClimber.Pair(self.__checkHeuristic(possibleGame), possibleState))
        return neighborState[0].right

        # for index, position in enumerate(self.game.getState()):
        #     if position > 0:
        #         # Check moving the queen one row up (position - 1)
        #         possibilityState = self.gameState.copy()
        #         possibilityState[index] = position - 1
        #         possibilityGame = EightQueen()
        #         possibilityGame.setBoard(possibilityState)
        #         possibilityHeuristic = self.__checkHeuristic(possibilityGame)
        #         if possibilityHeuristic > maxNeighborHeuristic:
        #             maxNeighborState = possibilityState
        #             maxNeighborHeuristic = possibilityHeuristic
        #
        #     if position < 7:
        #         # Check moving the queen one row down (position + 1)
        #         possibilityState = self.gameState.copy()
        #         possibilityState[index] = position + 1
        #         possibilityGame = EightQueen()
        #         possibilityGame.setBoard(possibilityState)
        #         possibilityHeuristic = self.__checkHeuristic(possibilityGame)
        #         if possibilityHeuristic > maxNeighborHeuristic:
        #             maxNeighborState = possibilityState
        #             maxNeighborHeuristic = possibilityHeuristic
        #
        # return maxNeighborState


def main():
    hill = HillClimber()

if __name__ == "__main__":
    main()
