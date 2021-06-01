from typing import Sized
import PySimpleGUI as sg
import os
from gtts import gTTS
from playsound import playsound

#engine audio
language = 'pt-br'


#tipos de dados
file_types = [("Texto (*.txt)", "*.txt")]

#layout and pysimplegui stuff
sg.theme('Reddit')

layout = [  [sg.Text('Selecione um arquivo para começar!')],
            [sg.Text(size=(40,1), key='arquivo_selecionado')],
            [sg.Input(size=(25, 1), key="-FILE-"),sg.FileBrowse(file_types=file_types, key= 'file_browse'), sg.Button('Ler arquivo', key='ler_arquivo')]]

window = sg.Window('Leitor de texto', layout)

while True:
    event, values = window.read()

    if event == 'Exit' or event == sg.WIN_CLOSED:
        break
    
    try:
        if event == 'ler_arquivo':
            filepath = values['-FILE-']
            nome_arquivo = os.path.basename(filepath)
            window['arquivo_selecionado'].update(f'Lendo arquivo: {nome_arquivo}')
            with open(filepath) as text:
                mytext = text.read()
                myobj = gTTS(text=mytext, lang=language, slow=False)
                filename= 'versao2.mp3'
                myobj.save(filename)
                playsound(filename)
                os.remove(filename)
    except:
        window['arquivo_selecionado'].update('Por favor selecione um arquivo!',text_color = 'red')
    


window.close()