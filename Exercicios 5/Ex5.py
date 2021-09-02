#5.Desenvolver um algoritmo que efetue a soma de todos os números ímpares que são 
# múltiplos de três e que se encontram no conjunto dos números de 1 até 500.
lista=[]
soma = 0
for i in range(0,500):
    if i%3 == 0 and i%2 != 0:
        lista.append(i)
        soma+=i
print(lista)
print(soma)