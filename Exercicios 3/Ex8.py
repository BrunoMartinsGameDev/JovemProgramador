#8.Escreva um algoritmo que leia um valor inicial e imprima 
#a sequência de valores e oseu resultado. 
#Ex: Valor informado => 5; Sequênciade valores e resultado => 5 * 4 *3 * 2 * 1 = 120
num = int(input("Digite um numero: "))
total = 1
for i in range(0,num+1):
    exp = num-i
    if exp > 0:
        print(exp)
        total = total*(num-i)
print(total)
#Funçao de FATORIAL
'''def Fatoraçao(num):
    total = 1
    for i in range(0,num+1):
        exp = num-i
        if exp > 0:
            total = total*(num-i)
    return total
print(Fatoraçao(5))'''