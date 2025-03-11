class StateNode:
    def __init__(self):
        self.__stateDesc = [0,0,0,0,0,0,0]

    def __init__(self,state):
        self.__stateDesc = state

    def terminal(self):
        return all(x == 1 for x in self.__stateDesc)

    def moveRight(self, numCannibals, numMissionaries):
        curCannibals = self.__stateDesc.copy()[:2]
        curMissionaries = self.__stateDesc.copy()[4:]
        curBoat = self.__stateDesc.copy[3]

        #check if can move cannibals

        #check if can move missionaries

        #move boat

        #return copy of state




