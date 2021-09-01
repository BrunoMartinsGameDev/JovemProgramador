#7.Escrever um algoritmo que gera e escreve os númerosímpares entre 100 e 200.
impares = []
for i in range(100,201):
    if i%2 != 0:
       impares.append(i)
print(impares)