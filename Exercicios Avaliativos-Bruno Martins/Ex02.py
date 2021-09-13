#2.Faça um algoritmo que receba o ano de nascimento de uma pessoa e o ano atual,calcule e mostre:
# a.a idade dessa pessoa em anos;
# b.a idade dessa pessoa em meses;
# c.a idade dessa pessoa em dias; (considere mês sempre com 30 dias)
# d.a idade dessa pessoa em semanas.(considere que há exatamente 4semanas em cada mês)
import datetime
currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
#pega automaticamente o ano atual do computador
anoAtual = int(date.strftime("%Y"))
anoNasc = int(input("Em que ano você nasceu?"))
#Lidando com exeções
if anoNasc>anoAtual:
    print("Você veio do futuro?")
#Lida com os calculos de cada parte e os prints
else:
    print("você ja viveu em anos:", anoAtual-anoNasc,"anos")
    print("você ja viveu em meses:", (anoAtual-anoNasc)*12,"meses")
    print("você ja viveu em dias:", (anoAtual-anoNasc)*12*30,"dias")
    print("você ja viveu em semanas:", (anoAtual-anoNasc)*12*4,"semanas")