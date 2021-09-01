# Exercício 4
# Um funcionário recebe um salário fixo mais 4% decomissão sobre as vendas.
# Faça um algoritmo que receba o salário fixo de um funcionário
# e o valor de suas vendas, calcule e mostre a comissão
# e o salário final do funcionário.
comissao = float(input("Qual o valor total das suas vendas? "))
comissao = comissao*0.04
salario = float(input("Qual seu salario? "))
print("Voce recebeu", comissao,"de comissão, seu salário final é de", salario+comissao)