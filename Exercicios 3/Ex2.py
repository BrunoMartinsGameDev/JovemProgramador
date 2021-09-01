'''2.Crie um algoritmo que leia quatro valores digitadospelo usuário: n, a, b, c.
a.Se n = 1 imprimir os três valores a, b, c em ordem crescente.
b.Se n = 2 escrever os três valores a, b, c em ordemdecrescente.
c.Se n = 3 escrever os três valores a, b, c de formaque o maior fique no meio'''
n = int(input("Digite um valor de 1 a 3 "))
a = int(input("Digite um valor "))
b = int(input("Digite um valor "))
c = int(input("Digite um valor "))
lista= []
lista.append(a)
lista.append(b)
lista.append(c)
if n == 1:
    lista.sort()
    print(lista)
elif n == 2:
    lista.sort()
    lista.reverse()
    print(lista)
elif n == 3:
    lista2 = []#to sem criatividade pra dar nome pra variavel
    if a>b and a>c:
        lista2 = [b,a,c]
    elif b>a and b>c:
        lista2 = [a,b,c]
    elif c>a and c>b:
        lista2 = [b,c,a]
    else:
        print("Opa!")
    print(lista2)
else:
    print("numero invalido porra")

