# Escreva um programa que leia 10 números e imprima a quantidade de números positivos e a quantidade de números negativos digitados pelo usuário.

n = 1

neg = 0

pos = 0

while n <= 10:
    number = float(input("Informe um número:"))
    n += 1
    if(number < 0):
        neg += 1
    else:
        pos += 1
print("A quantidade de números negativos digitados é {} e a quantidade de números positivos digitados é {}".format(neg,pos))
  
