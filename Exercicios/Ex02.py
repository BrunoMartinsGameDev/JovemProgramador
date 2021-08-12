valorPao = 0.12
valorBroa = 1.5 
qntPao = int(input("Quantos paes você vendeu hoje? "))
qntBroa = int(input("Quantas broas voce vendeu hoje? "))
arrecadamento = float(valorBroa*qntBroa + valorPao*qntPao)
poupanca = float(arrecadamento * 0.1)
print("Você arrecadou R$",arrecadamento,"e deve reservar R$",poupanca,"na sua poupança!")