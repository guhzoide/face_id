import os
import cv2
import base64
import imutils
import pysftp as sf
from menu import main
import psycopg2 as PgSQL
import PySimpleGUI as sg
import PIL.Image as Image

def cadastraRosto():
    sg.theme('DarkBlack')
    dados = [
        [sg.Text('Digite seu nome'), sg.Input(key='nome')],
        [sg.Button('Seguir')]
    ]

    window = sg.Window('Menu', dados, element_justification='c')
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

    image = open("banco/"+ nome +".jpg", "rb")
    img = image.read()
    img_byte = bytearray(img)
    img_code = base64.b64encode(img_byte)
    con = PgSQL.connect(host='localhost',
                        database='postgres',
                        user='postgres',
                        password='faceid1234')
    cursor = con.cursor()
    cursor.execute('INSERT INTO usuarios (nome, imagem_rosto) VALUES (%s,%s);', (nome, img_code))
    con.commit()   
     
    cv2.destroyAllWindows()
    main()
cadastraRosto()