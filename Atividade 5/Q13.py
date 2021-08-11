# Escreva um programa que leia 10 números e imprima a quantidade de números positivos digitados pelo usuário

n = 1

cont = 0

while n <= 10:
    number = float(input("Informe um número:"))
    n += 1
    if(number >= 0):
        cont += 1
print("A quantidade de números positivos digitados é {}".format(cont))
  
