# A equipe pedagógica está analisando os resultados dos alunos no primeiro semestre. Para isso, eles precisam saber as notas dos 20 alunos do quarto ano da tarde. Escreva um programa que leia a nota dos alunos e informe quantos alunos tiraram nota maior ou igual a 6, quantos tiveram entre 4 e 6 e quantos tiraram notas abaixo de 4.

n = 1

nota_m6 = 0
nota_m4m6 = 0
nota_m4 = 0

while n <= 20:
    nota = float(input("Informe sua nota:"))
    if(nota >= 6):
        nota_m6 += 1
    elif(nota >= 4 and nota < 6):
        nota_m4m6 += 1
    elif(nota < 4):
        nota_m4 += 1
    n += 1
    
print("{} alunos tiveram nota maior ou igual a 6".format(nota_m6))
print("{} alunos tiveram nota maior ou igual a 4 e menor que 6".format(nota_m4m6))
print("{} alunos tiveram nota menor que 4".format(nota_m4))
