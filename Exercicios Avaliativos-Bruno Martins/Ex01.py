#1. Faça um algoritmo que calcule e mostre a tabuada de um numero digitado pelo usuário
num = int(input("De qual numero você deseja saber a tabuada?"))
print("TABUADA DO",num)
#Ira fazer a multiplicação do numero escolhido do zero até o 10
for i in range (0,11):
    print(num,"*",i,"= ",num*i)