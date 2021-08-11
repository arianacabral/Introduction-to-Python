# Escreva um programa que leia quatro notas de um aluno usando listas e calcule a média desse aluno.

notas = [float(input("Informe a sua nota: "))]

i = 1

for i in range(1,4):
    notas = notas + [float(input("Informe a sua nota: "))]

media = sum(notas)/4

print("A média das notas é {:.2f}".format(media))
