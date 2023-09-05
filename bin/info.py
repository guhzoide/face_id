import mysql.connector
import PySimpleGUI as sg

try:
    #--------------------------------------#
    #tema
    theme = 'SystemDefault'
    #--------------------------------------#
    #banco
    database = 'faceid'
    user = '37iwgyvd3z2t5axm9ilh'
    host = 'aws.connect.psdb.cloud'
    password = 'pscale_pw_KsIB7Pj35TEBrOMUetPFVpzYMLddcQABU8AoauUU8wC'
    #--------------------------------------#    
    #Arduino
    conn = mysql.connector.connect(host=host, user=user, password=password, database = database)
    mycursor = conn.cursor()
    mycursor.execute(f"select port, baudrate from cadastroip where estacao='fechadura';")
    consulta = mycursor.fetchone()
    port = consulta[0]
    baudrate = consulta[1]
    conn.close()
    #--------------------------------------#
    #parametros para a verificação do rosto
    face_detection=""
    faceset_initialize=""
    face_search=""
    face_landmarks=""
    dense_facial_landmarks=""
    face_attributes=""
    beauty_score_and_emotion_recognition=""

except Exception as error:
    error = str(error)
    sg.popup(F'Erro ao conectar no banco de dados:\n{error}', font='Arial 15')