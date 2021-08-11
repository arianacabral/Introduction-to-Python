d = [int(input("Ano de Nascimento:")),int(input("Ano Atual:"))]
idade = d[1]-d[0]

if idade >= 60:
    print("Você tem",idade,"anos e já pode dar entrada na APOSENTADORIA!")
else:
    print("Você tem", idade, "anos e NÃO possui a idade mínima para dar entrada na APOSENTADORIA!")
    
