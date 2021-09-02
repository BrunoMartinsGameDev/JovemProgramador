# Exercício 2
# Escrever um algoritmo que lê 5 valores para a,
# um de cada vez,
# e conta quantos destes valores são negativos,
# escrevendo esta informação.
a = [-7,-15,5,16,-16]
quantos = 0
for i in a:
    if i <0:
        quantos+=1
        print(i,"é negativo, totalizando",quantos,"numeros negativos")