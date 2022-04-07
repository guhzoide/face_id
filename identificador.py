import cv2

def verifica():
    # Inicializa identificador 
    faceCascade = cv2.CascadeClassifier("cascade/haarcascade_frontalface_default.xml")
    # ler imagem
    #file=r"images/"
    img = cv2.imread("images/test2.jpg")


    while True:
        # Pega a versão cinza da imagem
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Pega as coordenadas da localização do rosto na imagem
        faces = faceCascade.detectMultiScale(gray_img, scaleFactor=1.5, minNeighbors=5, minSize=(50, 50))
                                  

        # Desenha um retangulo nas coordenadas oferecidas
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                
        # Mostra a imagem
        cv2.imshow("Identified Face", img)
        
        # Espera o usuario pressionar q
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # fecha todas as janelas
    cv2.destroyAllWindows() 

    face = str(faces)
    #eye = str(eyes)

    print(face)

    #rosto = faces + eyes
    #print(rosto)

verifica()