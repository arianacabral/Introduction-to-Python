# Escreva um programa que leia o peso de 5 pessoas e informe o total dos pesos lidos

peso_total = 0

for i in range(1,6):
    peso = float(input("Informe o peso da peso {}:".format(i)))
    peso_total = peso_total + peso

print("O peso total é de {} kg".format(peso_total))
