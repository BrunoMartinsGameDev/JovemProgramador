from login import Login
from Registrer import Registrer

class Men:

    def Menu():

        print("|-----Bem vindo ao social bank!-----|\n|-----Oque deseja fazer?-----|\n|-----1.Logar-----|\n|-----2.Registrar-----|\n|-----3.Sair-----|")

        log = Login()

        regis = Registrer()

        choice = int(input())

        if choice == 1:

            log.TeladeLogin()

        elif choice == 2:

            regis.InsercaoDeRegistro()

        elif choice == 3:

            exit()

        else:

            print("|-----ERRO-----|")
            print("|-----Valor inválido-----|")