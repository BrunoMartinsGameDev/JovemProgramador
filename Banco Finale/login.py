import mysql.connector
from conta import Conta
import menu

class Login:

    con = mysql.connector.connect(host ='localhost', database = 'db_users', user = 'root', password ='12341234')

    cursor = con.cursor() 

    def TeladeLogin(self):
        self.con = mysql.connector.connect(host ='localhost', database = 'db_users', user = 'root', password ='12341234')

        self.cursor = self.con.cursor() 

        self.email = input("|-----Digite seu email cadastrado-----|\n")

        self.VerificaCredencias("email", self.email)

        self.senha = input("|-----Digite sua senha-----|\n")

        self.VerificaCredencias("senha",self.senha)

    def VerificaCredencias(self, tipo, variavel):

        if tipo =="email":

            self.emailExiste = False

            self.cursor.execute("select email from tb_users;")

            correioEletronico = self.cursor.fetchall()

            for i in correioEletronico:

                if variavel == i[0]: 

                    self.emailExiste = True

                    pass

            if not self.emailExiste:        

                print("|-----Email não encontrado, tente novamente!-----|")
                menu.Men.Menu()

        elif tipo == "senha":

            self.cursor.execute(f"select senha from tb_users where email = '{self.email}';")

            senhas = self.cursor.fetchall()
            print(senhas)

            for i in senhas:

                if variavel == i[0]:

                    print("|-----Login autorizado-----|\n")

                    Conta(self.email).Menu()

                else:

                    print("|-----Senha errada, tente novamente!-----|")

                    self.TeladeLogin()