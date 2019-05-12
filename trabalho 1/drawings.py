import colors

class Drawing:
    
    def __init__(self, color):
        self.color = color
        self.myCurves = []
    def setPos(self, pixel):
        self.myCurves.append(pixel)
    def getPos(self):
        return self.myCurves
    def getPoint(self):
        return (self.myCurves[0], self.myCurves[-1])
        