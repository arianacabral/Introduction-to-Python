# Escreva um programa que escreva uma mensagem definida pelo usuário, uma quantidade de vezes também definida pelo usuário

msg = input("Mensagem de entrada:")
n = int(input("Número de vezes que a mensagem será repetida:"))

i = 1 

while i <= n:
    print("{} - {}".format(i,msg))
    i += 1
