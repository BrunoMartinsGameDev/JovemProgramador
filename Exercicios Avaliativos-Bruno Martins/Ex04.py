#4.Elaborar um algoritmo que lê 2 valores a e b e os escreve com a mensagem:
# "São múltiplos" ou "Não são múltiplos"
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
#Verifica se a e b sao multiplos entre si, não importando qual é o maior numero
if a%b ==0 or b%a == 0:
    print("Eles são múltiplos")
else:
    print("Não são múltiplos")
