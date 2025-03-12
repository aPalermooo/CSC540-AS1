from typing import Optional


'''--- CONSTANTS ---'''
LEFT = False            #"bit" representation of direction
RIGHT = True
CANNIBAL = 'C'          #"char" representation of actor type
MISSIONARY = 'M'
'''-----------------'''

class State:

    def __distributeActors(self) -> None:
        """
        distributes all actor "objects" to their metaphorical side of the river, having these obejects allows for easier visualization of the problem
        while working on a solution
        :return: None
        """
        self.__cannibalsLeft = ([CANNIBAL for bit in self.__cannibalsState if bit == LEFT])
        self.__cannibalsRight = ([CANNIBAL for bit in self.__cannibalsState if bit == RIGHT])
        self.__missionariesLeft = ([MISSIONARY for bit in self.__missionariesState if bit == LEFT])
        self.__missionariesRight = ([MISSIONARY for bit in self.__missionariesState if bit == RIGHT])

    def __adjustState(self) -> None:
        """
        Updates the states such that the state now reflects the placement of the actors
        :return: None
        """
        self.__cannibalsState.clear()
        self.__missionariesState.clear()
        self.__cannibalsState = [LEFT for _ in self.__cannibalsLeft]
        self.__cannibalsState += [RIGHT for _ in self.__cannibalsRight]

        self.__missionariesState = [LEFT for _ in self.__missionariesLeft]
        self.__missionariesState += [RIGHT for _ in self.__missionariesRight]


    def __init__(self, cannibalsState : list[bool] = None,
                 boatState : bool = None,
                 missionariesState : list[bool] = None):
        """
        Sets up the positioning of all the "actors"/pieces of the problem
        :param cannibalsState:      The state as of which side of the river each of the 3 cannibals are on
        :param boatState:           The state as of which side of the river the boat is on
        :param missionariesState:   The state as of which side of the river each of the 3 missionaries are on
        """
        if cannibalsState is None:
            cannibalsState = [LEFT, LEFT, LEFT]
        if boatState is None:
            boatState = LEFT
        if missionariesState is None:
            missionariesState = [LEFT, LEFT, LEFT]

        '''Binary Encoding'''
        self.__cannibalsState : list[bool] = cannibalsState
        self.__boatState : bool = boatState
        self.__missionariesState : list[bool] = missionariesState

        '''Object Representation'''
        self.__cannibalsLeft : list[str] = []
        self.__cannibalsRight : list[str] = []

        self.__boat : list[str] = []

        self.__missionariesLeft : list[str] = []
        self.__missionariesRight : list[str] = []

        self.__distributeActors()


    '''--- Getter Methods ---'''
    def checkCannibals(self) -> list[bool]:
        return self.__cannibalsState

    def checkMissionaries(self) -> list[bool]:
        return self.__missionariesState

    def isBoatOnLeft(self) -> bool:
        """
        A helper function that allows to check for the positioning of the boat
        :return: true if the boat is on the left side of the river, false if it is on the right side
        """
        return not self.__boatState
    '''----------------------'''


    def isTerminalState(self) -> int:
        """
        Evaluates a handful of conditions of the distribution of the actors to determine if it is a terminal state
        :return: 1 if state is a successful terminal state, -1 if state is a failure terminal state, 0 if state is not a terminal state
        """
        if ( len(self.__cannibalsRight) == 3 and            #Victory Condition
            len(self.__missionariesRight) == 3 ):
            return 1

        if len(self.__cannibalsLeft) > len(self.__missionariesLeft):    #Failure, Cannibal eats missionary
            return -1
        if len(self.__cannibalsRight) > len(self.__missionariesRight):  #Failure, Cannibal eats missionary
            return -1

        if len(self.__missionariesLeft) == 0 and len(self.__cannibalsLeft) > 1:     #Failure, Cannibals eats each other
            return -1
        if len(self.__missionariesRight) == 0 and len(self.__cannibalsRight) > 1:   #Failure, Cannibals eats each other
            return -1

        return 0            #No Goal is meet yet

    def printState(self) -> None:
        """
        Allows for debug operations and visualization of where the actors are in a given moment in time
        :return: None
        """

        print(self.__cannibalsLeft, end = "")       #Cannibals on Left

        if self.isBoatOnLeft():                     #Boat
            print("\tB",end="\t\t\t")               #
        else:                                       #
            print("\t\t\tB",end="\t")               #

        print(self.__cannibalsRight, end = "")      #Cannibals on Right

        print()

        print(self.__missionariesLeft, end = "")    #Missionaries on Right
        print("\t\t\t\t",end="")
        print(self.__missionariesRight, end = "")   #Missionaries on Left
        print()
        print()

    def isValidMove(self, actor1 : bool, actor2 : Optional[bool]) -> bool:
        """
        Checks if the requested move is valid or not with the position of the actors and the parameters given
        :pre: actor1 and actor2 can only be CANNIBAL or MISSIONARY
        :param actor1: The Actor type to be transferred across river **MUST BE FILLED*
        :param actor2: The Actor type to be transferred across the river **CAN BE NONE**
        :return: True if valid move is proposed, False if the move proposed is invalid
        """
        if actor1 is not CANNIBAL or actor1 is not MISSIONARY:                          #Checks if the parameters typed correctly
            return False
        if actor2 is not CANNIBAL or actor2 is not MISSIONARY or actor2 is not None:
            return False

        if self.isBoatOnLeft():                             #Decide from what side of the river the boat is loading from
            sourceCannibals = self.__cannibalsLeft
            sourceMissionaries = self.__missionariesLeft
        else:
            sourceCannibals = self.__cannibalsRight
            sourceMissionaries = self.__missionariesRight

        numCannibalsRequested = 0                           #Count number of each actor type requested
        numMissionariesRequested = 0

        if actor1 is CANNIBAL:
            numCannibalsRequested += 1
        else:
            numMissionariesRequested += 1

        if actor2 is CANNIBAL:
            numCannibalsRequested += 1
        elif actor2 is MISSIONARY:
            numMissionariesRequested += 1

        return (len(sourceCannibals) >= numCannibalsRequested) and (len(sourceMissionaries) >= numMissionariesRequested)

    def __loadBoat(self, actor1 : bool, actor2 : Optional[bool]) -> None:
        """
        Removes actors from their side of the river and adds them into the boat object
        :pre: actor1 and actor2 can only be CANNIBAL or MISSIONARY
        :param actor1: The Actor type to be transferred across river **MUST BE FILLED*
        :param actor2: The Actor type to be transferred across the river **CAN BE NONE**
        :return: None
        """
        if self.isBoatOnLeft():                             #Decide from what side of the river the boat is loading from
            sourceCannibals = self.__cannibalsLeft
            sourceMissionaries = self.__missionariesLeft
        else:
            sourceCannibals = self.__cannibalsRight
            sourceMissionaries = self.__missionariesRight

        if actor1 is CANNIBAL:                              #Place first actor on boat
            self.__boat.append(sourceCannibals.pop())
        else:
            self.__boat.append(sourceMissionaries.pop())

        if actor2 is CANNIBAL:                              #Place second actor on boat
            self.__boat.append(sourceCannibals.pop())
        elif actor2 is MISSIONARY:
            self.__boat.append(sourceMissionaries.pop())

    def __sailBoat(self) -> bool:
        """
        Moves boat from one side of the river to the other
        Simulates taking its passengers across the river
        :pre: an actor is in the boat to move it across the river
        :return: False if the boat does not have an occupant to move it
        """
        if not self.__boat:
            return False        #Empty
        if self.isBoatOnLeft():
            self.__boatState = RIGHT
        else:
            self.__boatState = LEFT
        return True

    def __unloadBoat(self) -> None:
        """
        Removes actors from boat and places them on back on the side of the river of the boat
        :return: None
        """
        if not self.__boat:     #Boat is already empty
            return

        if self.isBoatOnLeft():                             #Decide from what side of the river the boat is offloading to
            sourceCannibals = self.__cannibalsLeft
            sourceMissionaries = self.__missionariesLeft
        else:
            sourceCannibals = self.__cannibalsRight
            sourceMissionaries = self.__missionariesRight

        while self.__boat:
            actor = self.__boat.pop()
            if actor is CANNIBAL:
                sourceCannibals.append(actor)
            else:                                           #Clean Pantry: We do not need to check for None
                sourceMissionaries.append(actor)


        self.__boat.clear()                                 #Remove Actors from boat

    def doTurn(self, actor1 : bool, actor2 : Optional[bool] = None) -> Optional[object]:
        """
        Completes a whole turn of loading the boat, moving the boat across the river, and placing the occupants on the other side
        :param actor1: The Actor type to be transferred across river **MUST BE FILLED*
        :param actor2: The Actor type to be transferred across the river **CAN BE NONE**
        :return: a copy of the state object with the transaction completed
        """
        if not self.isValidMove(actor1, actor2):
            return None

        copy = State(self.__cannibalsState, self.__boatState, self.__missionariesState)

        copy.__loadBoat(actor1, actor2)
        copy.__sailBoat()
        copy.__unloadBoat()
        copy.__adjustState()
        return copy


def main():
    state = State()
    state.printState()

if __name__ == "__main__":
    main()