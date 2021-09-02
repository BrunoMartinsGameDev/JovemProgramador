#9.Faça um algoritmo que leia tantos números quanto o usuário desejar e imprima a soma deles.
total = 0
true = True
while true:
    num = float(input("Digite um numero:\nDigite 0 se deseja sair:\n"))
    if num ==0:
        print("Código encerrado")
        print("Total:",total)
        true = False
        break
    else:
        total += num
        print("Total:",total)
    