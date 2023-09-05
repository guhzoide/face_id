import PySimpleGUI as sg
import mysql.connector

try:
    database = 'database'
    user = 'user'
    host = 'host'
    password = 'pass'

    conn = mysql.connector.connect(database=database, username=user, host=host, password=password)
    cursor = conn.cursor()
    cursor.execute("select usuario, pass, ip from cadastroip;")
    consulta = cursor.fetchone()
    username = consulta[0]
    password = consulta[1]
    address = consulta[2]
    conn.close()

except Exception as error:
    error = str(error)
    sg.popup(F'Erro ao pegar dados do servidor(bd.py):\n {error}', font='Arial 15')