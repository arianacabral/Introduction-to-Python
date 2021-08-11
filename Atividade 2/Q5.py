Notas = [float(input("Nota 1:")),float(input("Nota 2:")),float(input("Nota 3:")),float(input("Nota 4:"))]

media_notas = sum(Notas)/4

if media_notas >= 7:
    print("A média das notas é",media_notas)
    print("Aprovado!")
else:
     print("A média das notas é",media_notas)
     print("Reprovado!")
