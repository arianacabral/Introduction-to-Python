# Escreva um programa que escreva uma mensagem definida pelo usuário 55 vezes

msg = input("Mensagem de entrada:")

n = 1

while n <= 55:
    print("{} - {}".format(n,msg))
    n += 1
