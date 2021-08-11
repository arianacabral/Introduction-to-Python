# Escreva um programa que leia dois números inteiros positivos e calcule o valor do primeiro número elevado ao segundo número. Não utilize o operador **

numero = [int(input("Informe a base da exponenciação")), int(input("Informe o expoente da exponenciação"))]

if(numero[0] >= 0 & numero[1] >= 0):
    resultado = 1
    n = 1
    while n <= numero[1]:
        resultado = resultado * numero[0]
        n += 1
    print("O valor de {}^{} é {}".format(numero[0],numero[1],resultado))
else:
    print("Valores inválidos para a operação!")
