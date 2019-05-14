import settings

SPECIAL_TYPE = "fill"
pixels = []
toFill = []
(width, height) = settings.SCREEN_DIMENSION
left = False
right = False
up = False
down = False


def getToDraw(toDraw):
    global pixels
    for drawing in toDraw:
        for pixel in drawing.getPos():
            pixels.append(pixel)

def getNeighbours(firstPixel):
    global width
    global height
    global pixels
    global toFill
    global left
    global right
    global up
    global down
    pixel = firstPixel
    hasMore = True
    searched = []
    index = 0
    

    toFill.append(firstPixel)

    

    while hasMore:
        left = False
        right = False
        up = False
        down = False
        (x0, y0) = pixel
        searched.append(pixel)
        if (x0, y0 - 1) in pixels:
            up = True
        if (x0 - 1, y0) in pixels:
            left = True
        if (x0, y0 + 1) in pixels:
            down = True
        if (x0 + 1, y0) in pixels:
            right = True
     
        if x0 + 1 < width and not (x0 + 1, y0) in pixels and not (x0 + 1, y0) in toFill:
            toFill.append((x0, y0))
        if y0 + 1 < height and not (x0, y0 + 1) in pixels and not (x0, y0 + 1) in toFill:
            toFill.append((x0, y0 + 1))      
        if x0 - 1 > settings.CANVAS_START_AT and not (x0 - 1, y0) in pixels and not (x0 - 1, y0) in toFill:
            toFill.append((x0 - 1, y0))      
        if y0 - 1 >= 0 and not (x0, y0 - 1) in pixels and not (x0, y0 - 1) in toFill:
            toFill.append((x0, y0 - 1))       
        if  x0 + 1 < width and y0 + 1 < height and not (x0 + 1, y0 + 1) in pixels and not (x0 + 1, y0 + 1) in toFill and not (right and down):
            toFill.append((x0 + 1, y0 + 1))
        if x0 - 1 >= settings.CANVAS_START_AT and y0 - 1 > 0 and not (x0 - 1, y0 - 1) in pixels and not (x0 - 1, y0 - 1) in toFill  and not (left and up):
            toFill.append((x0 - 1, y0 - 1))
        if x0 + 1 < width and y0 - 1 > 0 and not (x0 + 1, y0 - 1) in pixels and not (x0 + 1, y0 - 1) in toFill and not (right and up):
            toFill.append((x0 + 1, y0 - 1))
        if x0 - 1 >= settings.CANVAS_START_AT and y0 + 1 < height and not (x0 - 1, y0 + 1) in pixels and not (x0 - 1, y0 + 1) in toFill  and not (left and down):
            toFill.append((x0 - 1, y0 + 1))


        hasMore = False
        while (toFill[index] in searched and index + 1 < len(toFill)):
            index += 1
        if not toFill[index] in searched:
            hasMore = True
            pixel = toFill[index]


def drawFill(_, ending_pos):
    global pixels
    global toFill
    firstPixel = ending_pos
    getNeighbours(firstPixel)

    while(len(toFill) > 0):
        yield toFill.pop()
  