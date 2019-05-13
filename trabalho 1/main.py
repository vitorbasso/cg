import pygame, sys, colors, square, rectangle, settings, drawings, line, polyline

#Armazena os objetos permanentes na tela
toDraw = []
undo = []

#escolhe qual o tipo do desenho - linha, retangulo, quadrado
drawMethod = line.drawLine
#ecolhe qual o tipo de detecção da área da tela a ser refrescada
locationMethod = rectangle.getLocationRectangle


pygame.init()


gameDisplay = pygame.display.set_mode(settings.SCREEN_DIMENSION)

gameDisplay.fill(settings.BACKGROUND_COLOR)
pygame.display.update()


pygame.display.set_caption("Primeiro Trabalho de CG")

clock = pygame.time.Clock()

finished = False
pressed = False
keepDrawing = False
poly = False
starting_pos = (0,0)
last_pos = (0,0)
ending_pos = (0,0)

#Seta os pixels nas posições especificadas em toDraw para serem pintados
def draw():
    for drawing in toDraw:
        for pixel in drawing.getPos():
            gameDisplay.set_at(pixel, drawing.getColor())

#Atualiza a janela, mostrando as atualizações
def show(starting, ending):
    #pygame.display.update(pygame.Rect(locationMethod(starting, ending))) #Passando esse parametro é mais eficiente, mas gera bugs complicados de resolver
    pygame.display.update()   #Versão menos eficiente, porém que evita bugs chatos

def showAll():
    pygame.display.update()

#Loop principal
while not finished:
    for event in pygame.event.get():
        #Para fechar o programa
        if event.type == pygame.QUIT:
            finished = True
        #Reseta o canvas quando o botao direito do mouse e pressionado
        elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[2] and not poly:
            print("Reseting canvas")
            gameDisplay.fill(settings.BACKGROUND_COLOR)
            toDraw = []
            undo = []
            showAll()
        #Quando pressionar botão esquerdo do mouse, pega a posição inicial e seta a variável pressed como true
        elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            if not poly:
                starting_pos = pygame.mouse.get_pos()
                pressed = True
        #Quando soltar o botão esquerdo do mouse, pega a posição final, seta a variável pressed como false e adiciona a figura resultante no array toDraw
        elif event.type == pygame.MOUSEBUTTONUP and pressed:
            gameDisplay.fill(settings.BACKGROUND_COLOR)
            ending_pos = pygame.mouse.get_pos()
            pressed = False
            drawing = drawings.Drawing(settings.DRAW_COLOR)
            for pixel in drawMethod(starting_pos, ending_pos):
                drawing.setPos(pixel)
            toDraw.append(drawing)
            draw()
            show(starting_pos, ending_pos)
            if keepDrawing:
                poly = True
            else:
                poly = False

            if poly:
                pressed = True
                starting_pos = last_pos
            else:
                pressed = False

        #Botao do meio do mouse termina rotina de polylinha ou botao direito
        elif event.type == pygame.MOUSEBUTTONDOWN and (pygame.mouse.get_pressed()[1] or pygame.mouse.get_pressed()[2]) and poly:
            poly = False
            pressed = False
            gameDisplay.fill(settings.BACKGROUND_COLOR)
            draw()
            show(starting_pos, ending_pos)

        #Enquanto o botão esquerdo estiver setado como pressed, quando o mouse mexer, calcular como a figura resultante seria naquela posição e mostrar na tela
        elif event.type == pygame.MOUSEMOTION and pressed:
            last_pos = pygame.mouse.get_pos()
            gameDisplay.fill(settings.BACKGROUND_COLOR)
            for pixel in drawMethod(starting_pos, last_pos):
                gameDisplay.set_at(pixel, settings.DRAW_COLOR)
            draw()
            show(starting_pos, last_pos)
        #Atalhos de teclado para mudar a geometria a ser desenhada - 1 linha 2 retangulo 3 quadrado
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                print("Drawing LINE")
                drawMethod = line.drawLine
                keepDrawing = line.keepDrawing()
                locationMethod = rectangle.getLocationRectangle
            elif event.key == pygame.K_2:
                print("Drawing RECTANGLE")
                drawMethod = rectangle.drawRectangle
                keepDrawing = rectangle.keepDrawing()
                locationMethod = rectangle.getLocationRectangle
            elif event.key == pygame.K_3:
                print("Drawing SQUARE")
                drawMethod = square.drawSquare
                keepDrawing = square.keepDrawing()
                locationMethod = square.getLocationSquare
            elif event.key == pygame.K_4:
                print("Drawing POLYLINE")
                drawMethod = polyline.drawPoly
                keepDrawing = polyline.keepDrawing()
                locationMethod = square.getLocationSquare
            #Famoso ctrl + z  - undo
            elif event.key == pygame.K_z and pygame.key.get_mods() & pygame.KMOD_CTRL and len(toDraw) > 0:
                print("UNDO")
                undo.append(toDraw.pop())
                gameDisplay.fill(settings.BACKGROUND_COLOR)
                draw()
                showAll()
            #Famoso ctrl + y - redo
            elif event.key == pygame.K_y and pygame.key.get_mods() & pygame.KMOD_CTRL and len(undo) > 0:
                print("REDO")
                toDraw.append(undo.pop())
                gameDisplay.fill(settings.BACKGROUND_COLOR)
                draw()
                showAll()
            elif event.key == pygame.K_a:
                print(toDraw[0].getPoint())
        

    clock.tick(settings.REFRESH_RATE)
    #Fim do LOOP principal

pygame.quit()
quit()