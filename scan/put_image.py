import pysftp as sf

#servidor
address = 'ip'
username = 'use'
password = 'pass'

def put():
    with open('verifica/nomes.dat', 'r') as file:
        for line in file:
            pass
        last = line   
    
    img = 'verifica/'+ last

    with sf.Connection(address, username=username, password=password) as sftp:
        with sftp.cd('/home/guh/faceid/tentativas'):             
            sftp.put(img)