#Exercício 3
# Uma loja utiliza o código V para transação à vistae P para transaçãoa prazo.
# Faça um programa que receba código e valor de 15transações.
# Calcule e mostre:
# * O valor total das compras à vista
# * O valor total das compras a prazo.
# * O valor total das compras efetuadas
# Extra
# * O valor da primeira prestação das compras a prazo,
# sabendo-se que essas serão pagas em três vezes

vista = []
prazo = []
for i in range(0,15):
    print("Compra numero:",i+1)
    valor = float(input("Qual o valor da transação?"))
    codigo = str(input("Irá pagar as vista ou a prazo?(V/P"))
    if codigo == 'v' or codigo == 'V':
        vista.append(valor)
    elif codigo == 'p' or codigo == 'P':
        prazo.append(valor)
def AVista():
    total = 0
    for i in vista:
        total += i
    return total
def APrazo():
    total = 0
    for i in prazo:
        total += i
    return total
def Total():
    total = 0
    for i in prazo+vista:
        total += i
    return total
print("Total das transações a vista:",AVista())
print("Total das transações a prazo:",APrazo())
print("Total das transações totais:",Total())
print("Primeira prestação das compras a prazo é de:",APrazo()/3)
