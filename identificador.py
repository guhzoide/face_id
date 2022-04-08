import cv2
import emoji
import numpy as np
from facepplib import FacePP, exceptions
from __future__ import print_function, unicode_literals

face_detection=""
faceset_initialize=""
face_search=""
face_landmarks=""
dense_facial_landmarks=""
face_attributes=""
beauty_score_and_emotion_recognition=""
def verifica():
    # Inicializa identificador 
    faceCascade = cv2.CascadeClassifier("cascade/haarcascade_frontalface_default.xml")
    # ler imagem
    #file=r"images/"
    img = cv2.imread("images/test1.jpg")


    while True:
        # Pega a versão cinza da imagem
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Pega as coordenadas da localização do rosto na imagem
        faces = faceCascade.detectMultiScale(gray_img, scaleFactor=1.5, minNeighbors=5, minSize=(50, 50))                      

        # Desenha um retangulo nas coordenadas oferecidas
        for (x, y, w, h) in faces:
            cv2.rectangle(gray_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                
        # Mostra a imagem
        cv2.imshow("Identified Face", img)
        
        # Espera o usuario pressionar q
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    hh, ww = img.shape[:2]
    lower = np.array([200, 200, 200]) 
    upper = np.array([255, 255, 255])
    lixo = cv2.inRange(img, lower, upper)
    
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (20,20))
    morph = cv2.morphologyEx(lixo, cv2.MORPH_CLOSE, kernel)
    mask = 255 - morph
    result = cv2.bitwise_and(img, img, mask=mask)

    imgName = "removeBackground.jpg"
    cv2.imwrite(imgName, result)

    imgB = cv2.imread("removeBackground.jpg")
    imgGray = cv2.cvtColor(imgB, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(imgName, imgGray)


    cmp = app.compare.get(img, imgB)

    # fecha todas as janelas
    cv2.destroyAllWindows() 
verifica()