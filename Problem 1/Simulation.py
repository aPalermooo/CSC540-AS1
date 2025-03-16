########################################
#   Name:           Simulation.py
#   Description:    AS1 : Problem 1
#                       Combines all modules and simulates the Cannibal/Missionary problem to find an optimal solution
#   Author:         Xander Palermo <ajp2s@missouristate.edu>
#   Date:           14 March 2025
#
#   Class:          CSC 540 - Introduction to Artificial Intelligence
#   Teacher:        Dr. Rahul Dubey
########################################
import heapq
from Node import Node
from State import State, Pair

MAX_SEARCH_DEPTH = 13

class Simulation:

    def __init__(self):
        self.rootNode = Node(State())
        self.__exploredNodes = set()
        self.__treeHeap : list[Node] = []
        heapq.heappush(self.__treeHeap, self.rootNode)
        self.__generateTree(self.rootNode)
        # print(self.__treeHeap)


    def __generateTree(self, node : Node) -> None:
        """
        Takes a node and expands if for all possible outcomes of actions from that state
        Also expands for all children that are generated
        :pre: node contains a State object in its MetaData
        :param node: The node to be expanded, typically the root node of a tree (such as self.rootNode)
        :return: None
        """
        possibleStates = node.getMetadata().computeAllActions()         #Generate all possibilities
        if node.getCost() >= MAX_SEARCH_DEPTH:                          #return up a level in the tree after a certain ceiling of recursion
            return
        if possibleStates is None:                                      #or if there are no possibilities from the child
            return

        for state in possibleStates:
            # print(state.getEncoding())        #dbug
            # print(self.__exploredNodes)
            if state.getEncoding() in self.__exploredNodes:  #If a node has been explored already, it is not an optimal solution
                continue                                        #Discard
            self.__exploredNodes.add(state.getEncoding())
            child = node.createChild(state)
            child.setHeuristic(state.generateHeuristic() + child.getCost())
            heapq.heappush(self.__treeHeap, child)                #Building a priority queue proactively for A*
            # if child.getCost() == 1:      #dbug
            #     print("gen")
        for ch in node.getChildren():           #Recursively build tree Top to Bottom Left to Right
            self.__generateTree(ch)

    def getOptimalPath(self) -> list[Pair]:
        """
        Finds the cheapest solution in the priority queue and traces its parents nodes to find the actions
        taken to arrive to that node
        :return: an ordered list of moves to make to get to the optimal solution
        """
        searchIndex = 0
        while searchIndex < len(self.__treeHeap):
            # print(f"{searchIndex=}")
            if self.__treeHeap[searchIndex].getMetadata().isComplete(): #is solution (take the first solution found)
                break
            searchIndex += 1

        node = self.__treeHeap[searchIndex]
        path = []
        while node.getParent() is not None:                     #Trace parent nodes to root
            path.append(node.getMetadata().getPrevAction())
            node = node.getParent()

        path.reverse()  #Reverse the path so it begins from the root node
        return path

def main():
    print("Generating Possible Solutions...")
    simulation = Simulation()
    # simulation.applyHeuristic()
    print("Tracing Optimal Solution...")
    path = simulation.getOptimalPath()

    #Log to Console
    solution = State()
    solution.printState()
    for step in path:
        step.print()
        solution = solution.doTurn(step.first,step.second)
        solution.printState()

if __name__ == "__main__":
    main()