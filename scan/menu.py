import PySimpleGUI as sg
import os

def main():
    sg.theme('DarkBlack')
    menu = [
        [sg.Text('Bem-vindo(a)')],
        [[sg.Image("banco/logo.jpg")]],
        [sg.Text('O que deseja fazer')],
        [sg.Button('Indentificar', size=(15,0)), sg.Button('Cadastrar', size=(15,0))]
    ]

    window = sg.Window('Menu', menu, element_justification='c', size=(650,350))
    e, v = window.read()

    if e == sg.WINDOW_CLOSED:
        window.close()

    elif e == 'Indentificar':
        window.close()
        ident = 'python scan/identificador.py'
        os.system(ident)

    elif e == 'Cadastrar':
        window.close()
        cad = 'python scan/cadastrar.py'
        os.system(cad)