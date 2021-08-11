# Escreva um programa que leia 20 números e imprima a quantidade de números negativos digitados pelo usuário.

cont = 0

for i in range(1,21):
    num = int(input("{} - Informe um número: ".format(i)))
    if(num < 0):
        cont += 1

print("A quantidade de números negativos é {}".format(cont))
