import pyttsx3
import PySimpleGUI as sg
def falar(texto):
    engine = pyttsx3.init('sapi5')
    engine.setProperty('rate', 180)
    engine.save_to_file(texto, 'output.mp3')
    engine.runAndWait()
sg.theme('LightBlue')
layout = [
    [sg.Text('Convert texto to sound file:')],
    [sg.Multiline(size=(40, 10), key='texto')],
    [sg.Button('Convert')],
    [sg.Text('                                      Created by FlukerBr', text_color='blue')]
]
window = sg.Window('Convert text to sound file', layout, element_justification='center')
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Convert':
        falar(values['texto'])
