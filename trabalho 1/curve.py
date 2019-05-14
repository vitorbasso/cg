import line, numpy

SPECIAL_TYPE = "curve"
starting_pos = (0,0)
ending_pos = (0,0)
first_control = (0,0)

def drawCurve(starting_pos1, ending_pos1):
    global starting_pos
    global ending_pos
    starting_pos = starting_pos1
    ending_pos = ending_pos1
    for pixel in bezierCurve(starting_pos, starting_pos, ending_pos, ending_pos):
        yield pixel
    
    

def getFirstControl(_, first_control1):
    global starting_pos
    global ending_pos
    global first_control
    first_control = first_control1
    for pixel in bezierCurve(starting_pos, starting_pos, first_control, ending_pos):
        yield pixel


def getSecondControl(_, second_control):
    global starting_pos
    global ending_pos
    global first_control
    for pixel in bezierCurve(starting_pos, second_control, first_control, ending_pos):
        yield pixel

def bezierCurve(starting_pos,first_control,second_control,ending_pos):
    anterior = (0,0)
    proximo = (0,0)

    for t in numpy.arange(0,1,0.05):
        omt = 1 - t
        omt2 = omt * omt
        omt3 = omt2 * omt
        t2 = t * t
        t3 = t2 * t
        x = omt3 * starting_pos[0] + ((3*omt2)*t*first_control[0]) + (3*omt*t2*second_control[0])+t3*ending_pos[0]
        y = omt3 * starting_pos[1] + ((3*omt2)*t*first_control[1]) + (3*omt*t2*second_control[1])+t3*ending_pos[1]
        x = int(numpy.floor(x))
        y = int(numpy.floor(y))

        if t == 0:
            anterior = (x,y)
        else:
            proximo = (x,y) 
            for pixel in line.drawLine(anterior, proximo):
                    yield pixel
            anterior = proximo

        yield anterior

def special():
    return True