import bresenham

def drawLine(initialPos, endPos):
    for pixel in bresenham.drawLine(initialPos,endPos):
        yield pixel

def special():
    return False