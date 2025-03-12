from typing import Optional


class Node:
    def __init__(self, metaData, root : object = None, parent : "Node"= None):
        #Tree Structure
        self.__root = self if root is None else root
        self.__parent = parent
        self.__children = []

        #Data to be organized in tree
        self.__metaData = metaData
        self.__heuristic = 0
        self.__cost = 0

    '''--- Getter Methods ---'''
    def getRoot(self) -> "Node":
        return self.__root

    def getParent(self) -> Optional["Node"]:
        return self.__parent

    def getMetadata(self):
        return self.__metaData

    def getChildren(self) -> list["Node"]:
        return self.__children

    def hasChildren(self) -> bool:
        return len(self.getChildren()) > 0

    def getHeuristic(self) -> int:
        return self.__heuristic

    def getCost(self) -> int:
        return self.__cost
    '''----------------------'''

    '''--- Setter Methods ---'''
    def setHeuristic(self, heuristic: int) -> None:
        """
        Sets a value/key to a give node. By default, until this function is called, all nodes have a heuristic of 0
        :param heuristic: the value to be assigned to the node
        :return: None
        """
        self.__heuristic = heuristic

    def setCost(self, cost : int) -> None:
        self.__cost = cost

    def createChild(self, metaData) -> "Node":
        """
        Create a new child in the tree structure from the node passed as self
        :param metaData: The metadata to be attached to the new child node
        :return: the child object
        """
        child = Node(metaData, root=self.getRoot(), parent=self)
        self.__children.append(child)
        child.setCost(self.getCost() + 1)
        return child
    '''-----------------------'''

    def print(self) -> None:
        """
        Debugging Tool: Prints all associated data for a node in the tree to the console
        :return: None
        """
        print("----------------")
        print(f"|{self.getMetadata()}|")
        print(f"|{self.getHeuristic()}|")
        print(f"|{self.getCost()}|")
        print("----------------")

    def printImmediateChildren(self) -> None:
        """
        Debugging Tool: Prints all associated data for each node associated as a child of the node passed on, to the console
        If node has no children, prints None in console
        :return: None
        """
        if not self.hasChildren():
            print("None")
        else:
            for child in self.getChildren():
                child.print()


def testPrintAndCreation():
    root = Node(0)
    children1 = []
    for i in range(4):
        children1.append(root.createChild(i))
    root.print()
    root.printImmediateChildren()

    child2 = children1[0].createChild(5)
    child2.setHeuristic(3)
    child2.print()




if __name__ == "__main__":
    testPrintAndCreation()