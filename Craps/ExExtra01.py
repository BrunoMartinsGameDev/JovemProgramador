#Extra 1
# Jogo de Craps.
# Faça um programa de implemente um jogo de Craps.
# O jogador lança um par de dados, obtendo um valorentre 2 e 12.
# Se, na primeira jogada, você tirar 7 ou 11, vocêum "natural" e ganhou.
# Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de"craps" e você perdeu.
# Se, na primeira jogada, você fez um 4, 5, 6, 8,9 ou 10,este é seu"Ponto".
# Seu objetivo agora é continuar jogando os dadosaté tirar este númeronovamente.
# Você perde, no entanto, se tirar um 7 antes de tirareste Pontonovamente.
# Seu jogo pode ser implementado com uma das seguintesopções dejogadores:
# 1) Jogo com dois jogadores.
# 2) Dar opção (1 à 6) jogadores.
import random
import time
from Player import Player

def Start():
    Menu()
def Dados():
    oi = input("Aperte Enter para girar os Dados")
    return random.randint(2,12)
def Menu():
    print("Bem vindo ao jogo do CRAPS")
    print("1. Iniciar Jogo\n2.Instruções\n3.Sair")
    opc = int(input(""))
    if opc == 1:
        print("Escolha com quantos Jogadores queres Jogar(de 1 até 6)\n0.Menu\n")
        choice = int(input(""))
        if choice >= 1 or choice <=6:
            MaisJogadores(choice)           
        elif choice == 0:
            Menu()
        else:
            print("Opção Inválida")
            Menu()
    elif opc == 2:
        Instructions()
    elif opc == 3:
        print("Jogo encerrado")
        exit()
    else:
        print("Opção Inválida")
        Menu()
def Instructions():
    print("O jogador lança um par de dados, obtendo um valorentre 2 e 12.")
    print("Se, na primeira jogada, você tirar 7 ou 11, você um natural e ganhou.")
    print("Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de craps e você perdeu.")
    print("Se, na primeira jogada, você fez um 4, 5, 6, 8,9 ou 10,este é seu Ponto.")
    print("Seu objetivo agora é continuar jogando os dadosaté tirar este númeronovamente.")
    print("Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente")
    opc = int(input("Digite 1 para voltar ao menu!\n"))
    if opc == 1:
        Menu()
    else:
        print("Opção Inválida")
        Instructions()
def MaisJogadores(qtdPlayers):
    true = True
    players = []
    for i in range(0,qtdPlayers):
        jogador = Player("Jogador "+str(i+1))
        players.append(jogador)  
    while true:  
        for i in players:            
            if i.getSePerdeu() == False:
                print("Rodada",i.rodada)
                print("Vez do",i.nome)
                pontoDaRodada = Dados()                
                print("Soma dos Dados =",pontoDaRodada)
                if i.rodada == 1:
                    if pontoDaRodada == 7 or pontoDaRodada == 11:
                        print("Você é um natural,",i.nome,"ganhou o Jogo")
                        true = False
                        break
                    elif pontoDaRodada == 2 or pontoDaRodada == 3 or pontoDaRodada == 12:
                        print("Você tirou um craps,",i.nome,"eliminado!")
                        i.sePerdeu = True
                    else:
                        i.setPoint(pontoDaRodada)
                        print("Seu ponto é:", i.getPoint())
                else:
                    if pontoDaRodada == i.getPoint():
                        print("Você tirou seu ponto novamente,",i.nome,"ganhou o Jogo")
                        true = False
                        break
                    elif pontoDaRodada == 7:
                        print("Você tirou o numero 7,um craps,",i.nome,"eliminado!")
                        i.sePerdeu = True
                    else:
                        print("Você ainda está no jogo", i.nome)
            else:
                for i in players:
                    count = 0
                    if i.sePerdeu == True:
                        count +=1
                        if count == len(players):
                            print("Todos os Jogadores foram eliminados, o Jogo acabou")
                            true = False
                            break                            
            i.rodada+=1
            time.sleep(1)
Start()