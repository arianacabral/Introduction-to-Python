# Escreva um programa que leia 10 números e imprima “Positivo” ou “Negativo” de acordo com o valor do número digitado

n = 1

while n <= 10:
    number = float(input("Informe um número:"))
    n += 1
    if(number >= 0):
        print("O número {} é POSITIVO".format(number))
    else:
        print("O número {} é NEGATIVO".format(number))

    
