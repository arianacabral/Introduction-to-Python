velocidade = float(input("Velocidade (em km/h):"))

if velocidade <= 80:
    print("Não há multa!")
else:
    print("Você ultrapassou a velocidade máxima de 80 km/h! A multa a ser paga é de", (velocidade - 80)*50, "reais.")
    
