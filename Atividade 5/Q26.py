# Construa um programa que imprima os números inteiros positivos terminados com 5 menores que 300

n = 1

while n <= 300:
    if(n%5==0):
        if(n%2!=0):
            print(n)
    n+= 1
    
