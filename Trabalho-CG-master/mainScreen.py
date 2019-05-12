import sys

from button import Button
from bresenham import bresenham
import pygame

Display_Width = 800
Display_Height = 600

pygame.init()
screen = pygame.display.set_mode((Display_Width, Display_Height))
screen.fill((255, 255, 255))
pygame.font.init()
font = pygame.font.SysFont('Russo One', 23)
lineColor = (0, 0, 0, 255)


def printMousePos():
    running = True
    while running:
        printEvent = pygame.event.poll()

        if printEvent.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif printEvent.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, (192, 192, 192), (680, 20, 120, 30), 0)
            text = font.render(str(printEvent.pos), True, (0, 0, 0))

            screen.blit(text, (690, 25))
        pygame.display.update()


def colorLine(start, end):
    (x0, y0) = start
    (x1, y1) = end
    line = tuple(bresenham(x0, y0, x1, y1))
    for pixel in line:
        screen.set_at(pixel, lineColor)


def drawBresenham(resetButton):
    lineStart = 0
    lineEnd = 0
    run = True
    while run:
        for bresenhamEvent in pygame.event.get():
            if bresenhamEvent.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if bresenhamEvent.type == pygame.MOUSEBUTTONDOWN:
                if resetButton.isOver(pygame.mouse.get_pos()):
                    return
                lineStart = pygame.mouse.get_pos()
            if bresenhamEvent.type == pygame.MOUSEBUTTONUP and lineStart:
                lineEnd = pygame.mouse.get_pos()

        if lineStart != 0 and lineEnd != 0:
            colorLine(lineStart, lineEnd)
            lineStart = 0
            lineEnd = 0

        pygame.display.flip()


def drawSpline():
    print('no function for Spline yet')


def drawBezier():
    print('no function for Bezier yet')


def drawButtons():
    dark_gray = (140, 140, 140)
    bresenhamButton = Button(dark_gray, 64, 540, 120, 40, "Bresenham")
    bresenhamButton.draw(screen)

    bezierButton = Button(dark_gray, 248, 540, 120, 40, "Bezier")
    bezierButton.draw(screen)

    splineButton = Button(dark_gray, 432, 540, 120, 40, "Spline")
    splineButton.draw(screen)

    resetButton = Button(dark_gray, 616, 540, 120, 40, "Reset")
    resetButton.draw(screen)

    return bresenhamButton, bezierButton, splineButton, resetButton


def reset():
    screen.fill((255, 255, 255))
    return drawButtons()


if __name__ == '__main__':

    bresenhamBtn, bezierBtn, splineBtn, resetBtn = reset()
    pygame.display.update()
    while True:
        reset()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bresenhamBtn.isOver(pygame.mouse.get_pos()):
                    drawBresenham(resetBtn)

                if bezierBtn.isOver(pygame.mouse.get_pos()):
                    drawBezier()

                if splineBtn.isOver(pygame.mouse.get_pos()):
                    drawSpline()
