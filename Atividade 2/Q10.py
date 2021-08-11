idade = int(input("Idade:"))

if idade >= 0 and idade <= 10:
    print("Você é uma CRIANÇA!")
elif idade > 10 and idade <= 17:
    print("Você é um ADOLESCENTE!")
elif idade > 17 and idade <= 23:
    print("Você é um JOVEM!")
elif idade > 23 and idade <= 55:
    print("Você é um ADULTO!")
elif idade > 55:
    print("Você é um IDOSO!")
else:
    print("Idade Inválida!")
    
