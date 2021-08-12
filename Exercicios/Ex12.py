number = int(input("Por favor digite um numero inteiro "))
def numerozin(numbero):
    parImpar = ""
    posneg = ""
    if numbero%2 ==0:
        parImpar = "Par"
    else:
        parImpar = "Impar"
    if numbero <0:
        posneg = "Negativo"
    else:
        posneg = "Positivo"
    return print("O numero",numbero,"é",parImpar,"e",posneg)
numerozin(number)