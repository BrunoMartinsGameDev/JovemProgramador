#3.A prefeitura de uma cidade fez uma pesquisa entre seus habitantes,coletando dados sobre o salário e número de filhos.
#A prefeitura deseja saber:
# a.média do salário da população;
# b.média do número de filhos;
# c.maior salário;
# d.percentual de pessoas com salário até R$1000,00.
salario = [1000,15000,2000,500,700,900,1898]
filhos = [2,0,1,3,2,1,0]
salarioTotal = 0
for i in range(0,len(salario)):
    salarioTotal+=salario[i]
print("média do salário é", salarioTotal/len(salario))
filhosTotal = 0
for i in range(0,len(filhos)):
    filhosTotal+=filhos[i]
print("média de filhos é",filhosTotal/len(filhos))
print("Maior salário é de",max(salario))
count = 0
for i in salario:
    if i<=1000:
        count+=1
print("Porcentagem com pessoas com salario com menos de 1000 reais é:",round((count/len(salario))*100,2),"%")