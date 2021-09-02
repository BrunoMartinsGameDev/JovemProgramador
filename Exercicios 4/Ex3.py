# Exercício 3
# Em uma eleição presidencial existem quatro candidatos.
# Os votos são informados através de códigos.
# Os dados utilizados para a contagem dos votos obedecemà seguintecodificação:
# - 1,2,3,4 = voto para os respectivos candidatos;
# - 5 = voto nulo;
# - 6 = voto em branco;
# Elabore um algoritmo que leia o código do candidatoem um voto.
# Calcule e escreva:
# - total de votos para cada candidato;
# - total de votos nulos;
# - total de votos em branco;
# Faça um algoritmo para ler 10 votos.
# Ou se digitar zero sai do laço de repetição.

i=0
joao = 0
carlos = 0
jessica = 0
almirante = 0
nulo = 0
branco = 0
while i<10:
    voto = int(input("Em qual candidato deseja votar? \n1.Joao\n2.Carlos\n3.Jessica\n4.Almirante\n5.Nulo\n6.Branco\n\n0.Parar de votar"))
    if voto ==1:
        joao+=1
    elif voto ==2:
        carlos+=1
    elif voto ==3:
        jessica+=1
    elif voto ==4:
        almirante+=1
    elif voto ==5:
        nulo+=1
    elif voto ==6:
        branco+=1
    elif voto ==0:
        break
    else:
        print("Código invalido")
        i-=1
    i+=1
print("Votação encerrada")
print("Joao:",joao,"Votos")
print("Carlos:",carlos,"Votos")
print("Jessica:",jessica,"Votos")
print("Almirante:",almirante,"Votos")
print("Nulo:",nulo,"Votos")
print("Branco:",branco,"Votos")
