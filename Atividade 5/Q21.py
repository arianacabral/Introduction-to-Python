# Escreva um programa que leia a idade de 5 pessoas e, ao final, informe a média das idades dessas pessoas.

n =1

soma = 0 

while n <= 5:
    idade = int(input("Idade da pessoa {}:".format(n)))
    soma = soma + idade
    n += 1  

media = soma/5

print("A média das idades é {}".format(media))
