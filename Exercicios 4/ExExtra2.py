# Exercício Extra 2
# Faça uma progressão aritmética onde você
# solicita para o usuário quantos números
# serão mostrados, a razão da Progressão Aritmética
# e o início da Progressão Aritmética.
primeiroTermo = float(input("Qual o primeiro termo da PA? "))
razao = float(input("Qual a razao da PA? "))
qtdNum = int(input("Quantos numero existiram nessa PA? "))
pa = [primeiroTermo]
for i in range(0,qtdNum-1):
    pa.append(pa[i]+razao)
print(pa)
