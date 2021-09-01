# Exercício 5
# Faça um algoritmo que receba o peso de uma pessoa,calcule e mostre:
# a) o novo peso se a pessoa engordar 15% sobre opeso digitado
# b) o novo peso se a pessoa emagrecer 20% sobre opeso digitado
peso = float(input("Quanto você pesa? "))
print("Se voce engordar 15% desse peso ficara com:", round(peso*1.15,2),"mas se emagrecer 20% deste peso ficara com",round(peso*0.8,2))
