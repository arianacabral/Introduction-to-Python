# Escreva um programa que leia 10 números inteiros. Em seguida informe a quantidade de números 3 lidos

num3 = 0

for i in range(1,11):
    num = int(input("{} - Informe um número: ".format(i)))
    if(num == 3):
        num3 += 1

print("A quantidade de números 3 é {}".format(num3))
