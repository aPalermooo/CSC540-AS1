import copy
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

    def __expandTree (self, node):
        for index in range(1,10):
            possibleGame = copy.deepcopy(node.getMetadata())
            childExists = possibleGame.doTurn(index)
            # print(childExists)
            if childExists >= 0:
                child = node.createChild(possibleGame)
                child.setHeuristic(possibleGame.generateHeuristic())
                if child.getCost() > MAX_SEARCH:
                    return
                self.__expandTree(child)

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
        self.__root = children[select]
        self.__root.setToRoot()
        for ch in self.__root.getChildren():
            ch.getMetadata().print()

    def doPlayerTurn(self, prompt):
        self.__game.doTurn(prompt)
        self.__followGame()
        self.__game.doTurn(1)
        self.__followGame()
        self.__game.doTurn(5)
        self.__followGame()
        self.__game.doTurn(8)
        self.__followGame()
        self.__game.doTurn(7)
        self.__followGame()
        self.__root.getMetadata().print()
        for child in self.__root.getChildren():
            child.getMetadata().print()


def main():
    mini = MiniMax()
    mini.doPlayerTurn(3)

if __name__ == "__main__":
    main()