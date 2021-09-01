# Exercício 1
# Pedrinho tem um cofrinho com muitas moedas,
# e deseja saber quantos reais conseguiu poupar.
# Faça um algoritmo para ler a quantidade de cadatipo de moeda,
# e imprimir o valor total economizado, em reais.
# Considere que existam moedas de 1, 5, 10, 25 e 50centavos,
# e ainda moedas de 1 real. Não havendo moeda de um tipo,
# a quantidade respectiva é zero.
qntmoeda1 = int(input("Quantas moedas de 1 centavo você tem? "))
qntmoeda5 = int(input("Quantas moedas de 5 centavos você tem? "))
qntmoeda10 = int(input("Quantas moedas de 10 centavos você tem? "))
qntmoeda25 = int(input("Quantas moedas de 25 centavos você tem? "))
qntmoeda50 = int(input("Quantas moedas de 50 centavos você tem? "))
qntmoeda1Real = int(input("Quantas moedas de 1 Real você tem? "))
def Somar():
    total = qntmoeda1*0.01+qntmoeda5*0.05+qntmoeda10*0.1+qntmoeda25*0.25+qntmoeda50*0.5+qntmoeda1Real
    return total
print("Você tem um total de "+str(round(Somar(),2))+" reais")