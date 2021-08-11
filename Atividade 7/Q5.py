# Escreva um programa que leia o valor de 10 produtos, salve em uma lista e informe a média dos valor dos produtos

produtos = [float(input("Valor do produto: "))]

i = 1

for i in range(1,10):
    produtos = produtos + [float(input("Valor do produto: "))]

media = sum(produtos)/10

print("A média de preço dos produtos é R$ {:.2f}".format(media))
