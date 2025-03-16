########################################
#   Name:           HillClimber.py
#   Description:    AS1 : Problem 3(Part 2)
#                       Runs a greedy search algorithm on the attached EightPuzzle.py to find a completed state of the
#                           Puzzle using the allowed moves
#   Author:         Xander Palermo <ajp2s@missouristate.edu>
#   Date:           16 March 2025
#
#   Class:          CSC 540 - Introduction to Artificial Intelligence
#   Teacher:        Dr. Rahul Dubey
########################################
from copy import deepcopy
from random import randint
from matplotlib import pyplot as mlt
from EightPuzzle import EightPuzzle

NUM_ITERATIONS = 1000
RANDOM_RESET_CHANCE = 5

NEIGHBOR_ACTIONS = ["moveUp", "moveDown", "moveLeft", "moveRight"]

class HillClimber:
    def __init__(self, state : list[int | None] | None = None):
        """
        Begins a simulation of a hill climbing algorithm on an Eight tile slide puzzle
        Runs for MAX_ITERATIONS iterations.
        Every iteration there is a RANDOM_RESET_CHANCE chance of a reset occurring
        :param state: Can be selected to start at a specific state, if none provided the starting state is randomized
        """
        self.__puzzle = EightPuzzle()
        if state is None:
            self.__puzzle.randomize()
            self.__currentHeuristic = self.__checkHeuristic(self.__puzzle)
        else:
            self.__puzzle.setBoard(state)
            self.__currentHeuristic = self.__checkHeuristic(self.__puzzle)


        self.__bestBoards : list[tuple[int, list[int | None]]]= []
        self.__graphData = []

        print("Starting Game state is:")
        self.__puzzle.print()
        print("\nStarting Hill Climber Algorithm...")

        for iteration in range(NUM_ITERATIONS):
            state = self.__checkNeighbors()
            self.__puzzle.setBoard(state)
            self.__graphData.append((iteration, self.__checkHeuristic(self.__puzzle)))
            if randint(1,100) <= RANDOM_RESET_CHANCE:
                self.__bestBoards.append((self.__checkHeuristic(self.__puzzle),
                                          self.__puzzle.getState()))
                self.__puzzle.randomize()
            self.__currentHeuristic = self.__checkHeuristic(self.__puzzle)

        self.__bestBoards.sort(key = lambda x: x[0])
        self.__puzzle.setBoard(self.__bestBoards[-1][1])


        self.__puzzle.print()
        print(self.__checkHeuristic(self.__puzzle))
        self.plot()

    def __checkHeuristic(self, puzzle : EightPuzzle):
        """
        Determines a heuristic of a puzzle state based on the number of tiles that
            are in the correct spot
        :param puzzle: the puzzle to be evaluated
        :return: the number of tiles within the provided puzzle that are in the correct spot
        """
        heuristic = 0
        state = puzzle.getState()
        for i in range(1,10):
            heuristic += 1 if state[i-1] == i else 0
        heuristic += 1 if state[-1] is None else 0
        return heuristic

    def __checkNeighbors(self) -> list[int | None]:
        """
        Attempts to use each action on a temporary copy of the current puzzle state,
        :return: a 2D list representation of the state of the puzzle after completing the most optimal move
        """
        neighborStates : list[tuple[int, list[int]]] = []
        for action in NEIGHBOR_ACTIONS:
            possiblePuzzle = deepcopy(self.__puzzle)
            success = getattr(possiblePuzzle, action)()
            if bool(success):
                neighborStates.append((self.__checkHeuristic(possiblePuzzle),
                                       possiblePuzzle.getState()))
        neighborStates.sort(key=lambda x: x[0])
        return neighborStates[-1][1]

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
    HillClimber()

if __name__ == "__main__":
    main()