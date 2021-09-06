#2.Uma rainha requisitou os serviços de um monge,o qual exigiu o pagamento em grãos de trigo da seguinte maneira:
# os grãos de trigo seriam dispostos em um tabuleiro de xadrez,de tal forma que a primeira casa do tabuleiro tivesse um grão,
# e as casas seguintes o dobro da anterior.Construa um algoritmo que calcule quantos grãos de trigo a Rainha deverá pagar ao monge. Um tabuleiro tem 64 casas.
total = 1
lista = [total]
for i in range(0,64):
    if i > 0:
        total*=2
        lista.append(total)          
    print("Casa",i+1,":", total,"grãos")
totalGrande = 0
for i in range(len(lista)):
    totalGrande+=lista[i]
print(totalGrande)
    