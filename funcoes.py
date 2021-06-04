from gtts import gTTS, lang #Ler arquivos
from playsound import playsound #Musica
import speech_recognition as sr #speech recognition
import os #sistema
import PySimpleGUI as sg #biblioteca gráfica
import darkdetect #detectar modo escuro


def speak(text):
    tts = gTTS(text = text, lang = 'pt-br', slow= False)
    filename = 'audio.mp3'
    tts.save(filename)
    playsound(filename)
    os.remove(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        said = r.recognize_google(audio, language = 'pt-BR')

    return said

#janelas pysimplegui
def janela_inicial():
    if darkdetect.isDark() == True:
        sg.theme('DarkBlue17')
    else:
        sg.theme('Reddit')

    file_types = [("Todos arquivos", "*.*")]
    layout = [[sg.Text('Selecione um arquivo para começar!')],
            [sg.Text(size=(23,1), key='arquivo_selecionado')],
            [sg.Button('Ditar texto', key='ditar_texto'), sg.Input(size=(25, 1), key="-FILE-"),sg.FileBrowse(file_types=file_types, key= 'file_browse'), sg.Button('Ler arquivo', key='ler_arquivo')]]

    return sg.Window('Leitor de texto', layout=layout, finalize=True, element_justification='c')

def janela_speech_recognition():
    if darkdetect.isDark() == True:
        sg.theme('DarkBlue17')
    else:
        sg.theme('Reddit')
        
    layout =[[sg.Text('Clique no arquivo que deseja criar e comece a falar!',size=(37,1) , key= 'texto_informativo')],
            [sg.Button('Texto',size = (10, 1), key='txt_button'), sg.Button('Word',size = (10, 1), key='docx_button')],
            [sg.Button('Voltar', key='back')]]
    
    return sg.Window('Voz para texto', layout= layout, finalize= True, element_justification='c')
