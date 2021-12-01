import mysql.connector
import time
import menu

class Conta:

    con = mysql.connector.connect(host ='localhost', database = 'db_users', user = 'root', password ='12341234')
    cursor = con.cursor()

    def __init__(self,email):

        self.email = email

    def VerSaldo(self):

        self.cursor.execute(f"select saldo from tb_users where email = '{self.email}'")

        saldo = self.cursor.fetchone()

        print(f"saldo de {self.username[0].rstrip()} = {saldo[0]}")

        time.sleep(2)
        
        self.Menu()

    def Sacar(self,qtd):

        self.cursor.execute(f"select saldo from tb_users where email = '{self.email}'")

        saldo = self.cursor.fetchone()

        if saldo[0]<= 0 or saldo[0]<float(qtd):

            print("|-----Saldo Insuficiente, deposite algum valor-----|")

            time.sleep(2)

            self.Menu()

        else:

            self.cursor.execute(f"update tb_users set saldo = {float(saldo[0])-float(qtd)} where email = '{self.email}'")

            self.con.commit()

            print("|-----Saque efetuado com sucesso-----|")

            time.sleep(2)

            self.Menu()

    def Depositar(self,qtd):

        self.cursor.execute(f"select saldo from tb_users where email = '{self.email}'")

        saldo = self.cursor.fetchone()

        self.cursor.execute(f"update tb_users set saldo = {float(saldo[0])+float(qtd)} where email = '{self.email}'")

        self.con.commit()

        print("|-----Deposito efetuado com sucesso-----|")

        time.sleep(2)

        self.Menu()  

    def Gerenciar(self):

        print('-----Bem vindo(a) ao menu de gerenciamento de conta-----')

        escolha=int(input('-----o que deseja fazer?-----\n1)  |-----Alterar senha-----|  \n2)  |-----Excluir conta-----|  \n'))

        if escolha == 1:

            verificar=input('|-----informe sua senha atual-----|\n')

            self.cursor.execute(f"select senha from tb_users where email = '{self.email}'")

            verif = self.cursor.fetchone()

            if verificar == verif[0]:

                senha=input('|-----informe sua nova senha-----|\n')

                self.cursor.execute(f"update tb_users set senha = '{senha}' where email = '{self.email}'")

                self.con.commit()

                time.sleep(1)

                self.Menu()

        elif escolha == 2:

            ask=int(input('|-----tem certeza que deseja excluir sua conta?-----|\n |-----1-sim 2-não-----|\n'))

            if ask == 1:

                verif=input('|-----informe sua senha atual-----|\n')

                self.cursor.execute(f"delete from tb_users where senha = '{verif}' and email = '{self.email}'")

                self.con.commit() 

                print("|-----Conta Excluida com êxito-----|")

                time.sleep(2)   

                menu.Men.Menu()

    def TransferirPara(self,usuario):

        try:

            qtd= float(input("|-----Quanto deseja transferir?-----|\n"))

        except:

            print("|-----Digite um valor válido!-----|")

            self.TransferirPara(usuario)

        self.cursor.execute(f"select saldo from tb_users where email = '{self.email}'")

        saldo = self.cursor.fetchone()

        if saldo[0]>0 or saldo[0]>=qtd:

            self.cursor.execute(f"update tb_users set saldo = {float(saldo[0])-float(qtd)} where email = '{self.email}'")

            self.con.commit()

            self.cursor.execute(f"select saldo from tb_users where email = '{usuario}'")

            saldo = self.cursor.fetchone()

            self.cursor.execute(f"update tb_users set saldo = {float(saldo[0])+float(qtd)} where email = '{usuario}'")

            self.con.commit()

            time.sleep(2)

            self.Menu()

        else:

            print("|-----Saldo Insuficiente, deposite algum valor!-----|")

            self.Menu()

    def Menu(self):

        self.cursor.execute(f"select username_razao from tb_users where email = '{self.email}'")

        self.username = self.cursor.fetchone()

        print(f"|-----Bem Vindo(a) {self.username[0].rstrip()}-----|")  

        print("|------------Menu principal-----------|")

        desc=int(input('1)  |-----Ver Saldo-----|\n2)  |-----Saque-----|\n3)  |-----Depositar-----|\n4)  |-----Transferir-----|\n5)  |-----Gerenciamento de Conta-----|\n6)  |-----Sair-----|\n'))

        if desc == 1:

            self.VerSaldo()

        elif desc == 2:

            qtd = input("|-----Quanto deseja Sacar?-----|\n")

            self.Sacar(qtd)

        elif desc == 3:

            qtd = input("|-----Quanto deseja depositar?-----|\n ")

            self.Depositar(qtd)

        elif desc == 4:

            usuario = input("|-----Para quem deseja transferir?(Digite o email cadastrado do usuario)-----|\n ")

            self.TransferirPara(usuario)

        elif desc == 5:

            self.Gerenciar()

        elif desc == 6:  
            menu.Men.Menu()
            