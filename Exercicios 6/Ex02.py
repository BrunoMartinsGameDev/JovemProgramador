#Exercício 2
# Faça um programa que receba a idade de 15 pessoase que calcule e mostre:
# a) A quantidade de pessoas em cada faixa etária;
# b) A percentagem de pessoas na primeira e na última faixa etária, com relação ao total de pessoas:
#    Até 15 anos
#    De 16 a 30 anos
#    De 31 a 45 anos
#    De 46 a 60 anos
#    Acima de 61 anos
idade15 = []
idade30 = []
idade45 = []
idade60 = []
idadeVelho = []
for i in range(0,15):
    idade = int(input("Digite uma idade: \n"))
    if idade <=15:
        idade15.append(i)
    elif idade <=30:
        idade30.append(i)
    elif idade <=45:
        idade45.append(i)
    elif idade <=60:
        idade60.append(i)
    else:
        idadeVelho.append(i)
print("Quantidade de pessoas\n")
print("Até 15 anos:",len(idade15))
print("Até 30 anos:",len(idade30))
print("Até 45 anos:",len(idade45))
print("Até 60 anos:",len(idade60))
print("Mais que 60 anos:",len(idadeVelho))
total = len(idade15)+len(idade30)+len(idade45)+len(idade60)+len(idadeVelho)
print("Porcentagem de pessoas até 15 anos: ",(len(idade15)/total)*100,"%")
print("Porcentagem de pessoas mais de 60 anos: ",(len(idadeVelho)/total)*100,"%")