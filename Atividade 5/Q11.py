# Escreva um programa que leia 10 números e imprima “Positivo” quando o número digitado for maior que 0.

n = 1

while n <= 10:
    number = float(input("Informe um número:"))
    n += 1
    if(number >= 0):
        print("O número {} é POSITIVO".format(number))

    

