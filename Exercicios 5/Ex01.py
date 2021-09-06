#1.Escreva um programa que converta um intervalo de tempo 
# dado em minutos,em horas,minutos e segundos.
# Por exemplo,se o tempo dado for 145,87 minutos,o programa deve fornecer 2 h 25 min 52,2 s
tempoMin = float(input("Digite um tempo em minutos: "))
timeHoras = int(tempoMin/60)
timeMinutos = int(tempoMin-60*timeHoras)
timeSegundos = ((tempoMin)-int(tempoMin))*60
print(timeHoras,"H",timeMinutos,"min",round(timeSegundos,2),"s")