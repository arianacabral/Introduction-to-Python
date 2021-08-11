# Escreva um programa que leia a quantidade de horas, minutos e segundos de uma partida de tênis. Calcule o total em segundos
t_h = int(input("Tempo da partida em horas:"))
t_min = int(input("Tempo da partida em minutos:"))
t_s = int(input("Tempo da partida em segundos:"))
print("A duração da partida é",t_s+ t_min*60 + t_h*3600,"segundos")
