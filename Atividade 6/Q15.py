# Escreva um programa que pergunte o curso de um aluno e imprima o nome do curso 30 vezes

curso = input("Informe seu curso: ")

for i in range(1, 31):
    print("{} - {}".format(i,curso))
