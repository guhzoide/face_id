import os
import PySimpleGUI as sg

def main():
    sg.theme('DarkBlack')
    menu = [
        [sg.Text('Bem-vindo(a)')],
        [[sg.Image("logo.jpg")]],
        [sg.Text('O que deseja fazer')],
        [sg.Button('Indentificar', size=(15,0)), sg.Button('Cadastrar', size=(15,0)), sg.Button('Atualizar banco', size=(15,0))]
    ]

    window = sg.Window('Menu', menu, element_justification='c', size=(650,350))
    e, v = window.read()

    if e == sg.WINDOW_CLOSED:
        window.close()

    elif e == 'Indentificar':
        window.close()
        ident = 'python3 scan/identificador.py'
        os.system(ident)

    elif e == 'Cadastrar':
        window.close()
        cad = 'python3 scan/cadastrar.py'
        os.system(cad)

    elif e == 'Atualizar banco':
        window.close()
        atu = 'python3 scan/atualiza_banco.py'
        os.system(atu)