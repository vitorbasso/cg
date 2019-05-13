import bresenham

SPECIAL_TYPE = "polyline"

def drawPoly(initialPos, endPos):
    for pixel in bresenham.drawLine(initialPos,endPos):
        yield pixel

def special():
    return True