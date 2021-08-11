# Uma pesquisa está analisando o preço da cesta básica em diferentes estabelecimentos. Para ajudar nessa análise, escreva um programa que leia o preço da cesta básica em 20 estabelecimentos e informe o preço médio da cesta nos estabelecimentos pesquisados

soma = 0

for i in range(1,21):
    valor = float(input("Valor da cesta básica no estabelecimento {}: ".format(i)))
    soma = soma + valor

valor_medio = soma/20

print("O valor médio da cesta básica é de R$ {:.2f}".format(valor_medio))
