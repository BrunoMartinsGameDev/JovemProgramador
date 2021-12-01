from time import time
import mysql.connector
import re
from datetime import date
import menu
import time

class Registrer:

    con = mysql.connector.connect(host ='localhost', database = 'db_users', user = 'root', password ='12341234')

    if con.is_connected():
        print("Conexão:", con)
        
    cursor = con.cursor()
    print(cursor)

    def InsercaoDeRegistro(self):        
        if self.ValidacoesDeRegistro("username"):

            if self.ValidacoesDeRegistro("senha"):

                if self.ValidacoesDeRegistro("email"):

                    if self.ValidacoesDeRegistro("cpf_cnpj"):

                        if self.ValidacoesDeRegistro("tipo_conta"):   

                            if self.ValidacoesDeRegistro("data_NASC"):
                                self.cursor.execute(f"insert into tb_users (email, senha, username_razao, saldo, tipoCONTA, cpf_cnpj, data_NASC)\
                                     values ('{self.email}','{self.senha}','{self.username}',0,{self.tipoConta},{self.cpfOuCnpj},'{self.aniver}');")                             
                                self.con.commit()
                                self.cursor.close()
                                menu.Men.Menu()

    def ValidacoesDeRegistro(self,type):

        if type == "username":

            self.username = input("|-----Digite seu nome de Usuário-----|\n") 

            return True

        elif type == "senha":

            self.senha = input("|-----Digite sua senha(somente numeros)-----|\n")

            self.repeatSenha = input("|-----Digite sua senha novamente(somente numeros)-----|\n")

            if self.senha == self.repeatSenha:

                try:

                    if self.senha == str(int(self.senha)):

                        return True

                except:

                    print("|-----Senha somente numeros!-----|")

                    self.InsercaoDeRegistro()
            else:

                print("|-----Senhas diferentes!-----|")

                self.InsercaoDeRegistro()

        elif type == "email":

            self.email = input("|-----Digite seu email-----|\n")

            pattern = re.compile(r"\"?([-a-zA-Z0-9.`_?{}]+@\w+\.\w+)\"?")

            emails = [self.email]

            for i in emails:

                if not re.match(pattern, i):

                    print (f"ERRO X84, seu PC se irá explodir em:")

                    time.sleep(1)

                    print("3.....")

                    time.sleep(1)

                    print("2.....")

                    time.sleep(1)

                    print("1.....")

                    time.sleep(1)

                    print("HAHAHA")

                    print("você caiu no conto do relâmpago marquinhos")

                    self.InsercaoDeRegistro()    

                else:

                    self.emailExiste = False

                    self.cursor.execute("select email from tb_users;")

                    correioEletronico = self.cursor.fetchall()

                    for i in correioEletronico:

                        if self.email == i[0]:    

                            print(f"|-----Email já existente-----|")

                            self.emailExiste = True

                            self.InsercaoDeRegistro()

                    if not self.emailExiste:      

                        return True

        elif type == "cpf_cnpj":
            cpfCnpjExiste = False
            self.cpfOuCnpj = input("|-----Insira seu CPF ou CNPJ-----|\n")

            if len(self.cpfOuCnpj) == 11 or len(self.cpfOuCnpj) == 14:

                self.cursor.execute("select cpf_cnpj from tb_users;")

                sla=self.cursor.fetchall()
                for i in sla:
                    if int(self.cpfOuCnpj) == int(i[0]):
                        cpfCnpjExiste = True
                        print(i[0])

                        print("|-----Cpf ou Cnpj já existente no banco de dados-----|")
                        time.sleep(1.2)
                        self.InsercaoDeRegistro()    
                if cpfCnpjExiste == False:
                    return True                

                else:                
                    print("CPF/CNPJ invalido, tente novamente!")
                    time.sleep(2)
                    self.InsercaoDeRegistro()

        elif type == "tipo_conta":       

            try:

                self.tipoConta = int(input("|-----Que tipo de conta deseja criar?(0.Conta Corrente 1.Conta Poupança)-----|\n"))

                if self.tipoConta == 0:

                    return True

                elif self.tipoConta == 1:

                    return True

                else:

                    print("|-----Código Inválido!!!!-----|")

                    self.InsercaoDeRegistro()

            except:

                print("ERRO x84, seu PC irá em explodir em:")

                time.sleep(1)

                print("3....")

                time.sleep(1)

                print("2....")

                time.sleep(1)

                print("Tá parei,suhauhsa")

                time.sleep(2)

                self.InsercaoDeRegistro()

        elif type == "data_NASC":

            try:

                dia = int(input("|-----Digite o dia de seu nascimento-----|\n"))

                mes = int(input("|-----Digite o mes de seu nascimento-----|\n"))

                ano = int(input("|-----Digite o ano de seu nascimento-----|\n"))

            except:

                print("|-----Formato incorreto, digite apenas numeros-----|")

                self.InsercaoDeRegistro()       

            self.aniver = date(ano,mes,dia)    
            print(self.aniver)
            def calculate_age():

                born = self.aniver

                today = date.today()

                extra_year = 1 if ((today.month, today.day) < (born.month, born.day)) else 0

                return today.year - born.year - extra_year

            if calculate_age()<18:

                print("SAI DAQUI MENOR")

                self.InsercaoDeRegistro()

            else:

                print("FBI, OPEN UP")

                return True