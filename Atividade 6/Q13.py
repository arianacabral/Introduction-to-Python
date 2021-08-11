# Escreva um programa que imprima na tela os 10 primeiros números terminados com 2

for i in range(1,100):
    nm = str(i)
    if(nm[-1] == "2"):
        print(nm)

