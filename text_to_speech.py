import PySimpleGUI as sg #biblioteca gráfica
import os #sistema
from gtts import gTTS, lang #Ler arquivos
from playsound import playsound #Musica
import docx2txt #para arquivos docx
import PyPDF2 #para pdf



#engine audio

def speak(text):
    tts = gTTS(text = text, lang = 'pt-br', slow= False)
    filename = 'audio.mp3'
    tts.save(filename)
    playsound(filename)
    os.remove(filename)

#tipos de dados
file_types = [("Todos arquivos", "*.*")]

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

    if event == 'ler_arquivo':
        filepath = values['-FILE-']
        nome_arquivo = os.path.basename(filepath)
        window['arquivo_selecionado'].update(f'Arquivo lido: {nome_arquivo}', text_color = 'black')

        if filepath == '':
            window['arquivo_selecionado'].update('Por favor selecione um arquivo!',text_color = 'red')

        if nome_arquivo.split(".")[-1] == 'txt':
            with open(filepath) as text_to_read:
                txt = text_to_read.read()
                speak(txt)
        elif nome_arquivo.split(".")[-1] == 'docx':
            docx_text = docx2txt.process(filepath)
            speak(docx_text)
        elif nome_arquivo.split(".")[-1] == 'pdf':
            # creating a pdf file object 
            pdfFileObj = open(filepath, 'rb') 
            # creating a pdf reader object 
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
                
            # creating a page object 
            pageObj = pdfReader.getPage(0) 
                
            # extracting text from page 
            pdf_text = pageObj.extractText() 
                
            # closing the pdf file object 
            speak(pdf_text)
            pdfFileObj.close() 

    else:
        window['arquivo_selecionado'].update('Por favor selecione um arquivo de texto!',text_color = 'red')

window.close()