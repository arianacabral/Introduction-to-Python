# Escreva um programa que leia o curso de 20 alunos e escreva a mensagem “PARABÉNS!” sempre que o aluno for de (SEU CURSO)

n = 1

while n <= 20:
    curso = input("Informe seu curso:")
    n += 1
    if(curso.upper() == "ENGENHARIA BIOMÉDICA"):
        print("Parabéns!")
    
