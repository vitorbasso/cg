import settings, colors, drawings

SPECIAL_TYPE = "fill"
pixels = []
toFill = []
(width, height) = settings.SCREEN_DIMENSION
canvasStart = settings.CANVAS_START_AT
originalColor = colors.WHITE
screen = None

def getScreen(s):
    global screen
    screen = s

def getNeighbours(pixel):
    global width
    global height
    global toFill
    global originalColor
    global screen

    
    toFill.append(pixel)
    originalColor = screen.get_at((pixel))[:3]
    (r,g,b) = originalColor
    searched = []
    teste = False

    while len(toFill) > 0:
        (x,y) = toFill.pop()



        if screen.get_at((x,y))[:3] == originalColor:
            continue

        
        

        if x + 1 < width:
            toFill.append((x+1,y))
        if y + 1 < height:
            toFill.append((x,y+1))
        if x - 1 > settings.CANVAS_START_AT:
            toFill.append((x-1,y))
        if y - 1 > 0:
            toFill.append((x, y-1))
        

        
        
    


def drawFill(f, ending_pos):
    firstPixel = ending_pos
    getNeighbours(firstPixel)
    return (f, ending_pos)
  