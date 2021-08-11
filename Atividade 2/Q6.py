Irmão1 = [(input("Nome do primeiro irmão:")),int(input("Idade do primeiro irmão:"))]
Irmão2 = [(input("Nome do segundo irmão:")),int(input("Idade do segundo irmão:"))]


if Irmão1[1] < Irmão2[1]:
    print("O irmão mais novo é o(a)", Irmão1[0])
elif Irmão1[1] == Irmão2[1]:
    print(Irmão1[0], "e", Irmão2[0], "têm a mesma idade")
else:
     print("O irmão mais novo é o(a)", Irmão2[0])
