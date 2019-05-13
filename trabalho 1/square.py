import rectangle

def getSquare(initialPos, endPos):
    (x0, y0) , (x1, y1) = initialPos, endPos

    dx = abs(x1 - x0)
    dy = abs(y0 - y1)

    if dx > dy:
        if y0 > y1:
            y1 = y0 - dx
        else:
            y1 = y0 + dx
    else:
        if x0 > x1:
            x1 = x0 - dy
        else:
            x1 = x0 + dy
    return (x0, y0), (x1, y1)


def biggerSmaller(x, y):
    bigger = x if x > y else y
    smaller = y if x > y else x
    return bigger, smaller


def getLocationSquare(initialPos, endPos):
    (x0, y0) , (x1, y1) = getSquare(initialPos, endPos)

    x0, x1 = biggerSmaller(x0,x1)
    y0, y1 = biggerSmaller(y0,y1)
    return x1, y1, x0, y0

def drawSquare(initialPos, endPos):
    (x0, y0) , (x1, y1) = getSquare(initialPos, endPos)
    
    for pixel in rectangle.drawRectangle((x0, y0), (x1, y1)):
        yield pixel

def special():
    return False