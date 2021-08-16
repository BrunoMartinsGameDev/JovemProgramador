print("BEM VINDO AO CONTADOR DE DIAS PASSADOS!")
print("")
Programa()
def Programa():
        diasNoMes = 0
        diasCorridos = 0
    def DiasDoMes(mes):
        if (mes<8 and mes%2 != 0) or (mes>7 and mes%2 == 0):
            diasNoMes = 31
        elif mes == 2:
            diasNoMes == 28
        else:
            diasNoMes = 30   
        return diasNoMes      
    def DiasNumPeriodoDoTempo(mesAtual, anoAtual):
        while anoAtual-1>primeiroAno:
            diasCorridos = diasCorridos + 365
            mesAtual-=1
        while mesAtual-1>primeiroMes:
            diasCorridos = diasCorridos + DiasDoMes(mesAtual)        
            mesAtual-=1
        diasCorridos = diasCorridos + (DiasDoMes(primeiroMes)-primeiroDia)+ ultimoDia        
        return diasCorridos
    primeiroDia int(input("A partir de que dia você desejar contar?"))
    primeiroMes int(input("A partir de que mês você desejar contar?(em numero, ex: agosto = 8)"))
    primeiroAno int(input("A partir de que ano você desejar contar?"))
    ultimoDia int(input("Até que dia você desejar contar?"))
    ultimoMes int(input("Até que mês você desejar contar?(em numero, ex: agosto = 8)"))
    ultimoAno int(input("Até que ano você desejar contar?"))
    if (primeiroMes>12 or primeiroMes<1) or (ultimoMes >12 or ultimoMes <1):
        print("Mes Inexistente")
        Programa()
    elif (primeiroDia>DiasDoMes(primeiroMes) or primeiroDia<1) or (ultimoDia >DiasDoMes(ultimoMes) or ultimoDia <1):
        print("Dia Inexistente")
        Programa()
    #FEITO
    if ultimoAno < primeiroAno:
        print("Nós não voltamos para o passado, por favor tente novamente!")
        Programa()
    #COMPLETO
    else:
        #COMPLETO
        if ultimoMes < primeiroMes and ultimoAno==primeiroAno:
            print("Nós não voltamos para o passado, por favor tente novamente!")
            Programa()   
        #COMPLETO     
        elif ultimoMes == primeiroMes:
            if ultimoDia < primeiroDia:
                print("Nós não voltamos para o passado, por favor tente novamente!")
                Programa()            
            elif ultimoDia == primeiroDia:
                print("Nenhum dia se passou!")
            else:
                print(ultimoDia-primeiroDia,"dias se passaram!")
        #COMPLETO
        else:
            print(DiasNumPeriodoDoTempo(ultimoMes,ultimoAno),"dias se passaram!")