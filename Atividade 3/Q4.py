# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos

def soma_args(arg1,arg2,arg3):
    soma = arg1+arg2+arg3
    return soma

args = [float(input("Primeiro argumento:")),float(input("Segundo argumento:")),float(input("Terceiro argumento:"))]

soma = soma_args(args[0],args[1],args[2])

print("{} + {} + {} = {}".format(args[0],args[1],args[2],soma))
