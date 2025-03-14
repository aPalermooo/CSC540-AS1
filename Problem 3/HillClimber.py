from typing import Optional

from EightQueen import EightQueen

class HillClimber:
    def __init__(self, state: Optional[list[int]] = None):
        self.game = EightQueen()
        if state is None:
            self.game.randomize()
            self.gameState = self.game.getState()
        else:
            self.game.setBoard(state)
            self.gameState = state

        self.game.print()
        for i in range(10000):
            self.game.setBoard(self.__checkNeighbors())

        print()
        self.game.print()

    @staticmethod
    def __checkHeuristic(game):
        # Calculate the heuristic value (the number of conflicts)
        horizontal = sum([1 for element in game.checkHorizontal() if element == 1])
        posDiagonal = sum([1 for element in game.checkPositiveDiagonal() if element == 1])
        negDiagonal = sum([1 for element in game.checkNegativeDiagonal() if element == 1])
        return horizontal + posDiagonal + negDiagonal

    def __checkNeighbors(self):
        maxNeighborHeuristic = self.__checkHeuristic(self.game)
        maxNeighborState = self.gameState

        for index, position in enumerate(self.game.getState()):
            if position > 0:
                # Check moving the queen one row up (position - 1)
                possibilityState = self.gameState.copy()
                possibilityState[index] = position - 1
                possibilityGame = EightQueen()
                possibilityGame.setBoard(possibilityState)
                possibilityHeuristic = self.__checkHeuristic(possibilityGame)
                if possibilityHeuristic > maxNeighborHeuristic:
                    maxNeighborState = possibilityState
                    maxNeighborHeuristic = possibilityHeuristic

            if position < 7:
                # Check moving the queen one row down (position + 1)
                possibilityState = self.gameState.copy()
                possibilityState[index] = position + 1
                possibilityGame = EightQueen()
                possibilityGame.setBoard(possibilityState)
                possibilityHeuristic = self.__checkHeuristic(possibilityGame)
                if possibilityHeuristic > maxNeighborHeuristic:
                    maxNeighborState = possibilityState
                    maxNeighborHeuristic = possibilityHeuristic

        return maxNeighborState


def main():
    hill = HillClimber()

if __name__ == "__main__":
    main()
