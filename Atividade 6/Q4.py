# Escreva um programa que leia o valor de 4 produtos e informe o total da compra

soma = 0

for x in range(1,5):
    valor = float(input("Informe o valor do produto {}:".format(x)))
    soma = soma + valor

print("O valor da soma é {:.2f}".format(soma))
