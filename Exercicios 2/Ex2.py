# Exercício 2
# Um tonel de refresco é feito com 8 partes de águamineral
# e 2 partes de suco de maracujá.
# Faça um algoritmo para calcular quantos litros deágua
# e de suco são necessários para se fazer X litros de refresco
# (informados pelo usuário).
qntSuco = float(input("Quantos litros de suco serão feitos? "))
parteAgua = 0
parteSuco = 0
def Partes():
    parteAgua = qntSuco*0.8
    parteSuco = qntSuco*0.2
    print("Você precisa de "+str(round(parteAgua,2))+" litros de água e "+ str(round(parteSuco,2))+" listros de suco")
Partes()