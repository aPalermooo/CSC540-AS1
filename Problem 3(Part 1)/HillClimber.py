########################################
#   Name:           HillClimber.py
#   Description:    AS1 : Problem 3(Part 1)
#                       Runs a greedy search algorithm on the attached EightQueen.py to find a completed state of the
#                           problem in such that no queen can capture another
#   Author:         Xander Palermo <ajp2s@missouristate.edu>
#   Date:           16 March 2025
#
#   Class:          CSC 540 - Introduction to Artificial Intelligence
#   Teacher:        Dr. Rahul Dubey
########################################
import heapq
from matplotlib import pyplot as mlt
from copy import deepcopy
from typing import Optional

from EightQueen import EightQueen

NUM_ITERATIONS = 1000 # The number of iterations to run the simulation for

class HillClimber:
    class __Pair:
        """
        An auxiliary class that is used to pair heuristic values with their associated state such that
            the states can be sorted by their heuristic value.
        """
        def __init__(self, left, right):
            self.left = left
            self.right = right

        def __lt__(self, other):
            return self.left < other.left

    def __init__(self, state: Optional[list[int]] = None):
        """
        Begins a simulation of a hill climbing algorithm on an Eight Queen Puzzle
        Runs for MAX_ITERATIONS iterations.
        If encounters a local maximum, the state is randomized and the algorithm continues
        :param state: Can be selected to start at a specific state, if none provided the starting state is randomized
        """
        self.game = EightQueen()
        if state is None:
            self.game.randomize()
            self.gameState = self.game.getState()
        else:
            self.game.setBoard(state)
            self.gameState = state

        self.__bestBoards = []
        self.__graphData = []
        print("Starting Game state is:")
        self.game.print()
        print("\nStarting Hill Climber Algorithm...")
        # ran = 0
        for i in range(NUM_ITERATIONS):
            state = self.__checkNeighbors()
            if self.game.getState() == state:           # The hill climber has hit a local maxima
                # heapq.heappush(self.__bestBoards, HillClimber.__Pair(       # Save the current state and heuristic and restart
                #     self.__checkHeuristic(self.game), self.game.getState()))
                # print("random" + str(ran) + " " + str(self.__checkHeuristic(self.game)))
                # ran += 1
                self.__bestBoards.append(HillClimber.__Pair(       # Save the current state and heuristic and restart
                    self.__checkHeuristic(self.game), self.game.getState()))
                self.game.randomize()
                self.gameState = self.game.getState()
            else:
                self.game.setBoard(state)
            self.__graphData.append((i,self.__checkHeuristic(self.game)))
        if self.__bestBoards:       #If there were random restarts, pick the local maxima saved with the highest heuristic
            self.game.setBoard(min(self.__bestBoards).right)
        print("\n")
        print("Computed best game state is:")
        self.game.print()
        # print(len(self.__bestBoards))
        self.plot()

    @staticmethod
    def __checkHeuristic(game):
        """
        Calculates the heuristic value of a game depending on the number of queens that can capture one another
        :param game: the game to be evaluated
        :return: a representation of how close the state is to being complete
        """
        # Calculate the heuristic value (the number of conflicts)
        horizontal = sum([-1 for element in game.checkHorizontal() if element == 1])
        posDiagonal = sum([-1 for element in game.checkPositiveDiagonal() if element == 1])
        negDiagonal = sum([-1 for element in game.checkNegativeDiagonal() if element == 1])
        return horizontal + posDiagonal + negDiagonal

    def __checkNeighbors(self) -> list[int]:
        """
        Looks at all neighbor states and selected the largest heuristic value of them.
        If multiple have the same heuristic value, the one that was generated first is returned
            (Neighbors are generated from left to right along the 2D state list)
        :return: a game state as a 2D list
        """
        neighborState : list[HillClimber.__Pair] = []

        for x in range(len(self.gameState)):
            if self.gameState[x] > 0:                   #If the move cannot be done (ie the movement is impossible), it will not be considered
                possibleState = deepcopy(self.gameState)
                possibleState[x] = possibleState[x] - 1
                possibleGame = EightQueen()
                possibleGame.setBoard(possibleState)
                heapq.heappush(neighborState, HillClimber.__Pair(self.__checkHeuristic(possibleGame), possibleState))
            if self.gameState[x] < 7:
                possibleState = deepcopy(self.gameState)
                possibleState[x] = possibleState[x] + 1
                possibleGame = EightQueen()
                possibleGame.setBoard(possibleState)
                heapq.heappush(neighborState, HillClimber.__Pair(self.__checkHeuristic(possibleGame), possibleState))
        return neighborState[0].right

    def plot(self) -> None:
        """
        Uses data collected during runtime and plots it using a python library
        :return: None
        """
        x = [x[0] for x in self.__graphData]
        y = [x[1] for x in self.__graphData]
        mlt.plot(x,y)
        mlt.title("Hill Climber Algorithm")
        mlt.xlabel("Iteration")
        mlt.ylabel("Heuristic Value")
        mlt.show()

def main():
    hill = HillClimber()

if __name__ == "__main__":
    main()
