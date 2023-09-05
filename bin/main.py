import os
import cv2
import imutils
import paramiko
from bd import *
from info import *
import pysftp as sf
from PIL import Image
import mysql.connector
import PySimpleGUI as sg
from kivymd.app import MDApp
from datetime import datetime
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager

sg.theme(theme)
Window.size = (1100,620)
Window.set_system_cursor("hand")
data = (datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
faceCascade = cv2.CascadeClassifier("cascade/haarcascade_frontalface_default.xml")

class Menu(Screen):
    pass

class Cadastro(Screen):
    pass

class Dados(Screen):
    def salvarCamera(self):
        try:
            nome = self.ids.nome.text
            chapa = self.ids.chapa.text
            cpf = self.ids.cpf.text
            email = self.ids.email.text
            nivel = self.ids.nivel.text

            nome = nome.upper()
            chars = "''()[],. "
            nome = nome.translate(str.maketrans('', '', chars))

            con = mysql.connector.connect(host=host,database=database,user=user,password=password)
            cursor = con.cursor()
            cursor.execute(f"select * from cadastros where cpf='{cpf}' and chapa='{chapa}';")
            result = str(cursor.fetchall())
            chars = "''()[],"
            consulta = result.translate(str.maketrans('', '', chars))
            cursor.close()
            while True:
                if consulta != '':
                    resp = (sg.popup_yes_no('Já exixte um cadastro com este CPF, deseja atualizar ?', font='Arial 20'))
                    if resp == 'No':
                        return False

                    else:
                        webcam = cv2.VideoCapture(0)
                        try:
                            while True:
                                _, img = webcam.read()
                                faces = faceCascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=8, minSize=(25, 25))

                                for (x, y, w, h) in faces:
                                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
                                    contador = str(faces.shape[0])
                                    if contador > '1':
                                        sg.popup_auto_close('Mais de um rosto detectado', font='Arial 20')

                                img = imutils.resize(img, width=850)
                                cv2.imshow("Verificando face, aguardando retorno...", img)

                                if cv2.waitKey(1) & 0xFF == ord('q'):
                                    break

                            webcam.release()

                            imgName = f".banco/{chapa}.jpg"
                            cv2.imwrite(imgName, img)

                            with sf.Connection(address, username=username, password=password) as sftp:
                                with sftp.cd('faceid/banco'):
                                    sftp.put(imgName)

                            con = mysql.connector.connect(host=host,database=database,user=user,password=password)
                            cursor = con.cursor()
                            cursor.execute(f"update cadastros set nome='{nome}', chapa='{chapa}', email='{email}', nivel='{nivel}' where cpf='{cpf}';")
                            con.commit()
                            cursor.close()

                            sg.popup_auto_close('Cadastro atualizado com sucesso', font='Arial 20')
                            cv2.destroyAllWindows()
                            return False

                        except Exception as error:
                            error = str(error)
                            with open('log/log.dat', 'a') as file:
                                file.write(data + '\n' + 'log de novoCadastro\n' + error + '\n\n-------------------------------------------------------------------------------\n\n')
                            sg.popup_auto_close(f'Erro: {error}', font='Arial 20')
                            cv2.destroyAllWindows()
                            return False

                webcam = cv2.VideoCapture(0)
                while True:
                    _, img = webcam.read()
                    faces = faceCascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=8, minSize=(25, 25))

                    for (x, y, w, h) in faces:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
                        contador = str(faces.shape[0])
                        if contador > '1':
                            sg.popup_auto_close('Mais de um rosto detectado', font='Arial 20')

                    img = imutils.resize(img, width=850)
                    cv2.imshow("Verificando face, aguardando retorno...", img)

                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

                webcam.release()

                imgName = f".banco/{chapa}.jpg"
                cv2.imwrite(imgName, img)

                with sf.Connection(address, username=username, password=password) as sftp:
                    with sftp.cd('faceid/banco'):
                        sftp.put(imgName)

                con = mysql.connector.connect(host=host,database=database,user=user,password=password)
                cursor = con.cursor()
                cursor.execute('INSERT INTO cadastros (nome, chapa, email, cpf, nivel) VALUES (%s,%s,%s,%s,%s);', (nome, chapa, email, cpf, nivel))
                con.commit()
                cursor.close()

                sg.popup_auto_close('Cadastro realizado com sucesso', font='Arial 20')
                cv2.destroyAllWindows()
                return False
                
        except Exception as error:
            error = str(error)
            with open('log/log.dat', 'a') as file:
                file.write(data + '\n' + 'log de novoCadastro\n' + error + '\n\n-------------------------------------------------------------------------------\n\n')
            sg.popup_auto_close(f'Erro: {error}', font='Arial 20')
            cv2.destroyAllWindows()
            return False

class DadosManual(Screen):
    def salvarManual(self):
        try:
            nome = self.ids.nome.text
            chapa = self.ids.chapa.text
            cpf = self.ids.cpf.text
            email = self.ids.email.text
            nivel = self.ids.nivel.text

            nome = nome.upper()
            chars = "''()[],. "
            nome = nome.translate(str.maketrans('', '', chars))

            con = mysql.connector.connect(host=host,database=database,user=user,password=password)
            cursor = con.cursor()
            cursor.execute(f"select * from cadastros where cpf='{cpf}' and chapa='{chapa}';")
            result = str(cursor.fetchall())
            chars = "''()[],"
            consulta = result.translate(str.maketrans('', '', chars))
            cursor.close()

            if consulta != '':
                resp = (sg.popup_yes_no('Já exixte um cadastro com este CPF, deseja atualizar ?', font='Arial 20'))
                if resp == 'No':
                    return False
                else:
                    try:
                        foto = cv2.imread(sg.popup_get_file('Selecione uma foto', font='Arial 20'))
                        cv2.imshow("", foto)
                        cv2.waitKey(100)
                        imgName = f".banco/{chapa}.jpg"
                        cv2.imwrite(imgName, foto)

                        with sf.Connection(address, username=username, password=password) as sftp:
                            with sftp.cd('faceid/banco'):
                                sftp.put(imgName)

                        sg.popup_ok(f'Cadastro atualizado com sucesso', font='Arial 20')
                        cv2.destroyAllWindows()
                        con = mysql.connector.connect(host=host,database=database,user=user,password=password)
                        cursor = con.cursor()
                        cursor.execute(f"update cadastros set nome='{nome}', chapa='{chapa}', email='{email}', nivel='{nivel}' where cpf='{cpf}';")
                        con.commit()
                        cursor.close()
                        return False

                    except Exception as error:
                        error = str(error)
                        with open('log/log.dat', 'a') as file:
                            file.write(data + '\n' + 'log de update no cadastro manual\n' + error + '\n\n-------------------------------------------------------------------------------\n\n')
                        sg.popup_auto_close(f'Erro: {error}', font='Arial 20')
                        return False
                    
            foto = cv2.imread(sg.popup_get_file('Selecione uma foto', font='Arial 20'))
            cv2.imshow("", foto)
            cv2.waitKey(100)
            imgName = f".banco/{chapa}.jpg"
            cv2.imwrite(imgName, foto)

            con = mysql.connector.connect(host=host,database=database,user=user,password=password)
            cursor = con.cursor()
            cursor.execute('INSERT INTO cadastros (nome, chapa, email, cpf, nivel) VALUES (%s,%s,%s,%s,%s);', (nome, chapa, email, cpf, nivel))
            con.commit()
            cursor.close()

            with sf.Connection(address, username=username, password=password) as sftp:
                with sftp.cd('faceid/banco'):
                    sftp.put(imgName)

            cv2.destroyAllWindows()
            return False
            
        except Exception as error:
            error = str(error)
            with open('log/log.dat', 'a') as file:
                file.write(data + '\n' + 'log de cadastroManual\n' + error + '\n\n-------------------------------------------------------------------------------\n\n')
            sg.popup_auto_close(f'Erro: {error}', font='Arial 20')

class MainApp(MDApp):
    def build(self):
        self.root = Builder.load_file('lib/menu.kv')
        sm = ScreenManager()
        sm.add_widget(Menu())
        sm.add_widget(Cadastro())
        sm.add_widget(Dados())
        sm.add_widget(DadosManual())
        return sm

    def ident(self):
        os.system('python bin/identificacao.py')

    def lista_img(self):
        with open ('verifica/list.dat', 'w+') as file:
            file.write('')

        sg.theme(theme)
        lista = [
            [sg.Text('Escolha uma das opções', font='Arial 20')],
            [sg.Button('Imagens autorizadas', font='Arial 20', size=(20,0)), sg.Button('Imagens negadas', font='Arial 20', size=(20,0))],
            [sg.Button('Voltar', font='Arial 20', size=(20,0))]
        ]
        os.remove('verifica/list.dat')
        window = sg.Window("Lista", lista, element_justification='c')
        while True:
            e, v = window.read()

            if e == sg.WINDOW_CLOSED:
                window.close()
                return False
            elif e == 'Voltar':
                window.close()
                return False

            elif e == 'Imagens autorizadas':
                try:
                    remotepath = 'faceid/tentativas/autorizadas'
                    ssh = paramiko.SSHClient()
                    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    ssh.connect(hostname=address, username=username, password=password)
                    stdin, stdout, stderr = ssh.exec_command('ls faceid/tentativas/autorizadas')
                    stdin.close()

                    with open('verifica/list.dat', 'a') as file:
                        file.write('==============================================\n AUTORIZADAS \n\n')

                    for line in stdout.readlines():
                        dados = str(line)
                        with open('verifica/list.dat', 'a') as file:
                            file.write(dados + '\n')

                    file = open('verifica/list.dat', 'r', encoding='utf-8')
                    file = file.read()
                    window.close()

                except Exception as error:
                    error = str(error)
                    window.close()
                    sg.popup_ok(f'Erro: {error}', font='Arial 20')
                    error = str(error)
                    data = (datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    with open('log/log.dat', 'a') as file:
                            file.write(data + '\n' + 'log de lista\n' + error + '\n\n-------------------------------------------------------------------------------\n\n')
                    return False

            elif e == 'Imagens negadas':
                try:
                    remotepath = 'faceid/tentativas/negadas'
                    ssh = paramiko.SSHClient()
                    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    ssh.connect(hostname=address, username=username, password=password)
                    stdin, stdout, stderr = ssh.exec_command('ls faceid/tentativas/negadas')
                    stdin.close()

                    with open('verifica/list.dat', 'a') as file:
                        file.write('==============================================\n NEGADAS \n\n')

                    for line in stdout.readlines():
                        dados = str(line)
                        with open('verifica/list.dat', 'a') as file:
                            file.write(dados + '\n')

                    file = open('verifica/list.dat', 'r', encoding='utf-8')
                    file = file.read()
                    window.close()

                except Exception as error:
                    error = str(error)
                    window.close()
                    sg.popup_ok(f'Erro: {error}', font='Arial 20')
                    error = str(error)
                    data = (datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    with open('log/log.dat', 'a') as file:
                            file.write(data + '\n' + 'log de lista\n' + error + '\n\n-------------------------------------------------------------------------------\n\n')
                    return False

            lista = [
                [sg.Multiline(file, size=(95,35))],
                [sg.Text('Escreva o nome da imagem', font='Arial 20'), sg.Input(key='img', font='Arial 15', size=(25,1))],
                [sg.Button('Voltar', font='Arial 15', size=(20,0)), sg.Button('Abrir imagem', font='Arial 15', size=(20,0))]
            ]
            window = sg.Window("Imagens", lista, element_justification='c')

            while True:
                e, v = window.read()
                if e == sg.WINDOW_CLOSED:
                    window.close()
                    return False

                elif e == 'Voltar':
                    window.close()
                    return False

                elif e == 'Abrir imagem':
                    img = v['img']
                    if img == '':
                        sg.popup_ok('Favor digitar o nome da imagem que deseja visualizar', font='Arial 20')
                        window.close()

                    try:
                        with sf.Connection(address, username=username, password=password) as sftp:
                            with sftp.cd(remotepath):
                                sftp.get(img)
                        im = Image.open(img)
                        im.show()
                        os.remove(img)

                    except Exception as error:
                        window.close()
                        sg.popup_ok(f'Erro: {error}', font='Arial 20')
                        error = str(error)
                        data = (datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                        with open('log/log.dat', 'a') as file:
                            file.write(data + '\n' + 'log de lista\n' + error + '\n\n-------------------------------------------------------------------------------\n\n')
                        return False

    def atualiza(self):
        sg.theme(theme)
        remotepath = '/home/guh/faceid/banco'
        localpath = '.banco/'
        sg.popup_auto_close('Aguarde finalizar...', font='Arial 20')
        while True:
            try:
                with sf.Connection(address, username=username, password=password) as sftp:
                    with sftp.cd('faceid/'):
                        sftp.get_d(remotepath, localpath)

                sg.popup_auto_close('Banco atualizado', font='Arial 20')
                return False

            except Exception as error:
                sg.popup_ok(f'Erro: {error}', font='Arial 20')
                error = str(error)
                with open('log/log.dat', 'a') as file:
                    file.write(data + '\n'+ 'log de atualiza\n' + error + '\n\n-------------------------------------------------------------------------------\n\n')
                return False

if __name__ == "__main__":
    MainApp().run()