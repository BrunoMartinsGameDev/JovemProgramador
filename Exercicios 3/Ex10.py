#Chico tem 1,50m e cresce 2 centímetros por ano,
#enquanto Juca tem 1,10m ecresce 3 centímetros por ano.
#Construir um algoritmoque calcule e imprima 
#quantosanos serão necessários para que Juca seja maior queChico. (Usar While)
chico = 1.5
juca = 1.10
anos = 0
while juca<=chico:
    juca+=0.03
    chico+=0.02
    anos+=1
print("Demorou",anos,"anos pro juca ser maior que chico")
print("Chico =",round(chico,2))
print("Juca =",round(juca,2))