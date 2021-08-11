# Escreva um programa que leia números até o usuário digitar -1. Ao final, informe quantos números foram lidos.

def conta_numeros(number):

    cont = 1
    
    while number != -1:
         number = float(input("Informe um número:"))
         cont += 1
    return cont
          

input0 = float(input("Informe um número:"))

n = conta_numeros(input0)

print("A quantidade de números digitados foi {}".format(n))
