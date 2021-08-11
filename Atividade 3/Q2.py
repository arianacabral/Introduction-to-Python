#Faça uma função que receba o raio e retorne a área de um círculo

import math

def area_circulo(raio):
    area = math.pi*pow(raio,2)
    return area

raio = float(input("Raio do círculo:"))

area_circ = area_circulo(raio)

print("A área do círculo de raio {} é {:.2f}".format(raio,area_circ))
