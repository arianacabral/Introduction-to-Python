Notas = [float(input("Nota 1:")),float(input("Nota 2:"))]

if sum(Notas)/2 >= 7:
    print("A média das notas é",sum(Notas)/2)
    print("Aprovado!")
else:
     print("A média das notas é",sum(Notas)/2)
     print("Reprovado!")
