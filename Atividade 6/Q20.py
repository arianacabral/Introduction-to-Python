# Escreva um programa que leia 50 números e imprima “maior” caso o número seja maior que 100 e “menor” caso seja menor que 100

for i in range(1,51):
    num = float(input("{} - Informe um número: ".format(i)))
    if(num > 100):
        print("MAIOR!")

    elif(num < 100):
        print("MENOR!")

    else:
        print("IGUAL!")
