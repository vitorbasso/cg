import pygame, colors, square, rectangle, settings, drawings, line, polyline, circle, curve, fill

#Setando variaveis pygame
pygame.init()
canvas = pygame.display.set_mode(settings.SCREEN_DIMENSION)
pygame.display.set_caption("Primeiro Trabalho de CG")
clock = pygame.time.Clock()

#Definindo variaveis do programa
#Armazena os objetos permanentes na tela
toDraw = []
#Armazena os objetos que foram ctrl+z para possivel ctrl+y
undo = []
#Variaveis para controle
finished = False
pressed = False
specialType = settings.SPECIAL_TYPE_STANDARD
poly = False
curva = False
clickedThisOnce = []
for i in range(16):
    clickedThisOnce.append(False)
turnFill = False


curvaPhase = 2
starting_pos = (0,0)
last_pos = (0,0)
ending_pos = (0,0)
objectColor = settings.DRAW_COLOR

#Define qual o metodo de desenho e qual o metodo de deteccao da area na tela em que o desenho foi feito
drawMethod = line.drawLine

#Funcoes para atualizar a tela

def draw(pixel, color):
    canvas.set_at(pixel, color)

def resetScreen():
    canvas.fill(settings.BACKGROUND_COLOR)

def refreshScreen():
    pygame.display.update(pygame.Rect(settings.CANVAS_LOCATION(0,0)))

def blankScreen():
    resetScreen()
    pygame.display.update(pygame.Rect(settings.CANVAS_LOCATION(0,0)))

def drawScene():
    resetScreen()
    for drawing in toDraw:
        for pixel in drawing.getPos():
            draw(pixel, drawing.getColor())

def drawAndShow():
    drawScene()
    if pressed:
        for pixel in drawMethod(starting_pos, last_pos):
            draw(pixel, objectColor)
    refreshScreen()

def resetCanvas(event):
    reset = event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[2] and not poly
    if reset:
        del toDraw[:]
        del undo[:]
        drawAndShow()
    return  reset

def printMenu():
    global drawMethod
    global canvas
    global objectColor
    canvas.fill(objectColor)
    i = 0 
    for i in range(7):
        for pixel in line.drawLine((0,settings.MENU_SLICES * i),(settings.CANVAS_START_AT,settings.MENU_SLICES * i)):
                canvas.set_at(pixel, colors.WHITE)
        canvas.blit(pygame.transform.scale(pygame.image.load(settings.MENU_IMAGES[i]), (140, 65)), (5, settings.MENU_SLICES * i + 5))
    canvas.blit(pygame.transform.scale(pygame.image.load(settings.MENU_IMAGES[6]), (140, 140)), (5, settings.MENU_SLICES * i + 5))
    pygame.display.update(pygame.Rect(0,0,settings.CANVAS_START_AT, settings.SCREEN_DIMENSION[1]))

def endPoly(event):
    global poly
    global pressed
    end = poly and event.type == pygame.MOUSEBUTTONDOWN and (pygame.mouse.get_pressed()[2] or pygame.mouse.get_pressed()[1])
    if end:
        poly = False
        pressed = False
        drawAndShow()
    return end

def testFill(trash, pixel):
    global toDraw
    global last_pos
    global canvas
    toFill = []

    originalColor = canvas.get_at(pixel)[:3]

    (width, height) = settings.SCREEN_DIMENSION
    toFill.append(pixel)

    drawing = drawings.Drawing(objectColor)
    drawing.setPos(pixel)

    if not originalColor == objectColor:

        while len(toFill) > 0:
            (x,y) = toFill.pop()

            if canvas.get_at((x,y))[:3] == originalColor:
                drawing.setPos((x,y))
                canvas.set_at((x,y), objectColor)
                if x + 1 < width:
                    toFill.append((x+1, y))
                if x - 1 > settings.CANVAS_START_AT:
                    toFill.append((x-1, y))
                if y + 1 < height:
                    toFill.append((x, y + 1))
                if y - 1 > 0:
                    toFill.append((x,y-1))
            

    toDraw.append(drawing)
    yield pixel
        


def updateCurvaPhase():
    global curvaPhase
    global pressed
    global curva
    global drawMethod
    if curvaPhase == 3:
        pressed = False
        curvaPhase = 0
    if curvaPhase == 0:
        curvaPhase = 1
        drawMethod = curve.drawCurve
    elif curvaPhase == 1:
        curvaPhase = 2
        drawMethod = curve.getFirstControl
    elif curvaPhase == 2:
        curvaPhase = 3
        drawMethod = curve.getSecondControl

def getCurvaPhase():
    global curvaPhase
    return curvaPhase

def isSpecial():
    global specialType
    global poly
    global curva
    global turnFill
    if specialType == polyline.SPECIAL_TYPE:
        poly = True
    else:
        poly = False

    if specialType == curve.SPECIAL_TYPE:
        curva = True
    else:
        curva = False

    if specialType == "fill":
        turnFill = True
    else:
        turnFill = False

def isKeepDrawing():
    global poly
    global curva
    global pressed
    global starting_pos
    global ending_pos
    if poly or curva:
        pressed = True
        starting_pos = ending_pos
    else:
        pressed = False


#Fim funcoes para atualizar tela

#funcoes para detectar estado
def mouseDown(event):
    return event.type == pygame.MOUSEBUTTONDOWN

def leftMouseDown(event):
    return (pygame.mouse.get_pressed()[0] and mouseDown(event) and not (pygame.mouse.get_pressed()[1] or pygame.mouse.get_pressed()[2]))

def leftMouseUp(event):
    return event.type == pygame.MOUSEBUTTONUP and pressed and not pygame.mouse.get_pressed()[0]

def getMousePos():
    return pygame.mouse.get_pos()

def dragging(event):
    return (event.type == pygame.MOUSEMOTION and pressed)

def isCtrlZ(event):
    return event.key == pygame.K_z and pygame.key.get_mods() & pygame.KMOD_CTRL

def isCtrlY(event):
    return event.key == pygame.K_y and pygame.key.get_mods() & pygame.KMOD_CTRL

def endProgram(event):
    return event.type == pygame.QUIT

def isLine():
    return getMousePos()[1] < settings.MENU_SLICES

def isRectangle():
    return getMousePos()[1] > settings.MENU_SLICES and getMousePos()[1] < settings.MENU_SLICES * 2

def isSquare():
    return getMousePos()[1] > settings.MENU_SLICES * 2 and getMousePos()[1] < settings.MENU_SLICES * 3

def isPolyline():
    return getMousePos()[1] > settings.MENU_SLICES * 3 and getMousePos()[1] < settings.MENU_SLICES * 4

def isCircle():
    return getMousePos()[1] > settings.MENU_SLICES * 4 and getMousePos()[1] < settings.MENU_SLICES * 5

def isCurve():
    return getMousePos()[1] > settings.MENU_SLICES * 5 and getMousePos()[1] < settings.MENU_SLICES * 6

def isFill():
    return getMousePos()[1] > settings.MENU_SLICES * 6

#Fim de funcoes para detectar estados

#Funcoes com logica para auxiliar o programa

def resetClicks():
    global clickedThisOnce
    for i in range(16):
        clickedThisOnce[i] = False

def handleColor():
    global objectColor
    global clickedThisOnce
    global specialType
    global turnFill
    (mousePosX, mousePosY) = getMousePos()
    if mousePosX >= 12 and mousePosX <= 38 and mousePosY >= 468 and mousePosY <= 484:
        print("COR: BLACK")
        objectColor=colors.BLACK
        if not clickedThisOnce[0]:
            resetClicks()
            clickedThisOnce[0] = True
            turnFill = False   
        else:
            clickedThisOnce[0] = False
            turnFill = True
    if mousePosX >= 43 and mousePosX <= 64 and mousePosY >= 468 and mousePosY <= 484:
        print("COR: WHITE")
        objectColor=colors.WHITE
        if not clickedThisOnce[1]:
            resetClicks()
            clickedThisOnce[1] = True
            turnFill = False
        else:
            clickedThisOnce[1] = False
            turnFill = True
    if mousePosX >= 12 and mousePosX <= 38 and mousePosY >= 500 and mousePosY <= 517:
        print("COR: RED")
        objectColor=colors.RED
        if not clickedThisOnce[2]:
            resetClicks()
            clickedThisOnce[2] = True
            turnFill = False
        else:
            clickedThisOnce[2] = False
            turnFill = True
    if mousePosX >= 43 and mousePosX <= 64 and mousePosY >= 500 and mousePosY <= 517:
        print("COR: GREEN")
        objectColor=colors.GREEN
        if not clickedThisOnce[3]:
            resetClicks()
            clickedThisOnce[3] = True
            turnFill = False
        else:
            clickedThisOnce[3] = False
            turnFill = True
    if mousePosX >= 12 and mousePosX <= 38 and mousePosY >= 533 and mousePosY <= 549:
        print("COR: BLUE")
        objectColor=colors.BLUE
        if not clickedThisOnce[4]:
            resetClicks()
            clickedThisOnce[4] = True
            turnFill = False
        else:
            clickedThisOnce[4] = False
            turnFill = True
    if mousePosX >= 43 and mousePosX <= 64 and mousePosY >= 533 and mousePosY <= 549:
        print("COR: ORANGE")
        objectColor=colors.ORANGE
        if not clickedThisOnce[5]:
            resetClicks()
            clickedThisOnce[5] = True
            turnFill = False
        else:
            clickedThisOnce[5] = False
            turnFill = True
    if mousePosX >= 12 and mousePosX <= 38 and mousePosY >= 564 and mousePosY <= 581:
        print("COR: MAGENTA")
        objectColor=colors.MAGENTA
        if not clickedThisOnce[6]:
            resetClicks()
            clickedThisOnce[6] = True
            turnFill = False
        else:
            clickedThisOnce[6] = False
            turnFill = True
    if mousePosX >= 43 and mousePosX <= 64 and mousePosY >= 564 and mousePosY <= 581:
        print("COR: YELLOW")
        objectColor=colors.YELLOW
        if not clickedThisOnce[7]:
            resetClicks()
            clickedThisOnce[7] = True
            turnFill = False
        else:
            clickedThisOnce[7] = False
            turnFill = True
    if mousePosX >= 87 and mousePosX <= 108 and mousePosY >= 468 and mousePosY <= 484:
        print("COR: PURPLE")
        objectColor=colors.PURPLE
        if not clickedThisOnce[8]:
            resetClicks()
            clickedThisOnce[8] = True
            turnFill = False
        else:
            clickedThisOnce[8] = False
            turnFill = True
    if mousePosX >= 113 and mousePosX <= 133 and mousePosY >= 468 and mousePosY <= 484:
        print("COR: SILVER")
        objectColor=colors.SILVER
        if not clickedThisOnce[9]:
            resetClicks()
            clickedThisOnce[9] = True
            turnFill = False
        else:
            clickedThisOnce[9] = False
            turnFill = True
    if mousePosX >= 87 and mousePosX <= 108 and mousePosY >= 500 and mousePosY <= 517:
        print("COR: GRAY")
        objectColor=colors.GRAY
        if not clickedThisOnce[10]:
            resetClicks()
            clickedThisOnce[10] = True
            turnFill = False
        else:
            clickedThisOnce[10] = False
            turnFill = True
    if mousePosX >= 113 and mousePosX <= 133 and mousePosY >= 500 and mousePosY <= 517:
        print("COR: BROWN")
        objectColor=colors.BROWN
        if not clickedThisOnce[11]:
            resetClicks()
            clickedThisOnce[11] = True
            turnFill = False
        else:
            clickedThisOnce[11] = False
            turnFill = True
    if mousePosX >= 87 and mousePosX <= 108 and mousePosY >= 533 and mousePosY <= 549:
        print("COR: PINKER")
        objectColor=colors.PINKER
        if not clickedThisOnce[12]:
            resetClicks()
            clickedThisOnce[12] = True
            turnFill = False
        else:
            clickedThisOnce[12] = False
            turnFill = True
    if mousePosX >= 113 and mousePosX <= 133 and mousePosY >= 533 and mousePosY <= 549:
        print("COR: TEAL")
        objectColor=colors.TEAL
        if not clickedThisOnce[13]:
            resetClicks()
            clickedThisOnce[13] = True
            turnFill = False
        else:
            clickedThisOnce[13] = False
            turnFill = True
    if mousePosX >= 87 and mousePosX <= 108 and mousePosY >= 564 and mousePosY <= 581:
        print("COR: OLIVE")
        objectColor=colors.OLIVE
        if not clickedThisOnce[14]:
            resetClicks()
            clickedThisOnce[14] = True
            turnFill = False
        else:
            clickedThisOnce[14] = False
            turnFill = True
    if mousePosX >= 113 and mousePosX <= 133 and mousePosY >= 564 and mousePosY <= 581:
        print("COR: PINK")
        objectColor=colors.PINK
        if not clickedThisOnce[15]:
            resetClicks()
            clickedThisOnce[15] = True
            turnFill = False
        else:
            clickedThisOnce[15] = False
            turnFill = True

def isMenu():
    global drawMethod
    global specialType
    global curvaPhase
    global clickedThisOnce
    global canvas
    if getMousePos()[0] < settings.CANVAS_START_AT:
        if isLine():
            print("Drawing LINE")
            drawMethod = line.drawLine
            specialType = settings.SPECIAL_TYPE_STANDARD
            drawAndShow()
            return True
        elif isRectangle():
            print("Drawing RECTANGLE")
            drawMethod = rectangle.drawRectangle
            specialType = settings.SPECIAL_TYPE_STANDARD
            drawAndShow()
            return True
        elif isSquare():
            print("Drawing SQUARE")
            drawMethod = square.drawSquare
            specialType = settings.SPECIAL_TYPE_STANDARD
            drawAndShow()
            return True
        elif isPolyline():
            print("Drawing POLYLINE")
            drawMethod = polyline.drawPoly
            specialType = polyline.SPECIAL_TYPE
            drawAndShow()
            return True
        elif isCircle():
            print("Drawing CIRCLE")
            drawMethod = circle.drawCircle
            specialType = settings.SPECIAL_TYPE_STANDARD
            drawAndShow()
            return True
        elif isCurve():
            print("Drawing CURVE")
            drawMethod = curve.drawCurve
            specialType = curve.SPECIAL_TYPE
            curvaPhase = 1
            drawAndShow()
            return True
        elif isFill():
            handleColor()
            printMenu()
            if turnFill:
                print("Drawing COLOR FILL")
                #drawMethod = fill.drawFill            
                #fill.getToDraw(toDraw)
                drawMethod = testFill
                specialType = fill.SPECIAL_TYPE
                drawAndShow()
            return True
        else:
            return False

#Fim funcoes com logica para auxiliar o programa

#Funcoes extras

def ctrlZ():
    print("UNDO")
    undo.append(toDraw.pop())
    drawAndShow()

def ctrlY():
    print("REDO")
    toDraw.append(undo.pop())
    drawAndShow()


#Fim funcoes extras

printMenu()
blankScreen()


#Loop principal
while not finished:
    for event in pygame.event.get():
        if endProgram(event):
            finished = True
        #Quando pressionar botão esquerdo do mouse, pega a posição inicial e seta a variável pressed como true
        elif leftMouseDown(event):
            if isMenu():
                None
            elif not poly:
                starting_pos = getMousePos()
                if starting_pos[0] > settings.CANVAS_START_AT:
                    pressed = True
                    print("Starting pos: " , starting_pos)
        #Quando soltar o botão esquerdo do mouse, pega a posição final, seta a variável pressed como false e adiciona a figura resultante no array toDraw
        elif leftMouseUp(event):
            ending_pos = getMousePos()
            pressed = False
            isSpecial()

            if not curva or getCurvaPhase()==3:
                drawing = drawings.Drawing(objectColor)
                for pixel in drawMethod(starting_pos, ending_pos):
                    drawing.setPos(pixel)
                toDraw.append(drawing)
                drawAndShow()
                
            print("Ending pos: " , ending_pos)
            

            isKeepDrawing()

            if curva:
                updateCurvaPhase()

        #Enquanto o botão esquerdo estiver setado como pressed, quando o mouse mexer, calcular como a o preview da figura e mostrar na tela
        elif dragging(event):
            last_pos = getMousePos()
            drawAndShow()
        elif endPoly(event):
            print("Finished polyline")
        elif resetCanvas(event):
            print("Reseting canvas")

        #Atalhos de teclado para mudar a geometria a ser desenhada - 1 linha 2 retangulo 3 quadrado 4 polylinha
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                print("Drawing LINE")
                drawMethod = line.drawLine
                specialType = settings.SPECIAL_TYPE_STANDARD
                drawAndShow() #Essa atualizacao e para caso o usuario mude o mode sem movimentar o mouse, o que nao causaria a atualizacao da tela
            elif event.key == pygame.K_2:
                print("Drawing RECTANGLE")
                drawMethod = rectangle.drawRectangle
                specialType = settings.SPECIAL_TYPE_STANDARD
                drawAndShow()
            elif event.key == pygame.K_3:
                print("Drawing SQUARE")
                drawMethod = square.drawSquare
                specialType = settings.SPECIAL_TYPE_STANDARD
                drawAndShow()
            elif event.key == pygame.K_4:
                print("Drawing POLYLINE")
                drawMethod = polyline.drawPoly
                specialType = polyline.SPECIAL_TYPE
                drawAndShow()
            elif event.key == pygame.K_5:
                print("Drawing CIRCLE")
                drawMethod = circle.drawCircle
                specialType = settings.SPECIAL_TYPE_STANDARD
                drawAndShow()
            elif event.key == pygame.K_6:
                print("Drawing CURVE")
                drawMethod = curve.drawCurve
                specialType = curve.SPECIAL_TYPE
                curvaPhase = 1
                drawAndShow()
            elif event.key == pygame.K_7:
                print("Drawing COLOR FILL")
                drawMethod = fill.drawFill
                specialType = fill.SPECIAL_TYPE
                fill.getToDraw(toDraw)
                
            #Famoso ctrl + z  - undo
            elif isCtrlZ(event) and len(toDraw) > 0:
                ctrlZ()
            #Famoso ctrl + y - redo
            elif isCtrlY(event) and len(undo) > 0:
                ctrlY()


    clock.tick(settings.REFRESH_RATE)

pygame.quit()
quit()