#Escreva um programa que leia a nota de 10 alunos e, ao final, informe quantos desses tiraram nota maior ou igual a 6.

cont = 0

for i in range(1,11):
    nota = float(input("Nota do aluno {}: ".format(i)))

    if(nota >= 6):
        cont += 1

print("{} alunos tiveram nota maior ou igual a 6".format(cont))
