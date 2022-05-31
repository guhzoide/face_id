import os
import PySimpleGUI as sg

def main():
    sg.theme('DarkBlack')
    menu = [
        [sg.Text('Bem-vindo(a)')],
        [[sg.Image("logo.jpg")]],
        [sg.Text('O que deseja fazer')],
        [sg.Button('Indentificação', size=(15,0)), sg.Button('Cadastro', size=(15,0))]
    ]

    window = sg.Window('Menu', menu, element_justification='c', size=(650,350))
    e, v = window.read()

    if e == sg.WINDOW_CLOSED:
        window.close()

    elif e == 'Indentificação':
        window.close()
        ident = 'python3 scan/identificacao.py'
        os.system(ident)
        os._exit(0)

    elif e == 'Cadastro':
        window.close()
        cad = 'python3 scan/cadastro.py'
        os.system(cad)
        os._exit(0)
