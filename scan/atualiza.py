import os
import pysftp as sf
from menu import main
import PySimpleGUI as sg
from datetime import datetime

#servidor
address = 'ip'
username = 'use'
password = 'pass'
data = (datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def atualiza():   
    sg.theme('DarkBlack')
    remotepath = '/home/guh/faceid/banco/'
    localpath = 'banco/'
    try:
        with sf.Connection(address, username=username, password=password) as sftp:
            with sftp.cd('/home/guh/faceid/'):
                sftp.get_d(remotepath, localpath)
                
        sg.popup_auto_close('banco local atualizado')
        main()
        os._exit(0)
        
    except Exception as error:
        sg.popup_ok('Algo deu errado, verifique o log')
        error = str(error)
        with open('log/log.dat', 'a') as file:
            file.write(data + '\n' + error + '\n\n------------------------------------------------------------------------\n\n')
        main()
        os._exit(0)
atualiza()