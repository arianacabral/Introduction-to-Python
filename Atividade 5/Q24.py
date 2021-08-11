# Escreva um programa que leia notas de um aluno até o usuário digitar -1 e, ao final, informe a média do aluno e se o aluno foi aprovado ou não (considere que a média mínima para aprovação é 7).

def media_notas(nota):

    cont = 0
    soma = 0
    
    while nota != -1:
         cont += 1
         soma = soma + nota
         nota = float(input("Informe sua nota:"))
    media = soma/cont

    if(media >= 7):
        print("A média das suas notas é {}. Você está APROVADO!".format(media))
    else:
        print("A média das suas notas é {}. Você está REPROVADO!".format(media))
          

nota = float(input("Informe sua nota:"))

media_notas(nota)
