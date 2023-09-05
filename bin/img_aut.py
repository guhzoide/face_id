from bd import *
from info import *
import pysftp as sf
import PySimpleGUI as sg
from datetime import datetime
data = (datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def put_aut():
    try:
        with open('verifica/nomes.dat', 'r') as file:
            for line in file:
                pass
            last = line
        img = 'verifica/' + last

        with sf.Connection(address, username=username, password=password) as sftp:
            with sftp.cd('faceid/tentativas/autorizadas'):             
                sftp.put(img)

    except Exception as error:
        sg.popup_ok('Algo deu errado, verifique o log', font='Arial 20')
        data = (datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        error = str(error)
        with open('log/log.dat', 'a') as file:
            file.write(data + '\n' + 'log de img_aut\n' + error + '\n\n-------------------------------------------------------------------------------\n\n')
