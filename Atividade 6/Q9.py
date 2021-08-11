# Considerando que um dado elevador suporta 350Kg, escreva um programa que leia o peso de 5 pessoas e, ao final, informe se o elevador suporta o peso total

peso_total = 0

for i in range(1,6):
    peso = float(input("Peso da pessoa {}:".format(i)))
    peso_total = peso_total + peso

if(peso_total <= 350):
    print("O peso total é de {:.2f} kg e o elevador suporta esse peso!".format(peso_total))

else:
    print("O peso total é de {.:2f} kg e o elevador não suporta esse peso!".format(peso_total))
