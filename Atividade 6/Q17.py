# Escreva um programa que leia a idade de 25 pessoas e, ao final, informe a média dessas idade


soma = 0

for i in range(1,21):
    idade = int(input("Idade da pessoa {}: ".format(i)))
    soma = soma + idade

valor_medio = soma/20

print("O valor médio das idades é {} ano(s)".format(valor_medio))
