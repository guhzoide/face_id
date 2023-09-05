import os
import cv2
import time
import serial
import imutils
from info import *
import psycopg2 as PgSQL
import PySimpleGUI as sg
import psycopg2 as PgSQL
from img_neg import put_neg
from img_aut import put_aut
from provaVida import provaVida
from datetime import datetime
from facepplib import FacePP, exceptions

faceCascade = cv2.CascadeClassifier("cascade/haarcascade_frontalface_default.xml")
data = str((datetime.now().strftime("%Y-%m-%d %H_%M_%S")))

def verifica(app):
    sg.theme(theme)
    chapa = sg.popup_get_text('Digite sua chapa', font='Arial 20')
    if chapa == '':
        sg.popup_ok('ATENÇÃO, digite sua chapa para continuar com a identificação', font='Arial 20')

    sg.popup_auto_close('ATENÇÃO, assim que seu rosto aparecer pisque seus olhos', font='Arial 20')
    provaVida()

    try:
        con = PgSQL.connect(host=host,database=database,user=user,password=password)
        cursor = con.cursor()
        cursor.execute(f"select nivel, nome, cpf from cadastros where chapa='{chapa}';")
        consulta = cursor.fetchone()
        nivel = consulta[0]
        nome = consulta[1]
        cpf = consulta[2]
        cursor.close()
            
        img1 = f".banco/{chapa}.jpg"

        with open('.banco/nivel.dat', 'r') as file:
            for line in file:
                pass
            last_nivel = line        

        if nivel <= last_nivel:
            sg.popup_ok('Você não possui acesso a este setor', font='Arial 20')
            result = False
            con = PgSQL.connect(host=host,database=database,user=user,password=password)
            cursor = con.cursor()
            cursor.execute('INSERT INTO acessos (colaborador_nome, chapa, cpf, data, acesso_autorizado) VALUES (%s,%s,%s,%s,%s);', (nome, chapa, cpf, data, result))
            con.commit()
            cursor.close()

        if cpf == '':
            sg.popup_ok('Você não possui cadastro em nosso sistema', font='Arial 20')
            result = False
            con = PgSQL.connect(host=host,database=database,user=user,password=password)
            cursor = con.cursor()
            cursor.execute('INSERT INTO acessos (colaborador_nome, chapa, cpf, data, acesso_autorizado) VALUES (%s,%s,%s,%s,%s);', (nome, chapa, cpf, data, result))
            con.commit()
            cursor.close()
            os._exit(0)

        webcam = cv2.VideoCapture(0)
        _, img = webcam.read()
        webcam.release()
        tentativa = data + '.jpg'
        with open('verifica/nomes.dat', 'w+') as file:
            file.write(tentativa)

        cv2.imwrite('verifica/'+ tentativa, img) 
        img2 = "verifica/"+ tentativa

        cmp_ = app.compare.get(image_file1=img1,image_file2=img2)
        confidence = cmp_.confidence

        while True:
            img_identifica = cv2.imread(img2)
            img_identifica = imutils.resize(img_identifica, width=950)

            faces = faceCascade.detectMultiScale(img_identifica, scaleFactor=1.1, minNeighbors=8, minSize=(25, 25))                                  

            for (x, y, w, h) in faces:
                cv2.rectangle(img_identifica, (x, y), (x + w, y + h), (255, 255, 0), 2)
                contador = str(faces.shape[0])
                if contador > '1':
                    sg.popup_auto_close('Mais de um rosto detectado', font='Arial 20')

            img_show = cv2.imread(img1)
            cv2.imshow("", img_show) 
            cv2.waitKey(100)

            if confidence > 80:
                result = True
                # porta = port
                # baud_rate = baudrate
                # ser = serial.Serial(porta, baud_rate)
                # time.sleep(2)
                # dados = "1"  
                # ser.write(dados.encode())
                # dados = "2"  
                # ser.write(dados.encode())
                # ser.close()
                
                sg.popup_auto_close('Olá, Acesso autorizado', font='Arial 20')
                cv2.destroyAllWindows()
                put_aut()
                break
            else:
                result = False
                sg.popup_auto_close('Acesso negado', font='Arial 20')
                cv2.destroyAllWindows()
                put_neg()
                break

        con = PgSQL.connect(host=host,database=database,user=user,password=password)
        cursor = con.cursor()
        cursor.execute('INSERT INTO acessos (colaborador_nome, chapa, cpf, data, acesso_autorizado) VALUES (%s,%s,%s,%s,%s);', (nome, chapa, cpf, data, result))
        con.commit()
        cursor.close()
        os.remove(img2)
        return False

    except FileNotFoundError as error:
        result = False
        error = str(error)
        con = PgSQL.connect(host=host,database=database,user=user,password=password)
        cursor = con.cursor()
        cursor.execute('INSERT INTO acessos (colaborador_nome, chapa, cpf, data, acesso_autorizado) VALUES (%s,%s,%s,%s,%s);', (nome, chapa, cpf, data, result))
        con.commit()
        cursor.close()
        put_neg()

        with open('log/log.dat', 'a') as file:
            file.write(data + '\n' + 'log de identificacao\n' + error + '\n\n-------------------------------------------------------------------------------\n\n')
        sg.popup_auto_close('Cadastro não encontrado', font='Arial 20')

    except Exception as error:
        sg.popup_auto_close(f'Erro: {error}', font='Arial 20')
        error = str(error)
        with open('log/log.dat', 'a') as file:
            file.write(data + '\n' + 'log de identificacao\n' + error + '\n\n------------------------------------------------------------------------------\n\n')

if __name__ == '__main__':

    api_key ='xQLsTmMyqp1L2MIt7M3l0h-cQiy0Dwhl'
    api_secret ='TyBSGw8NBEP9Tbhv_JbQM18mIlorY6-D'

    try:
        app_ = FacePP(api_key=api_key, api_secret=api_secret)
        funcs = [
            face_detection,
            verifica,
            faceset_initialize,
            face_search,
            face_landmarks,
            dense_facial_landmarks,
            face_attributes,
            beauty_score_and_emotion_recognition
        ]
        verifica(app_)

    except exceptions.BaseFacePPError as error:
        sg.popup_ok(f'Erro ao realizar identificação, Erro: {error}', font='Arial 20')
        error = str(error)
        with open('log/log.dat', 'a') as file:
            file.write(data + '\n' + 'log de FacePP\n' + error + '\n\n------------------------------------------------------------------------------\n\n')
        verifica(app_)

cv2.destroyAllWindows()