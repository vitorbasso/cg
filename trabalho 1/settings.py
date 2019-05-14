import colors, math


#Defina aqui a largura e a altura do canvas
larguraCanvas = 800
alturaCanvas = 600

#Defina o esquema de cor padrão entre os seguintes valores: 0 - (background branco, desenho preto) ou 1 - (background preto, desenho branco)
cor = 0


#Defina a taxa de atualização da tela
atualizacao = 144






#Não mexa aqui

MENU_SLICES = math.floor(alturaCanvas / 8)
CANVAS_START_AT = 2 * MENU_SLICES

MENU_IMAGES = []

MENU_IMAGES.append("images/linha.png")
MENU_IMAGES.append("images/rectangle.png")
MENU_IMAGES.append("images/square.png")
MENU_IMAGES.append("images/polyline.png")
MENU_IMAGES.append("images/circle.png")
MENU_IMAGES.append("images/curve.png")
MENU_IMAGES.append("images/fill.png")


largura = CANVAS_START_AT + larguraCanvas
altura = alturaCanvas
SCREEN_DIMENSION = (largura, altura)
if cor:
    BACKGROUND_COLOR = colors.BLACK
    DRAW_COLOR = colors.WHITE
else:
    BACKGROUND_COLOR = colors.WHITE
    DRAW_COLOR = colors.BLACK

REFRESH_RATE = atualizacao
SPECIAL_TYPE_STANDARD = ""

def CANVAS_LOCATION(startX, startY):
    return CANVAS_START_AT, 0, larguraCanvas, alturaCanvas