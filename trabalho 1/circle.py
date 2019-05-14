import math, bresenham

def extractPoints(starting_pos, ending_pos):
    (x0, y0), (x1, y1) = starting_pos, ending_pos
    return x0, y0, x1, y1

def calculateDistance(x0, y0, x1, y1):
    return int(math.sqrt((x1-x0) ** 2 + (y1-y0) ** 2))

def times8(x, y, offsetX, offsetY):
    yield (x+offsetX, y+offsetY)
    yield (-x+offsetX, y+offsetY)
    yield (x+offsetX, -y+offsetY)
    yield (-x+offsetX, -y+offsetY)
    yield (y+offsetX, x+offsetY)
    yield (-y+offsetX, x+offsetY)
    yield (y+offsetX, -x+offsetY)
    yield (-y+offsetX, -x+offsetY)
    

def drawCircle(starting_pos, ending_pos):
    x0, y0, x1, y1 = extractPoints(starting_pos, ending_pos)
    x, y = 0, calculateDistance(x0, y0, x1, y1)
    offsetX = calculateDistance(0, y0, x0, y0)
    offsetY = calculateDistance(x0, 0, x0, y0)
    for pixel in plotCircle(x, y, y, offsetX, offsetY):
        yield pixel


def plotCircle(x, y, radius, offsetX, offsetY):
    d = 1.0 - radius

    for pixel in times8(x, y, offsetX, offsetY):
        yield pixel

    while x < y:
        if d < 0:
            x += 1
            d += 2*x + 1
        else:
            x += 1
            y -= 1
            d += 2*(x-y) + 1
        for pixel in times8(x, y, offsetX, offsetY):
            yield pixel

def special():
    return False