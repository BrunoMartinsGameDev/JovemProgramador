horastrabalhadas = int(input("Quantas horas você trabalhou hoje? "))
horasExtras = int(input("E quantas horas extras você fez hoje?"))
salarioDoDia = horastrabalhadas*10 + horasExtras*15
salarioLiquido = salarioDoDia*0.9
print("Parabens, hoje voce recebeu R$", salarioDoDia)
print("Mas como o governo é OLHUDO ele tomou parte do seu salário, então receberás no fim R$",salarioLiquido)