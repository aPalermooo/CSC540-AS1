import copy
from os import abort

from numpy.f2py.auxfuncs import throw_error

from Node import Node
from TicTacToe import TicTacToe

MAX_SEARCH = 8

class MiniMax:
    def __init__(self):
        self.__game = TicTacToe()
        self.__root = Node(self.__game)

        self.__expandTree(self.__root)
        # for child in self.__root.getChildren():
        #     for grandchild in child.getChildren():
        #         grandchild.getMetadata().print()
        #         print()

    # def __getPossibleMoves(self, node):


    def __expandTree (self, node, maximize : bool = True):
        for index in range(1,10):
            possibleGame = copy.deepcopy(node.getMetadata())
            childExists = possibleGame.doTurn(index)
            # print(childExists)
            if childExists >= 0:
                child = node.createChild(possibleGame)
                heuristic = possibleGame.generateHeuristic()
                child.setHeuristic(heuristic)
                child.setLastMove(index)
                if heuristic is not None or child.getCost() > MAX_SEARCH:
                    continue
                self.__expandTree(child, not maximize)
        if not node.getChildren():
            return
        elif maximize:
            heuristic = (max([child.getHeuristic() for child in node.getChildren() if child.getHeuristic() is not None]
                             ,default=0))
        else:
            heuristic = (min([child.getHeuristic() for child in node.getChildren() if child.getHeuristic() is not None]
                             ,default=0))
        node.setHeuristic(heuristic)

    def __followGame(self):
        children = self.__root.getChildren()
        select = None
        for index in range(len(children)):
            child = children[index]
            # one = child.getMetadata().getState()
            # two = self.__game.getState()
            if child.getMetadata().getState() == self.__game.getState():
                select = index
                break
        if select is None:
            select = 0
        self.__root = children[select]
        self.__root.setToRoot()
        # for ch in self.__root.getChildren():
        #     ch.getMetadata().print()

    def findOptimalMove(self) -> int:
        maxIndex = 0
        children = self.__root.getChildren()
        for index in range(len(children)):
            if children[index].getHeuristic() == 1:
                return index
        for index in range(len(children)):
            if children[index].getHeuristic() == 0:
                return index

    def declareOptimalMove(self) -> int:



    def doPlayerTurn(self):
        self.__game.promptUser()
        self.__followGame()

    def doComputerTurn(self):
        move = self.findOptimalMove()
        self.__root.printImmediateChildren()
        self.__game.doTurn(move)
        self.__followGame()

    def __alternateTurn(self):
        player = self.__game.whichPlayer()
        if player == 1:
            return "doPlayerTurn"
        else:
            return "doComputerTurn"

    def playGame(self):
        while not self.__game.isGameOver():
            playerCall = self.__alternateTurn()
            getattr(self, playerCall)()



def main():
    mini = MiniMax()
    mini.playGame()

if __name__ == "__main__":
    main()