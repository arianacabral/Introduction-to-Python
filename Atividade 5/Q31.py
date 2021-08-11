# Os alunos de informática estão elegendo o representante da turma. Nessa eleições, dois candidatos concorrem para saber o eleito. Você foi contratado para construir uma urna eletrônica que leia o nome dos candidatos e ao final, informe qual dos dois foi eleito. A votação será encerrada quando alguém digitar -1.

def conta_votos(nome, Candidatos):

    nome = nome.upper()
    Candidatos[0] = Candidatos[0].upper()
    Candidatos[1] = Candidatos[1].upper() 

    candidato1 = 0
    candidato2 = 0

    
    while nome != "-1" :
        if(nome == Candidatos[0]):
            candidato1 += 1
        elif(nome == Candidatos[1]):
             candidato2 +=1
        else:
            print("Canditado inválido!")
        nome = input("Informe o nome do candidato em que você votará: ")
        nome = nome.upper()
        

    if(candidato1 > candidato2):
        candidato_eleito = Candidato[0]
        print("O candidato eleito foi o(a) candidato(a) {} com {} votos".format(candidato_eleito,candidato1))
    elif(candidato1 == candidato2):
        print("Os dois candidadtos tiveram a mesma quantidade de votos, {} votos!".format(candidato1))
    else:
       candidato_eleito = Candidato[1]
       print("O candidato eleito foi o(a) candidato(a) {} com {} votos".format(candidato_eleito,candidato2)) 
          

Candidato = [input("Nome do primeiro candidato: "),input("Nome do segundo candidato: ")]

Nome = input("Informe o nome do candidato em que você votará: ")

if(Nome.upper() == Candidato[0].upper() or Nome.upper() == Candidato[1].upper()):
    conta_votos(Nome, Candidato)
else:
    print("Candidato inválido!")
    
