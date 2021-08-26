palavraSecreta = str(input("Escreve a palavra a ser usada no jogo da Forca: "))
letrasDescobertas = []
vida = 3
def Iniciar():
    MensagemInicio()
    inserirPalavraOculta()
    pedirLetra()
    EndGame()
def MensagemInicio():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
def inserirPalavraOculta():
    for i in range(0, len(palavraSecreta)):
        letrasDescobertas.append("_")
    palavraDescoberta = "".join(letrasDescobertas)
    print(palavraDescoberta)
def pedirLetra():
    global vida
    acertou = False
    count = 0
    while acertou == False:
        letra = str(input("Digite uma letra: "))
        for i in range(0, len(palavraSecreta)):
            if letra == palavraSecreta[i]:
                count = 0
                letrasDescobertas[i] = letra
                count +=1   
        if count < 1:
            vida -= 1
            print("Você perdeu uma vida\n Vida igual a:", vida)         
        if vida == 0:
            print("Você perdeu!")
            break
        palavraDescoberta = "".join(letrasDescobertas)
        print(palavraDescoberta)
        if palavraDescoberta == palavraSecreta:
            print("VOCÊ GANHOU!")
            break
        acertou == True
        for x in range(0,len(letrasDescobertas)):
            if letrasDescobertas[x] == "_":
                acertou = False
def EndGame():
    print("Fim de Jogo")
