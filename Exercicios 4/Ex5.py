# Exercício 5
# Faça a lista fibonacci de 20 posições.
# Exemplo: [0, 1, 1, 2, 3, 5, 8 ...]
lista = []
fibo = 0
for i in range(0,20):
    if i == 0:
        lista.append(i)
        fibo=1
    elif i == 1:
        lista.append(i)
    else:
        fibo = lista[i-1] + lista[i-2]
        lista.append(fibo)
print(lista) 