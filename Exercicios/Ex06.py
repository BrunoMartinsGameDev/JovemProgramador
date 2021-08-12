salario = float(input("Parabéns, você vai receber um aumento! \nPor favor me informe seu sálario atual pra ele poder ser atualizado: "))
salarioBruto = salario+(salario*0.15)
salarioLiquido = salarioBruto - salarioBruto*0.08
print("Parabens, antes voce recebia R$",salario,"Agora você receberá R$", salarioBruto)
print("Mas como o governo é OLHUDO ele tomou parte do seu salário, então receberás no fim R$",salarioLiquido)

