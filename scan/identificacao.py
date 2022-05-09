import os
import cv2
import imutils
import pysftp as sf
from menu import main
import PySimpleGUI as sg
from datetime import datetime
from facepplib import FacePP, exceptions

#parametros para a verificação do rosto
face_detection=""
faceset_initialize=""
face_search=""
face_landmarks=""
dense_facial_landmarks=""
face_attributes=""
beauty_score_and_emotion_recognition=""
faceCascade = cv2.CascadeClassifier("cascade/haarcascade_frontalface_default.xml")

#servidor
address = '192.168.5.102'
username = 'face'
password = 'faceid'

def verifica(app):
    sg.theme('DarkBlack')
    dados = [
        [sg.Text('Digite seu nome'), sg.Input(key='nome')],
        [sg.Button('Ok')]
    ]

    window = sg.Window('Menu', dados, element_justification='c')
    e, v = window.read()
    nome = v['nome']

    if e == sg.WINDOW_CLOSED:
        window.close()
        main()
        os._exit(0)

    elif nome == '':
        sg.popup_ok('O campo nome precisa ser preenchido!')
        window.close()
        verifica(app_)
        os._exit(0)

    elif e == 'Ok':
        window.close()

 #----------------------------------------------------------------------------------------------------------------#
    try:
        img1 = "banco/" + nome + ".jpg"
        test = open(img1)
        test.close()
        webcam = cv2.VideoCapture(0)
        _, img = webcam.read()
        verifica = str(datetime.now())
        cv2.imwrite('verifica/'+ verifica +'.jpg', img) 

        img2 = "verifica/"+ verifica +".jpg"
        cmp_ = app.compare.get(image_file1=img1,image_file2=img2)
        confidence = cmp_.confidence

        with sf.Connection(address, username=username, password=password) as sftp:
            with sftp.cd('/home/face/face_id/tentativa'):             
                sftp.put(img2)

    except cv2.error:
        sg.popup_ok('Verifique a conexão com a câmera')
        main()
        os._exit(0)    

    except Exception:
        sg.popup_ok('Falha na conexão com o servidor')
    
    faceCascade = cv2.CascadeClassifier("cascade/haarcascade_frontalface_default.xml")
    while True:
        img = cv2.imread(img2)
        img = imutils.resize(img, width=950)
            
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=8, minSize=(25, 25))                                  

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
            contador = str(faces.shape[0])
            if contador > '1':
                sg.popup_auto_close('Mais de um rosto detectado')
        
        cv2.imshow("Face verificada", img)

        if confidence > 80:
            sg.popup_ok('Acesso autorizado')
            cv2.destroyAllWindows()
            break
        else:
            sg.popup_ok('Acesso negado')
            cv2.destroyAllWindows()
            break
    main()

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

    except exceptions.BaseFacePPError as e:
        sg.popup_ok('Erro')
        verifica(app_)
        os._exit(0)

    cv2.destroyAllWindows()
    os._exit(0)