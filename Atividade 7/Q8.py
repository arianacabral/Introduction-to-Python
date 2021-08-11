# Escreva uma função que recebe uma palavra e uma lista de palavras e retorne True se a palavra dada está contida na lista. Falso em outro caso

palavra = input("Informe a palavra para busca: ")

banco_de_palavras = [input("Informe a lista de palavras: ")]

if (palavra in banco_de_palavras):
    print("TRUE")
else:
    print("FALSE")
