import colors


#Defina aqui a largura e a altura da janela
largura = 800
altura = 600

#Defina o esquema de cor padrão entre os seguintes valores: 0 - (background branco, desenho preto) ou 1 - (background preto, desenho branco)
cor = 0


#Defina a taxa de atualização da tela
atualizacao = 144






#Não mexa aqui
SCREEN_DIMENSION = (largura, altura)
if cor:
    BACKGROUND_COLOR = colors.BLACK
    DRAW_COLOR = colors.WHITE
else:
    BACKGROUND_COLOR = colors.WHITE
    DRAW_COLOR = colors.BLACK

REFRESH_RATE = atualizacao
SPECIAL_TYPE_STANDARD = ""