#8.Criar um algoritmo que leia os limites inferior e superior de um intervalo e imprima 
# todos os números pares no intervalo aberto e seu somatório.
# Suponha que os números digitados são um intervalo crescente. 
# Exemplo:
# a.Limite inferior: 3
# b.Limite superior: 12
# c.Saída: 4 6 8 10
# d.Soma: 28
limiteSup = int(input("Digite limite superior\n"))
limiteInf = int(input("Digite limite inferior\n"))
total = 0
for i in range(limiteInf,limiteSup):
    if i%2 == 0:
        print(i)
        total +=i
print(total)
