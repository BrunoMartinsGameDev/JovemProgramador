#3.João recebeu seu salário de R$1200,00 e precisa pagar duas contas(C1=R$200,00eC2=R$120,00)
# que estão atrasadas.Como as contas estão atrasadas,João terá de pagar multa de 2% sobre cada conta.
# Faça um algoritmo que calcule e mostre quanto restará do salário do João
salario = float(input("Qual o seu salário joao?"))
qtdContas = int(input("Quantas contas você tem para pagar?"))
totalPagar = 0
#Repete o codigo para cada conta que o joao tem q pagar
for i in range (0,qtdContas):
    print("Conta:",i+1)
    valorConta = float(input("Qual o valor da conta?"))
    atraso = input("A conta ta atrasada?(S/N)")

    if atraso == "S" or atraso =="s":
        totalPagar += valorConta+valorConta*0.02
    else:
        totalPagar += valorConta
print("João, sobrou R$",round(salario-totalPagar,2))
