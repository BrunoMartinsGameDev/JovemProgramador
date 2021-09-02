#4.Faça um programa que calcule e escreva a seguinte soma:soma=1/1 + 3/2 + 5/3 + 7/4 + ... + 99/50.
import time
deCima = 1
deBaixo = 1
total = 0
for i in range(0,50):
    divisao = deCima/deBaixo
    print("foi dividido",deCima,"/",deBaixo)
    print("divisao=",divisao)
    total+=divisao
    deCima+=2
    deBaixo+=1
    time.sleep(0.5)
print("Total =", total)