import colors, square, rectangle

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
    def getMySquare(self):
        return square.getLocationSquare(self.getPoint())
    def getMyRectangle(self):
        return rectangle.getLocationRectangle(self.getPoint())
    def setColor(self, color):
        self.color = color
    def getColor(self):
        return self.color