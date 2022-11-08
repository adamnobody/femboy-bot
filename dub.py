class Dub:
    def __init__(self, name, creationTime):
        self.growth = 1
        self.name = name
        self.apple = 0
        self.creationTime = creationTime
        with open("ogorod.txt", "a+") as ogorod:
            ogorod.write(f"{self.name}, {self.creationTime}\n")
    def status(self):
        return self.growth
    def updateGrowth(self):
        self.growth += 1
    def appleStatus(self):
        return self.apple