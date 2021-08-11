# Escreva um programa que leia o valor de 6 produtos, salve em uma lista e informe o total desses produtos

produtos = [float(input("Valor do produto 1:")),
            float(input("Valor do produto 2:")),
            float(input("Valor do produto 3:")),
            float(input("Valor do produto 4:")),
            float(input("Valor do produto 5:")),
            float(input("Valor do produto 6:"))]

soma = sum(produtos)

print("O valor dos produtos é R$ {:.2f}".format(soma))
