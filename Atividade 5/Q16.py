# Escreva um programa que leia 51 números e imprima quantos números 5 foram digitados pelo usuário

n = 1

cont5 = 0

while n <= 51:
    number = float(input("{} - Informe um número:".format(n)))
    n += 1
    if(number == 5):
        cont5 += 1

print("A quantidade números 5 digitados é {}".format(cont5))
  
