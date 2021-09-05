#Exercício 4
# Faça um programa que receba a idade, altura e opeso de 25 pessoas,
# Calcule e mostre:
# * A quantidade de pessoas com idade superior a 50anos;
# * A média das Alturas das pessoas com idade entre10 e 20 anos
# * A porcentagem das pessoas com peso inferior a40 quilos
# entre todas as pessoas analisadas.
import random
veiosMais50 = 0
altura10a20 = []
pessoasCom40menos = 0
for i in range(0,25):
    idade = int(random.randrange(0,90))
    altura = round(random.uniform(1,2),2)
    peso = round(random.uniform(20,100),2)
    print(idade,altura,peso)
    if idade>50:
        veiosMais50+=1
    if idade>=10 and idade<=20:
        altura10a20.append(altura)
    if peso<40:
        pessoasCom40menos+=1
def TotalAltura():
    total = 0
    for i in altura10a20:
        total += i 
    return total
print("Pessoas com mais de 50 anos:",veiosMais50)
print("Média da altura entre 10 a 20 anos:",TotalAltura()/len(altura10a20))
print("Porcentagem de pessoas com menos de 40 kg:",(pessoasCom40menos/25)*100,"%")
