# Escreva um programa que leia uma mensagem informada pelo usuário e, em seguida, imprima essa mensagem 15(quinze) vezes

msg = input("Mensagem:")

for i in range(1,16):
    print("{} - {}".format(i,msg))
