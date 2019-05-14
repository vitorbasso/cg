import bresenham, settings

SPECIAL_TYPE = "fill"
toDraw = []

def getToDraw(toD):
    global toDraw
    toDraw = toD


def drawFill(_, ending_pos):
    jumpLine = False
    jumpCol = False
    finished = False
    (x, y) = ending_pos
    (width, height) = settings.SCREEN_DIMENSION

    while not finished:
        jumpCol = False
        i = y
        while i < height and not jumpCol:
            jumpLine = False
            j = x
            while ( j < width and not jumpLine):
                pixel = (j, i)
                for drawing in toDraw:
                    if pixel in drawing.getPos():
                        jumpLine = True
                        if pixel[1] == y:
                            jumpCol = True
                        if pixel == (x,y):
                            finished = True
                        y += 1
                if not jumpLine:
                    yield pixel
                j += 1
            i += 1

    finished = False
    jumpLine = False
    jumpCol = False
    
    (x, y) = ending_pos

    while not finished:
        jumpCol = False
        i = y
        while i > 0 and not jumpCol:
            jumpLine = False
            j = x
            while ( j > 0 and not jumpLine):
                pixel = (j, i)
                for drawing in toDraw:
                    if pixel in drawing.getPos():
                        jumpLine = True
                        if pixel[1] == y:
                            jumpCol = True
                        if pixel == (x,y):
                            finished = True
                        y -= 1
                if not jumpLine:
                    yield pixel
                j -= 1
            i -= 1

    finished = False
    jumpLine = False
    jumpCol = False
    
    (x, y) = ending_pos

    while not finished:
        jumpCol = False
        i = y
        while i > 0 and not jumpCol:
            jumpLine = False
            j = x
            while ( j < width and not jumpLine):
                pixel = (j, i)
                for drawing in toDraw:
                    if pixel in drawing.getPos():
                        jumpLine = True
                        if pixel[1] == y:
                            jumpCol = True
                        if pixel == (x,y):
                            finished = True
                        y -= 1
                if not jumpLine:
                    yield pixel
                j += 1
            i -= 1

    finished = False
    jumpLine = False
    jumpCol = False
    
    (x, y) = ending_pos

    while not finished:
        jumpCol = False
        i = y
        while i < height and not jumpCol:
            jumpLine = False
            j = x
            while ( j > 0 and not jumpLine):
                pixel = (j, i)
                for drawing in toDraw:
                    if pixel in drawing.getPos():
                        jumpLine = True
                        if pixel[1] == y:
                            jumpCol = True
                        if pixel == (x,y):
                            finished = True
                        y += 1
                if not jumpLine:
                    yield pixel
                j -= 1
            i += 1