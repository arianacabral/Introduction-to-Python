# Escreva um programa que leia a idade de 5 pessoas e, ao final, informe a idade total dessas pessoas.

n =1

soma = 0 

while n <= 5:
    idade = int(input("Idade da pessoa {}:".format(n)))
    soma = soma + idade
    n += 1  

print("A soma das idades é {}".format(soma))
