import PySimpleGUI as sg
import cv2

def verificav():
    # Inicializa identificador 
    faceCascade = cv2.CascadeClassifier("cascade/haarcascade_frontalface_default.xml")
    #eyeCascade = cv2.CascadeClassifier("cascade/haarcascade_eye.xml")

    #Inicializa a camera
    webcam = cv2.VideoCapture(0)

    while True:
        # Captura o frame
        _, img = webcam.read()

        # Pega a versão cinza da imagem
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Pega as coordenadas da localização do rosto na imagem
        faces = faceCascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=3, minSize=(50, 50))                                  

        # Desenha um retangulo nas coordenadas oferecidas
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2) 

        # Mostra a imagem
        cv2.imshow("Verificando face, aguarde", img) 
            
        file = open("banco")
        file = file.read()

        if len(faces)==0:
            print("Não encontrou face")

        else:
            dados = str(faces)
            if dados in file:
                valida = "Acesso autorizado"
                sg.theme('Black')
                sg.popup_auto_close(valida)

        # Espera o usuario pressionar q
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Fecha a camera
    webcam.release()
    
    # fecha todas as janelas
    cv2.destroyAllWindows()
verificav()