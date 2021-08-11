# Escreva um programa que leia o valor de 4 produtos, o valor pago pelo cliente e informe se há troco

soma = 0

for x in range(1,5):
    valor = float(input("Informe o valor do produto {}:".format(x)))
    soma = soma + valor

valor_pago = float(input("Valor pago:"))

if(valor_pago >= soma):
    troco = valor_pago - soma
    print("O valor da compra é de R$ {:.2f} e o seu troco é de R$ {:.2f}".format(soma, troco))
else:
    print("O valor pago é inferir ao valor da compra!")
