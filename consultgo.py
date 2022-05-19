from PyQt5 import  uic,QtWidgets
import sqlite3


def chama_segunda_tela():
    primeira_tela.label_4.setText("")
    nome_usuario = primeira_tela.lineEdit.text()
    senha = primeira_tela.lineEdit_2.text()
    banco = sqlite3.connect('banco_cadastro.db') 
    cursor = banco.cursor()
    try:
        cursor.execute("SELECT senha FROM cadastro WHERE login = '{}'".format(nome_usuario))
        senha_bd = cursor.fetchall() 
        print(senha_bd[0][0])
        banco.close()
    except:
        print("Erro ao validar o login")
        
    if senha == senha_bd[0][0]:
        primeira_tela.close()
        segunda_tela.show()
    else :
        primeira_tela.label_4.setText("Dados de login incorretos!")
    

def logout():
    segunda_tela.close()
    primeira_tela.show()

def abre_tela_cadastro():
    tela_cadastro.show()


def cadastrar():
    nome = tela_cadastro.lineEdit.text()
    login = tela_cadastro.lineEdit_2.text()
    registro = tela_cadastro.lineEdit_3.text()
    especiali = tela_cadastro.lineEdit_4.text()
    telefone = tela_cadastro.lineEdit_5.text()
    mail = tela_cadastro.lineEdit_6.text()
    senha = tela_cadastro.lineEdit_7.text()
    c_senha = tela_cadastro.lineEdit_8.text()

    if (senha == c_senha):
        try:
            banco = sqlite3.connect('banco_cadastro.db') 
            cursor = banco.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS cadastro (nome text,login text,registro text,especiali text,telefone text,mail text,senha text)")
            cursor.execute("INSERT INTO cadastro VALUES ('"+nome+"','"+login+"','"+registro+"','"+especiali+"','"+telefone+"','"+mail+"','"+senha+"')")

            banco.commit() 
            banco.close()
            tela_cadastro.label_2.setText("Usuario cadastrado com sucesso")

        except sqlite3.Error as erro:
            print("Erro ao inserir os dados: ",erro)
    else:
        tela_cadastro.label_2.setText("As senhas digitadas estão diferentes")
    


app=QtWidgets.QApplication([])
primeira_tela = uic.loadUi("primeira_tela.ui")
segunda_tela = uic.loadUi("segunda_tela.ui")
tela_cadastro = uic.loadUi("tela_cadastro.ui")
primeira_tela.pushButton.clicked.connect(chama_segunda_tela)
segunda_tela.pushButton.clicked.connect(logout)
primeira_tela.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
primeira_tela.pushButton_3.clicked.connect(abre_tela_cadastro)
tela_cadastro.pushButton.clicked.connect(cadastrar) 


primeira_tela.show()
app.exec()