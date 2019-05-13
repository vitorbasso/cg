import line, numpy

def drawCurve(starting_pos, ending_pos):
    for pixel in line.drawLine(starting_pos, ending_pos):
        yield pixel

SPECIAL_TYPE = "curve"

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
    return False