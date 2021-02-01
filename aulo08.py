import math

def paint_calc(height, width, cover):
    area = height * width
    #arrendodar numero com a math modulo e cail function
    num_of_cans = math.ceil(area / cover)
    print(f" Youll need {num_of_cans} cans of paint")

    paint_calc()

teste_h = int(input("Height of wall: \n"))
teste_w = int(input("Width of wall: \n"))
covarege = 5
#chama a função paint calc passando como parametro os inputs recebidos nas variaveis teste_h e teste-w
# a funcao calcula a area e retorna o print do arredondamento do valor
paint_calc(height = teste_h, width=teste_w, cover=covarage) 