# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem

base = int(input("Informe a base: "))
exp = int(input("Informe o expoente:"))

result = 1

if(base and exp >= 0):
    for i in range(1,exp+1):
        result = result * base
    print("{}^{} = {}".format(base,exp,result))
else:
    print("Valores inválidos!")
