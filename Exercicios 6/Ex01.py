#Exercício 1
#Faça um programa que receba a idade de dez pessoas
# e que calcule e mostre a quantidade de pessoas
# com idade maior ou igual a 18 anos.

idades = [5,10,50,36,18,20,7,15,10,90]
maiores = []
for i in idades:
    if i > 17:
        maiores.append(i)
print(maiores)
print(len(maiores))