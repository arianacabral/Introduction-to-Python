# Escreva um programa que leia a quantidade de notas de um aluno, leia as notas e ao final, informe se o aluno foi aprovado ou não (considere que a média mínima para aprovação é 6). Imprima também a média do aluno

n_notas = int(input("Quantidade de notas: "))
soma = 0

for i in range(1,n_notas+1):
    nota = float(input("Nota {}: ".format(i)))
    soma = soma + nota
    
media = soma/n_notas

if(media >= 6):
    print("Sua média é {:.2f}. Você está APROVADO!".format(media))
else:
    print("Sua média é {:.2f}. Você está REAPROVADO!".format(media))
