# Exercício 4
# Escrever um algoritmo que leia uma quantidade denúmeros
# que deve ser lidos.
# E conte quantos deles estão nos seguintes intervalos:
# 1) 0 à 25
# 2) 26 à 50
# 3) 51 à 75
# 4) 76 à 100.
lista = [5,20,30,45,60,70,80,96]
intervalo1 = 0
intervalo2 = 0
intervalo3 = 0
intervalo4 = 0

for i in lista:
    if  i <=100 and i>75:
        intervalo4+=1
    elif  i <76 and i>50:
        intervalo3+=1
    elif  i <51 and i>25:
        intervalo2+=1
    elif  i <26 and i>=0:
        intervalo1+=1
    else:
        pass
print("Entre 0 à 25:", intervalo1)
print("Entre 26 à 50:", intervalo2)
print("Entre 51 à 75:", intervalo3)
print("Entre 76 à 100:", intervalo4)