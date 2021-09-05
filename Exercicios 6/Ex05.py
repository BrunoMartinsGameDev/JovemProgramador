#Exercício 5
# Escreva um programa que lê o tamanho do lado deum quadrado
# e imprime um quadrado daquele tamanho com asteriscos.
# Seu programa deve funcionar para quadrados com lados
# de todos os tamanhos entre 1 e 20.
# Por exemplo, para lado igual a 5:
# *****
# *****
# *****
# *****
# *****
def Quadrado():
    tamanho = int(input("Digite a altura do seu quadrado:\n"))
    if tamanho<1:
        print("Tamanho Inválido")
        Quadrado()
    else:
        for i in range(0,tamanho):
            print("*"*tamanho)
Quadrado()