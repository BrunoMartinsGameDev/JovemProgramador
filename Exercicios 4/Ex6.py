# Exercício 6
# Faça um algoritmo que leia vários números
# e informe quantos desses números entre 100 e 200
# foram digitados.
# Quando o valor 0 (zero) for lido o algoritmo
# deverá cessar sua execução.
exit = 1
lista = []
qtdNum = 0
while exit != 0:
    num = int(input("Digite um numero: "))
    if num == 0:
        exit = 0
        break
    lista.append(num)
for i in lista:
    if i >99 and i<201:
        qtdNum+=1
print("Existem", qtdNum, "numeros entre 100 e 200")