#Escreva um programa que leia o nome do usuário e depois imprima 9 vezes o nome do lido.

n = 1

while n <= 300:
    nm = str(n)
    if( nm[-1] == "5" or nm[-1] == "9"):
        print(nm)
    n+= 1
    
