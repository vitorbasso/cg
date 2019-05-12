import pygame, sys, colors, bresenham, square, rectangle, settings, drawings

#Armazena os objetos permanentes na tela
toDraw = []

#escolhe qual o tipo do desenho - linha, retangulo, quadrado
drawMethod = bresenham.drawLine
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
starting_pos = (0,0)
last_pos = (0,0)
ending_pos = (0,0)
late_pos = (0,0)
ctrl = False

#Seta os pixels nas posições especificadas em toDraw para serem pintados
def draw():
    for drawing in toDraw:
        for pixel in drawing.getPos():
            gameDisplay.set_at(pixel, settings.DRAW_COLOR)

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
        #Quando pressionar botão esquerdo do mouse, pega a posição inicial e seta a variável pressed como true
        elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
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
        #Enquanto o botão esquerdo estiver setado como pressed, quando o mouse mexer, calcular como a figura resultante seria naquela posição e mostrar na tela
        elif event.type == pygame.MOUSEMOTION and pressed:
            late_pos = last_pos
            last_pos = pygame.mouse.get_pos()
            gameDisplay.fill(settings.BACKGROUND_COLOR)
            for pixel in drawMethod(starting_pos, last_pos):
                gameDisplay.set_at(pixel, settings.DRAW_COLOR)
            draw()
            show(starting_pos, last_pos)
        #Atalhos de teclado para mudar a geometria a ser desenhada - 1 linha 2 retangulo 3 quadrado
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                drawMethod = bresenham.drawLine
                locationMethod = rectangle.getLocationRectangle
            elif event.key == pygame.K_2:
                drawMethod = rectangle.drawRectangle
                locationMethod = rectangle.getLocationRectangle
            elif event.key == pygame.K_3:
                drawMethod = square.drawSquare
                locationMethod = square.getLocationSquare
            #Famoso ctrl + z nao quer funcionar de jeito nenhum essa bagaca
            elif event.key == pygame.K_z and pygame.key.get_mods() & pygame.KMOD_CTRL and len(toDraw) > 0:
                del toDraw[-1]
                gameDisplay.fill(settings.BACKGROUND_COLOR)
                draw()
                showAll()
            elif event.key == pygame.K_a:
                print(toDraw[0].getPoint())



        
    if pygame.mouse.get_pressed()[2]:
        gameDisplay.fill(settings.BACKGROUND_COLOR)
        toDraw = []
        showAll()

    clock.tick(144)

pygame.quit()
quit()