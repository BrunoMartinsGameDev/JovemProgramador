#7.Foi feita uma pesquisa entre os habitantes de uma região e coletados os dados de 
# altura e sexo(0=masc,1=fem) das pessoas.
# Faça um programa que leia 10 dados diferentes e informe:
# a.a maior e a menor altura encontradas;
# b.a média de altura das mulheres;
# c.a média de altura da população;
# d.o percentual de homens na população.
homi = []
totalHomi = 0
muie = []
totalMuie = 0
todos = []
totalTodos = 0
for i in range(0,10):
    print("Altura:",i+1)
    choice = int(input("Altura é de homem ou mulher?(0=M,1=F)\n"))
    altura = float(input("Digite a Altura:\n "))    
    if choice == 0:
        homi.append(altura)
        todos.append(altura)
        totalHomi += altura
        totalTodos += altura
    elif choice == 1:
        muie.append(altura)
        todos.append(altura)
        totalMuie += altura
        totalTodos += altura
    else:
        print("Codigo invalido!")
        break        
print("Maior altura encontrada: ",max(todos))
print("Menor altura encontrada: ",min(todos))
print("Média das mulheres:",totalMuie/len(muie))
print("Média de todos:",totalTodos/len(todos))
print("Percentual de homis:",(len(homi)/len(todos))*100,"%")

    
