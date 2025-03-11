class Actor:
    def __init__(self):
        self.onRightSide = False

class Wolf (Actor):
    def __init__(self):
        super().__init__()

class Sheep (Actor):
    def __init__(self):
        super().__init__()

class Boat:
    def __init__(self):
        return

class RiverSide:
    def __init__(self):
        self.wolves = []
        self.sheep = []

        self.boat = []