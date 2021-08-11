# Escreva um programa que leia o valor de 5 produtos, salve em uma lista e informe esses números na tela de maneira organizada.

produtos = [float(input("Valor do produto 1:")),
            float(input("Valor do produto 2:")),
            float(input("Valor do produto 3:")),
            float(input("Valor do produto 4:")),
            float(input("Valor do produto 5:"))]

i = 0

for i in range(0,len(produtos)):
    print(produtos[i])
