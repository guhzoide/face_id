import cv2
from info import *
import PySimpleGUI as sg
from datetime import datetime

data = (datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def provaVida():
	sg.theme(theme)
	try:
		cap = cv2.VideoCapture(0)

		face_cascade = cv2.CascadeClassifier('cascade/haarcascade_frontalface_default.xml')
		eye_cascade = cv2.CascadeClassifier('cascade/haarcascade_eye.xml')

		while(True):
			_, frame = cap.read()

			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			faces = face_cascade.detectMultiScale(gray, 1.3, 8)
			count = 0
			for (x,y,w,h) in faces:
				cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
				roi_gray = gray[y:y+h, x:x+w]
				roi_color = frame[y:y+h, x:x+w]
				eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 8)
				for (ex,ey,ew,eh) in eyes:
					count = 0
					eyeLocal = cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
					cv2.putText(frame, f"Pisque seus olhos: {count}", (10,50), cv2.FONT_HERSHEY_PLAIN, 3,(238,130,238),2)
					eyesCounter = str(eyes.shape[0])
					if eyesCounter == '1':
						cap.release()
						cv2.destroyAllWindows()
						return False

			cv2.imshow('frame',frame)

			if cv2.waitKey(1) & 0xFF == ord('q'):
				return False
		
	except Exception as error:
		error = str(error)
		with open('log/log.dat', 'a') as file:
			file.write(data + '\n' + 'log de provaVida\n' + error + '\n\n-------------------------------------------------------------------------------\n\n')
		sg.popup_auto_close('Algo deu errado, verifique o log', font='Arial 20')