altura = float(input("Eai, qual é sua altura? "))
sexo = str(input("Qual seu sexo?(M) OU (F) "))
if sexo == 'M' or sexo == 'm':
    pesoIdeal = (72.7*altura)-58
    print("Seu peso ideal é:",pesoIdeal)
elif sexo == 'F' or sexo == 'f':
    pesoIdeal = (62.1*altura)-44.7
    print("Seu peso ideal é:",pesoIdeal)
else:
    print("Sexo Invalido")
