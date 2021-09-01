#9.Faça um algoritmo que leia 10 números inteiros e calculeo somatório dos númerosnegativos. (Usar While)
lista= [-8,-15,10,5,3,4,-9,8,16,-16]
i = 0
total = 0
while i<len(lista):
    if lista[i]<0:
        total += lista[i]
    i +=1
print(total)