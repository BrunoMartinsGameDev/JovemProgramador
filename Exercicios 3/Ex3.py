'''3.Escreva um algoritmo para ler:
a.o número total de eleitores de um município
b.o número de votos brancos
c.nulos
d.válidos.
Calcular e escrever o percentual que cada um representaem relação
ao total deeleitores, e número de eleitores que não votaram.'''
eleitores = int(input("Quantos eleitores tem na cidade? "))
branco = int(input("Quantos votos brancos? "))
nulos = int(input("Quantos nulos? "))
validos = int(input("Quantos válidos? "))
porcBranco = (branco/eleitores)*100
porcNulos = (nulos/eleitores)*100
porcValidos = (validos/eleitores)*100
naoVotante = eleitores-(branco+nulos+validos)
porcNaoVotante = (naoVotante/eleitores)*100
print("Teve",round(porcBranco,2),"% votos Brancos. \nTeve",round(porcNulos,2),"% votos Nulos. \nTeve",round(porcValidos,2),"% votos Validos. \nTeve",round(porcNaoVotante,2),"% de nao votantes oque equivale a",naoVotante, "pessoas")