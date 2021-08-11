# Escreva um programa que leia o peso de 10 pessoas e informe o total lido

n = 1

peso_total = 0

while n <= 10:
    peso = float(input("Informe o seu peso:"))
    peso_total = peso_total + peso
    n += 1
print("O peso total é {:.2f}".format(peso_total))
