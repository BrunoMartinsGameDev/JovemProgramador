#Exercício 6
# Faça um programa que recebe a altura de um triangulo
# em um número inteiro e imprima-o utilizando asteriscos.
# Veja o Exemplo:
# Entrada: 5
# *
# **
# ***
# ****
# *****
def Triangulo():
    tamanho = int(input("Digite a altura do seu triangulo:\n"))
    if tamanho<1:
        print("Tamanho Inválido")
        Triangulo()
    else:
        for i in range(0,tamanho):
            mult = i+1
            print("*"*mult)
Triangulo()