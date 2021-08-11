# Escreva um programa que leia quatro notas de um aluno usando listas e informe se o mesmo foi aprovado ou não

notas = [float(input("Informe a sua nota: "))]

i = 1

for i in range(1,4):
    notas = notas + [float(input("Informe a sua nota: "))]

media = sum(notas)/4


if(media >= 6):
    print("A média das notas é {:.2f} e você está APROVADO!".format(media))
else:
    print("A média das notas é {:.2f} e você está REAPROVADO!".format(media))
