import os
import pysftp as sf
import PySimpleGUI as sg
from menu import main

#servidor
address = '192.168.5.102'
username = 'face'
password = 'faceid'

sg.theme('DarkBlack')
try:    
    with sf.Connection(address, username=username, password=password) as sftp:   
        with sftp.cd('/home/face/face_id/tentativa/'):        
            ls = sftp.listdir()
            ls = '\n \n'.join(ls)
            tentativas = [
                [sg.Multiline(ls, size=(95,35))],
                [sg.Text('Digite o nome da imagem'), sg.Input(key=('img'))],
                [sg.Button('Baixar')]
            ]

            window = sg.Window('Tentativas', tentativas, element_justification='c')
            e, v = window.read()
            img = v['img']
            if e == 'Baixar':
                window.close()
                sftp.get(img)
                sg.popup_auto_close('Download realizado com sucesso')
    main()
    os._exit(0)
except:
    sg.popup_ok('Falha na conexão com o servidor')
    main()
    os._exit(0)