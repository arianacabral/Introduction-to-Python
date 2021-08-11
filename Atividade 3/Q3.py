# Faça uma função que receba o raio e retorne o volume de uma esfera

import math

def volume_esfera(raio):
    volume = (4/3)*math.pi*pow(raio,3)
    return volume

raio = float(input("Raio da esfera:"))

vol_esf = volume_esfera(raio)

print("O volume da esfera de raio {} é {:.2f}".format(raio,vol_esf))

