#8.Altere o algoritmo abaixo,de maneira que ele imprima
# o percentual de pessoas considerando as faixas de idade:
# 0-17anos,18a34anos,35a49anos,50a64 anos e maiores de 64 anos.
# Lembrete:a soma dos percentuais das faixas deve totalizar 100%
numero = int(input("Quantas pessoas? "))
soma = 0
ate17 = 0
ate34 = 0
ate49 = 0
ate64 = 0
mais64 = 0
#loop que verifica a quantidade de pessoas em cada faixa etária
for x in range(0,numero):
    idade = int(input("Qual a idade? "))
    if idade>64:
        mais64+=1
    elif idade>49:
        ate64 +=1
    elif idade>34:
        ate49 +=1
    elif idade>17:
        ate34 += 1
    elif idade>0:
        ate17 +=1
    else:
        pass     
    soma+=1
print("Percentual de pessoas até 17 anos:",(ate17/soma)*100,"%")
print("Percentual de pessoas até 34 anos:",(ate34/soma)*100,"%")
print("Percentual de pessoas até 49 anos:",(ate49/soma)*100,"%")
print("Percentual de pessoas até 64 anos:",(ate64/soma)*100,"%")
print("Percentual de pessoas mais que 64 anos:",(mais64/soma)*100,"%")