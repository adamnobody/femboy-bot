class Dub:
    def __init__(self, name):
        self.growth = 1
        self.name = name
        self.apple = 0
    def status(self):
        return self.growth
    def updateGrowth(self):
        self.growth += 1
    def appleStatus(self):
        return self.apple