Notas = [float(input("Nota 1:")),float(input("Nota 2:"))]

media_notas = sum(Notas)/2

if media_notas >= 7:
    print("A média das notas é",media_notas)
    print("Você está APROVADO!")
elif media_notas >= 5:
    print("A média das notas é",media_notas)
    print("Você está RECUPERAÇÃO!")
else:
     print("A média das notas é",media_notas)
     print("Você está REPROVADO!")
