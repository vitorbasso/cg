import bresenham


def getLocationRectangle(initialPos, endPos):
    (x0, y0), (x1, y1) = initialPos, endPos
    biggerX, smallerX = biggerSmaller(x0, x1)
    biggerY, smallerY = biggerSmaller(y0, y1)
    
    return smallerX, smallerY, biggerX, biggerY

def biggerSmaller(x, y):
    bigger = x if x > y else y
    smaller = y if x > y else x
    return bigger, smaller

def drawRectangle(initialPos, endPos):
    (x0, y0), (x1, y1) = initialPos, endPos
    secondPos = (x0, y1)
    thirdPos = (x1, y0)

    for pixel in bresenham.drawLine(initialPos, secondPos):
        yield pixel
    for pixel in bresenham.drawLine(initialPos, thirdPos):
        yield pixel
    for pixel in bresenham.drawLine(secondPos, endPos):
        yield pixel
    for pixel in bresenham.drawLine(thirdPos, endPos):
        yield pixel

def keepDrawing():
    return False