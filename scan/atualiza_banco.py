import os
import pysftp as sf
import PySimpleGUI as sg
from menu import main

#servidor
address = 'ip'
username = 'face'
password = 'faceid'

sg.theme('DarkBlack')
try:    
    sg.popup_auto_close('Aguarde')
    os.mkdir('banco')
    local_path= 'banco/'
    with sf.Connection(address, username=username, password=password) as sftp:           
        sftp.get_d("/home/face/face_id/banco/", 'banco')
        sftp.close()
    sg.popup_auto_close('finalizado com sucesso')
    main()
except:
    sg.popup_ok('Algo deu errado, verifique se a pasta banco foi realmente excluída e tente novamente')
    main()
