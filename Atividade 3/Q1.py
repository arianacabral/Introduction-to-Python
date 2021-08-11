# Faça uma função que receba a base e altura de um retângulo e retorne a área do mesmo.

def area_retangulo(altura,base):
    area = altura*base
    return area

rect = [float(input("Altura do retângulo:")),float(input("Base do retângulo:"))]

area_rect = area_retangulo(rect[0],rect[1])

print("A área do retângulo de altura {} e base {} é {}".format(rect[0],rect[1],area_rect))
