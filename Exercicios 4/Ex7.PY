# Exercício 7
# Construa um algoritmo que leia uma quantidade indeterminada
# de números inteiros positivos e identifique
# qual foi o maior número digitado.
# O final da série de números digitada deve ser indicado
# pela entrada de –1.
true = True
lista = []
while true:
    num=int(input("Digite um numero:\nCaso queira encerra digite -1\n"))
    if num == -1:
        true = False
        break
    if num>0:
        lista.append(num)
print("O maior numero positivo foi", max(lista))