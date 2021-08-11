# Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def function_test(arg):
    if(arg > 0):
        resultado = "P"
    else:
        resultado = "N"

    return resultado

arg = float(input("Informe um número:"))

resultado = function_test(arg)

print("O resultado para {} é {}".format(arg,resultado))
