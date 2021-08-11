# Escreva um programa que leia o curso de 10 alunos e escreva a mensagem “PARABÉNS!” sempre que o aluno for de Introdução a Algoritmos com Python

for i in range(1,11):
    curso = input("Informe o curso: ")
    if(curso.upper() == "INTRODUÇÃO A ALGORITMOS COM PYTHON"):
        print("PARABÉNS!")
