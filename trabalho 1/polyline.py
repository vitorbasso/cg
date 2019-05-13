import bresenham

def drawPoly(initialPos, endPos):
    for pixel in bresenham.drawLine(initialPos,endPos):
        yield pixel

def keepDrawing():
    return True