# Exercício Extra 4
# De acordo com as duas listas a seguir,
# multiplique todos os itens da lista B pelos itensda lista A
# e armazene na lista C:
# A=[1,2,3,4,5];
# B=[6,7,8,9,10]
# Resultado: C = [6, 7, 8, 9, 10,
#                 12, 14, 16, 18, 20,
#                 18, 21, 24, 27, 30,
#                 24, 28, 32, 36, 40,
#                 30, 35, 40, 45, 50]
A = [1,2,3,4,5]
B = [6,7,8,9,10]
C = []
for i in A:
    for j in B:
        C.append(i*j)
print(C)