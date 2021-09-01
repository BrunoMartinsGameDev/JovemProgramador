# Exercício 7
# Um usuário deseja um algoritmo onde possa escolher
# que tipo de média deseja calcular a partir de 3 notas.
# Faça um algoritmo que leia as notas,
# a opção escolhida pelo usuário e calcule a média.
# 1 -aritmética # 2 -ponderada (3,3,4)
nota1 = float(input("Digita a nota 1: "))
nota2 = float(input("Digita a nota 2: "))
nota3 = float(input("Digita a nota 3: "))
print("Escolha o tipo de média\n 1.aritmética\n2.ponderada(3,3,4)")
escolha = int(input())
def Calculo():
    if escolha == 1:
        return (nota1+nota2+nota3)/3
    elif escolha == 2:
        return(nota1*3+nota2*3+nota3*4)/10
    else:
        print("Opção Inválida")
print("Média = ", round(Calculo(),2))