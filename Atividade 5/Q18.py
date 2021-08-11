# screva um programa que leia números até o usuário digitar 0. Ao final, informe quantos desses números eram o 7

def number_test(number):

    cont = 0
    while number != 0:
         number = float(input("Informe um número:"))
         if(number == 7):
             cont += 1
    return cont
          

input0 = float(input("Informe um número:"))

n = number_test(input0)

print("Foram digitados {} números 7".format(n))
