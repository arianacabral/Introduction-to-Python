# Escreva um programa que leia a idade de 11 jogadores de um time e, ao final, informe quantos desses tem mais que 30 anos

cont = 0

for i in range(1,12):
    idade = int(input("Idade do jogador {}: ".format(i)))

    if(idade > 30):
        cont += 1

print("A quantidade de jogadores com mais de 30 anos é {} ".format(cont))
