print("Especificação Código Preço\n"+
"Cachorro quente 100 1,20\n"+
"Bauru simples   101 1,30\n"+
"Bauru com ovo   102 1,50\n"+
"Hambúrger       103 1,20\n"+
"Cheeseburguer   104 1,30\n"+
"Refrigerante    105 1,00")
codigoItem = int(input("Por favor, digite o código do produto que deseja "))
qtd = int(input("Agora informe a quantidade que deseja "))

def TotalAPagar():
    valor = ""
    if codigoItem == 100:
        valor = 1.20
    elif codigoItem == 101:
        valor = 1.30
    elif codigoItem == 102:
        valor = 1.50
    elif codigoItem == 103:
        valor = 1.20
    elif codigoItem == 104:
        valor = 1.30
    elif codigoItem == 105:
        valor = 1.00
    if codigoItem >99 and codigoItem <106:
        return print("Ficou um total de R$", qtd*valor , ",vai ser no cartão?")
    else:
        return print("Código Inválido")
TotalAPagar()  

