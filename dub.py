class Dub:
    def __init__(self, name, master, growth, apple, timeZapoi):
        self.master = master
        self.growth = growth
        self.name = name
        self.apple = apple
        self.timeZapoi = timeZapoi
        with open("ogorod.txt", "a+") as ogorod:
            ogorod.writelines('\n' + f"{self.name} {self.master} {self.growth} {self.apple} {self.timeZapoi}")
    def status(self):
        return self.growth
    def updateGrowth(self):
        self.growth += 1
    def appleStatus(self):
        return self.apple