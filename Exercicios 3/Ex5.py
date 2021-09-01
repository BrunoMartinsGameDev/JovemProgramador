#5.Ler o ano atual e o ano de nascimento de uma pessoa.
#Escrever uma mensagemque diga se ela 
#poderá ou não votar este ano (nãoé necessário considerar o mêsem que a pessoa nasceu).
from datetime import datetime
anoAtual = int(datetime.today().strftime('%Y'))
anoNascimento = int(input("Que ano voce nasceu? "))
if anoAtual-anoNascimento>17:
    print("Voce pode votar!")
else:
    print("Voce ainda nao pode votar!")