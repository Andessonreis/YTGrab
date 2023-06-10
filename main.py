import PySimpleGUI as sg
from pytube import YouTube

sg.theme('BluePurple')  # Define o tema da janela

def download_video(url):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download()
        sg.popup('Download concluído!')  # Exibe uma mensagem de conclusão do download
    except Exception as e:
        sg.popup_error('Erro durante o download ', str(e))  # Exibe uma mensagem de erro em caso de falha no download

# Define o layout 
layout = [
    [sg.Text('Insira a URL do vídeo do YouTube:', font=('Arial', 12))],
    [sg.Input(key='-URL-', size=(50, 1))],
    [sg.Button('Download', size=(10, 1), font=('Arial', 12))]
]
window = sg.Window('Downloader YouTube Video', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Download':
        video_url = values['-URL-']
        if video_url:
            download_video(video_url)

window.close()

