import os
import cv2
import base64
import imutils
import pysftp as sf
from menu import main
import PySimpleGUI as sg
from datetime import datetime

#servidor
address = '192.168.5.108'
username = 'face'
password = 'faceid'

data = (datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
faceCascade = cv2.CascadeClassifier("cascade/haarcascade_frontalface_default.xml")

def cadastraRosto():
    sg.theme('DarkBlack')
    dados = [
        [sg.Text('Digite seu nome'), sg.Input(key='nome')],
        [sg.Button('Seguir')]
    ]

    window = sg.Window('Cadastro', dados, element_justification='c')
    e, v = window.read()
    nome = v['nome']
    if e == sg.WINDOW_CLOSED:
        window.close()
        main()
        os._exit(0)

    elif e == 'Seguir':
        window.close()

    faceCascade = cv2.CascadeClassifier("cascade/haarcascade_frontalface_default.xml")

    webcam = cv2.VideoCapture(0)

    while True:
        _, img = webcam.read()

        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        faces = faceCascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=8, minSize=(25, 25))                                  

        for (x, y, w, h) in faces:
            cv2.rectangle(gray_img, (x, y), (x + w, y + h), (255, 255, 0), 2)
            contador = str(faces.shape[0])
            if contador > '1':
                sg.popup_auto_close('Mais de um rosto detectado')

        img = imutils.resize(gray_img, width=850)
        cv2.imshow("Verificando face, aguardando retorno...", gray_img) 

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    webcam.release()
    
    imgName = "banco/" + nome + ".jpg"
    cv2.imwrite(imgName, gray_img)
    sg.popup_auto_close('Cadastro realizado com sucesso')
    try:
        with sf.Connection(address, username=username, password=password) as sftp:
            with sftp.cd('/home/face/face_id/cadastro'):             
                sftp.put(imgName)  
    except Exception as error:
        error = str(error)
        with open('log/log.dat', 'a') as file:
            file.write(data + '\n' + error + '\n\n------------------------------------------------------------------------\n\n')
        sg.popup('Falha ao conectar com o servidor')
     
    cv2.destroyAllWindows()
    main()
cadastraRosto()