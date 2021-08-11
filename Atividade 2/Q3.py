d = [int(input("Informe o Ano de Nascimento:")),int(input("Informe o Ano Atual:"))]
idade = d[1]-d[0]

if idade >= 60:
    print("Você tem",idade,"anos e já pode dar entrada na APOSENTADORIA!")
else:
    print("Você tem", idade, "anos e faltam",60-idade,"anos para você dar entrada na APOSENTADORIA!")
    
