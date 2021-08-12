saldoMedio = float(input("Qual foi seu Saldo médio no ultimo ano? "))
if saldoMedio<=200:
    print("Uma pena mas você não esta apto a receber nenhum crédito especial")
elif saldoMedio<=400:
    credito = saldoMedio*0.2
    print("Parabéns, você recebeu R$",credito,"de crédito especial!")
elif saldoMedio<=600:
    credito = saldoMedio*0.3
    print("Parabéns, você recebeu R$",credito,"de crédito especial!")
elif saldoMedio>600:
    credito = saldoMedio*0.4
    print("Parabéns, você recebeu R$",credito,"de crédito especial!")