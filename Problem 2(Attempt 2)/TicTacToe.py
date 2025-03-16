from Matrix import Matrix

PLAYER_ONE_TOKEN = 'X'
PLAYER_TWO_TOKEN = 'O'
BOARD_SIZE = 3

class TicTacToe:
    def __init__(self):
        self.__board = Matrix(BOARD_SIZE)
        self.__nextToken = PLAYER_TWO_TOKEN
        self.__complete : bool = False

        self.__MatrixKey = Matrix(BOARD_SIZE)
        for num in range(0,9):
            x = num % BOARD_SIZE
            y = BOARD_SIZE - 1 - (num // BOARD_SIZE)
            self.__MatrixKey.setValue(num+1, x, y )

    def __getNextToken(self) -> str:
        self.__nextToken = PLAYER_TWO_TOKEN if self.__nextToken == PLAYER_ONE_TOKEN else PLAYER_ONE_TOKEN
        return self.__nextToken

    def isGameOver(self):
        return self.__complete

    def whichPlayer(self) -> int:
        if self.__nextToken == PLAYER_TWO_TOKEN:
            return 1
        else:
            return 2

    def getState(self):
        state = []
        for row in self.__board.getMatrix():
            for space in row:
                state.append(space)
        return state

    def generateHeuristic(self):
        token = self.__board.checkAll()
        if token == PLAYER_ONE_TOKEN:
            return -1
        elif token == PLAYER_TWO_TOKEN:
            return 1
        else:
            return None

    def doTurn(self, location):
        if self.__complete:                 # Game is complete, do not run function
            return int(self.__complete)
        if not 0 < location <= 9:           #Out of Bounds
            return -2

        location -= 1                                   #Calcualte coordinate position
        x = location % BOARD_SIZE
        y = BOARD_SIZE - 1 - (location // BOARD_SIZE)

        nextToken = self.__getNextToken()

        successfulPlace = self.__board.setValue(nextToken, x, y)

        if not successfulPlace:                          # Spot was occupied
            self.__getNextToken()
            return -1

        # print(self.__board.checkAll())
        self.__complete = bool( self.__board.checkAll() )
        return int(self.__complete)

    def promptUser(self):
        self.printHelp()
        print()
        self.print()
        inputIsValid = -1
        while inputIsValid < 0:
            userInput = input("Enter your next move (1-9):")
            if not userInput.isdigit():
                print("deny")
                continue
            userInput = int(userInput)
            inputIsValid = self.doTurn(userInput)

    def print(self):
        self.__board.print(fill ="_")

    def printHelp(self):
        self.__MatrixKey.print(fill = "_")

def testDoTurn():
    game = TicTacToe()
    game.print()
    testInput = [1,2,5,8,9]
    for inp in testInput:
        print()
        game.doTurn(inp)
        game.print()

def testPrompt():
    game = TicTacToe()
    while not game.isGameOver():
        game.promptUser()
    game.print()

def main():
    game = TicTacToe()
    active = 1
    while active == 1:
        game.print()
        active = game.doTurn(int(input()))
    game.print()





if __name__  == "__main__":
    testPrompt()