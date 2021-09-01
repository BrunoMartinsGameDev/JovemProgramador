# Exercício Extra 1
# Faça um algoritmo que permita ao usuário informar
# a idade de quantas pessoas ele desejar.
# Após isso o algoritmo deve informar a soma das
# pessoas maiores de idade e a média de idade das
# pessoas maiores de idade informadas.
true = True
maiorDeIdade = []
soma = 0
while true:
    idade = int(input("Digite a idade de uma pessoa\nCaso deseje encerra digite -1\n"))
    if idade == -1:
        true = False
        break
    if idade >17:
        maiorDeIdade.append(idade)
for i in range(0,len(maiorDeIdade)):
    soma+=maiorDeIdade[i]
media = soma/len(maiorDeIdade)
print("A soma das idades das pessoas de maior é:",soma)
print("E a média dessas idades é:",media)