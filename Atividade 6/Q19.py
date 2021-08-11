# Escreva um programa que escreva uma contagem regressiva para o ano novo começando em 10. Ao final escreva a mensagem “Feliz Ano Novo!”

cont = 10

for i in range(1,11):
    print(cont)
    cont = cont - 1
    if (cont == 0):
        print("Feliz Ano!")
