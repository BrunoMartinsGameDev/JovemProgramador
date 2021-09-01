#1.Faça um algoritmo que leia um número e mostre se eleé positivo, negativo ou zero.
num = float(input("Digite um numero: "))
def PosOuNeg():
    if num == 0:
        return "Zero"
    elif num>0:
        return "Positivo"
    else:
        return "Negativo"
print("O numero",num,"é",PosOuNeg())