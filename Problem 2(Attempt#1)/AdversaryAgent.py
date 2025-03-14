
from TicTacToe import Game

class Adversary:

    class Encoding:
        def __init__(self, game: Game):
            self.gameState = game.getBoardState()

            self.state = []
            for y in self.gameState:
                for x in y:
                    if x == game.PLAYER_ONE_TOKEN:
                        self.state.append(-1)
                    elif x == game.PLAYER_TWO_TOKEN:
                        self.state.append(1)
                    else:
                        self.state.append(0)

            self.winningStates = [
                [1,1,1, 0,0,0, 0,0,0], [0,0,0, 1,1,1, 0,0,0], [0,0,0, 0,0,0, 1,1,1],
                [1,0,0, 1,0,0, 1,0,0], [0,1,0, 0,1,0, 0,1,0], [0,0,1, 0,0,1, 0,0,1],
                [1,0,0, 0,1,0, 0,0,1], [0,0,1, 0,1,0, 1,0,0]
            ]

    def __init__(self, game: Game):
        self.currentGameState = self.Encoding(game)


    def trimStates(self):
        self.winningStates = [ state for state in self.winningStates
                               if all(state[i] != 1 for i, value in enumerate(self.currentGameState) if value == -1)]




def main():
    game = Game()

    #Have human player make their move
    game.doTurn(int(input()))

    #Construct




