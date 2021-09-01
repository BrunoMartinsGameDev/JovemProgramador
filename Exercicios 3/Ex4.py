'''4.As maçãs custam R$1,30 cada se forem compradas menosde uma dúzia,
e R$1,00se forem compradas pelo menos 12.
Escreva um programaque leia o número de maçãs 
compradas, calcule e escreva o custo total dacompra.'''
maca = int(input("Quantas maças voce comprou? "))
if maca>11:
    print("O total é de",maca,"reais")
else:
    print("O total é de",maca*1.3,"reais")