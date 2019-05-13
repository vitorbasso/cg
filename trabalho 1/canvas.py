import pygame, colors, square, rectangle, settings, drawings, line, polyline, circle

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
keepDrawing = False
poly = False
starting_pos = (0,0)
last_pos = (0,0)
ending_pos = (0,0)

#Define qual o metodo de desenho e qual o metodo de deteccao da area na tela em que o desenho foi feito
drawMethod = line.drawLine
locationMethod = rectangle.getLocationRectangle


#Funcoes para atualizar a tela

def draw(pixel, color):
    canvas.set_at(pixel, color)

def resetScreen():
    canvas.fill(settings.BACKGROUND_COLOR)

def refreshScreen():
    pygame.display.update()

def blankScreen():
    resetScreen()
    refreshScreen()

def drawScene():
    resetScreen()
    for drawing in toDraw:
        for pixel in drawing.getPos():
            draw(pixel, drawing.getColor())

def drawAndShow():
    drawScene()
    if pressed:
        for pixel in drawMethod(starting_pos, last_pos):
            draw(pixel, settings.DRAW_COLOR)
    refreshScreen()

def resetCanvas(event):
    reset = event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[2] and not poly
    if reset:
        del toDraw[:]
        del undo[:]
        drawAndShow()
    return  reset

def endPoly(event):
    global poly
    global pressed
    end = poly and event.type == pygame.MOUSEBUTTONDOWN and (pygame.mouse.get_pressed()[2] or pygame.mouse.get_pressed()[1])
    if end:
        poly = False
        pressed = False
        drawAndShow()
    return end

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

#Fim funcoes para detectar estado

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

blankScreen()

#Loop principal
while not finished:
    for event in pygame.event.get():
        if endProgram(event):
            finished = True
        #Quando pressionar botão esquerdo do mouse, pega a posição inicial e seta a variável pressed como true
        elif leftMouseDown(event) and not poly:
            starting_pos = getMousePos()
            pressed = True
            print("Starting pos: " , starting_pos)
        #Quando soltar o botão esquerdo do mouse, pega a posição final, seta a variável pressed como false e adiciona a figura resultante no array toDraw
        elif leftMouseUp(event):
            ending_pos = getMousePos()
            pressed = False
            drawing = drawings.Drawing(settings.DRAW_COLOR)
            for pixel in drawMethod(starting_pos, ending_pos):
                drawing.setPos(pixel)
            toDraw.append(drawing)
            drawAndShow()
            print("Ending pos: " , ending_pos)
            if keepDrawing:
                poly = True
            else:
                poly = False

            if poly:
                pressed = True
                starting_pos = ending_pos
            else:
                pressed = False
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
                keepDrawing = line.keepDrawing()
                locationMethod = rectangle.getLocationRectangle
                drawAndShow() #Essa atualizacao e para caso o usuario mude o mode sem movimentar o mouse, o que nao causaria a atualizacao da tela
            elif event.key == pygame.K_2:
                print("Drawing RECTANGLE")
                drawMethod = rectangle.drawRectangle
                keepDrawing = rectangle.keepDrawing()
                locationMethod = rectangle.getLocationRectangle
                drawAndShow()
            elif event.key == pygame.K_3:
                print("Drawing SQUARE")
                drawMethod = square.drawSquare
                keepDrawing = square.keepDrawing()
                locationMethod = square.getLocationSquare
                drawAndShow()
            elif event.key == pygame.K_4:
                print("Drawing POLYLINE")
                drawMethod = polyline.drawPoly
                keepDrawing = polyline.keepDrawing()
                locationMethod = square.getLocationSquare
                drawAndShow()
            elif event.key == pygame.K_5:
                print("Drawing CIRCLE")
                drawMethod = circle.drawCircle
                keepDrawing = line.keepDrawing()
                locationMethod = square.getLocationSquare
                drawAndShow()
            #Famoso ctrl + z  - undo
            elif isCtrlZ(event) and len(toDraw) > 0:
                ctrlZ()
            #Famoso ctrl + y - redo
            elif isCtrlY(event) and len(undo) > 0:
                ctrlY()
            elif event.key == pygame.K_a: #debug
                print(toDraw[0].getPoint())







    clock.tick(settings.REFRESH_RATE)

pygame.quit()
quit()