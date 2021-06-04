from inspect import Traceback
import docx2txt #para arquivos docx
import PyPDF2 #para pdf
import os
import PySimpleGUI as sg
from funcoes import speak, get_audio, janela_inicial, janela_speech_recognition
from docx import Document


#janelas iniciais
janela1, janela2 = janela_inicial(), None

while True:
    window, event, values = sg.read_all_windows()

    if window == janela1 and event == 'Exit' or event == sg.WIN_CLOSED:
        break

    if window == janela1 and event == 'ler_arquivo':
        filepath = values['-FILE-']
        nome_arquivo = os.path.basename(filepath)
        window['arquivo_selecionado'].update(f'Arquivo lido: {nome_arquivo}', text_color = 'green')

        try:
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
                window['arquivo_selecionado'].update('Arquivo não suportado!',text_color = 'red')    
        except:
            window['arquivo_selecionado'].update('Arquivo vazio!',text_color = 'red')
            


        if filepath == '':
            window['arquivo_selecionado'].update('Por favor selecione um arquivo!',text_color = 'red')
    
    if window == janela1 and event == 'ditar_texto':
        janela2 = janela_speech_recognition()
        janela1.hide()

    if window == janela2 and event == 'back':
        janela2.hide()
        janela1.un_hide()
    try:
        if window == janela2 and event =='txt_button':
            window['texto_informativo'].update('Arquivo criado com sucesso!', text_color = 'green')
            with open('arquivo.txt', 'w', encoding='utf-8') as text_file:
                said = get_audio()
                text_file.write(said)
                
        if window == janela2 and event =='docx_button':
            window['texto_informativo'].update('Arquivo criado com sucesso!', text_color = 'green')
            #instancia docx
            documento = Document()
            said_docx = get_audio()
            documento.add_paragraph(said_docx)
            documento.save('demo.docx')
    except:
        window['texto_informativo'].update('Ocorreu algum erro, por favor tente novamente!', text_color = 'red')        

window.close()
