#7.Faça um programa que leia um valor n ,inteiro e positivo,calcule e mostre a seguinte soma:
#  S = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n.
num = float(input("Digite um numero inteiro e positivo!\n"))
soma = 0
#verifica se o valor é inteiro e positivo
if num <0 or num-int(num)!= 0:
    print("Valor inválido")
else:
    #faz a magia da matematica
    for i in range(0,int(num)):
        soma += 1/(i+1)
print("Soma total =",soma)