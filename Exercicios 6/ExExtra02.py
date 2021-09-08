#Extra 2
# Desenha moldura.
# Construa uma função que desenhe um retângulo usandoos caracteres ‘+’, ‘−’ e ‘| ‘.
# Esta função deve receber dois parâmetros, linhase colunas,
# sendo que o valor por omissão é o valor mínimo iguala 1 e o valormáximo é 20.
# Se valores fora da faixa forem informados, elesdevem ser modificados
# para valores dentro da faixa de forma elegante.
linhas = int(input("Informe quantas linhas tera seu retangulo(max 20): "))
colunas = int(input("Informe quantas colunas tera seu retangulo(max 20): "))
if colunas <1:
    colunas = 1
elif colunas>20:
    colunas = 20
if linhas <1:
    linhas = 1
elif linhas>20:
    linhas = 20
print("-"*colunas)
for i in range(0,linhas):
    
    print("|"+("+"*(colunas-2))+"|")
print("-"*colunas)