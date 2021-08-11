# Escreva um programa que leia a quantidade de notas de um aluno, leia as notas e informe a média do aluno

n = int(input("Quantidade de notas:"))

i = 1

soma = 0

while i <= n:
    nota = float(input("Nota {}:".format(i)))
    soma = soma + nota
    i += 1

media = soma/n

print("A média das notas foi {:.2f}".format(media))
