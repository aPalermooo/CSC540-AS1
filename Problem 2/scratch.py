from random import randint

from TicTacToe import Game


def isTerminalState(boardState : list[list[str]], playerToken: str) -> bool:
    ##Terminal condition is reached when there exists 3 in a row of a players token anywhere on the board

    # check row for terminal condition
    for row in boardState:
        if all(space == playerToken for space in row):
            # print("row")           # Dbug
            return True

    # check columns for terminal condition
    for col in range(Game.BOARD_LENGTH):
        if all(boardState[row][col] == playerToken for row in range(Game.BOARD_LENGTH)):
            # print("col")        #Dbug
            return True

    # check L -> R Diagonal for terminal condition
    if all(boardState[space][space] == playerToken for space in range(Game.BOARD_LENGTH)):
        # print("dia")           #Dbug
        return True

    # check R -> L Diagonal for terminal condition
    x = Game.BOARD_LENGTH - 1
    y = 0
    while x >= 0:
        if not boardState[y][x] == playerToken:
            return False
        x -= 1
        y += 1
    # print("anti-dia")       #Dbug
    return True

class Node:
    def __init__(self, metadata:list[str], parent=None) -> None:
        self.metadata = metadata
        self.parent = parent
        self.children : list[Node] = []
        self.value = 0
        self.move = None

    def print(self, height : int = 0) -> None:
        print(f"{height=}")
        print(self.metadata)
        print(f"{self.value=}")
        print([child.metadata[0:3] for child in self.children])
        print([child.metadata[3:6] for child in self.children])
        print([child.metadata[6:9] for child in self.children])


        if not self.hasNoChildren():
            for child in self.children:
                child.print(height=height+1)
        else:
            print("-"*50)

    def printImmediateChildren(self) -> None:
        print([child.metadata[0:3] for child in self.children])
        print([child.metadata[3:6] for child in self.children])
        print([child.metadata[6:9] for child in self.children])
        print([(str(child.value) + "\t") for child in self.children])
        print([(str(child.move) + "\t") for child in self.children])

    def getParent(self):
        return self.parent

    def getChildren(self):
        return self.children

    def hasNoChildren(self) -> bool:
        return len(self.children) == 0

    def addChild(self,metadata):
        newChild = Node(metadata, parent=self)
        self.children.append(newChild)
        return newChild

    def travel(self):
        self.parent = None
        return self

def expandTree(root :Node, origin: list[str], expansionVal = Game.PLAYER_ONE_TOKEN) -> Node:
    for index in range(len(origin)):
        if origin[index] == Game.BLANK:
            childData = origin.copy()
            childData[index] = expansionVal

            child = root.addChild(childData)
            child.move = index+1

            gameState = [child.metadata[0:3],child.metadata[3:6],child.metadata[6:9]]
            if isTerminalState(gameState,expansionVal):
                if expansionVal == Game.PLAYER_ONE_TOKEN:
                    child.value = -1
                else:
                    child.value = 1
                continue

            if expansionVal == Game.PLAYER_ONE_TOKEN:
                expandTree(child, child.metadata, expansionVal=Game.PLAYER_TWO_TOKEN)
            else:
                expandTree(child,child.metadata, expansionVal=Game.PLAYER_ONE_TOKEN)
    return root

def populateValue(root :Node, alpha = float('-inf'), beta = float('inf'), maximizingOn = False):
    if not root.hasNoChildren():
        values = []
        for child in root.children:
            values.append(populateValue(child,alpha,beta,not maximizingOn))
            # for index, value in enumerate(values):
                # if value == 2:
                #     values[index] = 1
                # elif value == -2:
                #     values[index] = -1

            if maximizingOn:
                alpha = max(alpha,values[-1])
            else:
                beta = min(beta,values[-1])
            if beta <= alpha:
                break

        if maximizingOn:
            root.value = alpha
        else:
            root.value = beta
    return root.value

def trimTree(root: Node, trimState: list[str]):
    for child in root.children:
        if child.metadata == trimState:
            return child.travel()

def decideMove(root) -> int:
    bestAction = max([child.value for child in root.children])

    reasonableActions = [child for child in root.children if child.value == bestAction]

    if len(reasonableActions) != 1:
        selectIndex = randint(0,len(reasonableActions)-1)
        return reasonableActions[selectIndex].move
    else:
        return reasonableActions[0].move




def main():
    #Initiate Game
    game = Game()


    #Populate the State Space
    origin = [Game.BLANK] * (Game.BOARD_LENGTH * Game.BOARD_LENGTH)
    root = Node(origin)
    expandTree(root, origin)
    populateValue(root)

    # Make Move and Adjust tree to State Space
    while not isTerminalState(game.getBoardStateDep(),game.getLastPlayerToken()):
        if game.isPlayerOneTurn():
            game.printBoardState()
            game.doTurn(int(input()))
        else:
            game.doTurn(decideMove(root))
        root = trimTree(root,game.getBoardState())
        populateValue(root,maximizingOn=not game.isPlayerOneTurn())
        # root.printImmediateChildren()



if __name__ == "__main__":
    main()
