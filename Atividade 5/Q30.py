# Um elevador suporta no máximo 350Kg. Sabendo disso, escreva um programa que leia o peso de 6 pessoas, informe o total lido e diga se o elevador pode ser utilizado ou não

n = 1

peso_total = 0

while n <= 6:
    peso = float(input("Informe o seu peso:"))
    peso_total = peso_total + peso
    n += 1
if(peso_total >= 350):
    print("O peso total é {:.2f} e o elevador não pode ser utilizado".format(peso_total))
else:
    print("O peso total é {:.2f} e o elevador pode ser utilizado".format(peso_total))
