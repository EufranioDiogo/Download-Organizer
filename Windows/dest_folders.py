from os import getlogin
from locale import getdefaultlocale
USER = getlogin()

language = getdefaultlocale()[0].lower()

if 'en' in language:
    TRACK_FOLDER = f'/home/{USER}/Downloads'
    MUSIC_FOLDER = f'C:\\Users\\{USER}\\Music'
    PICTURES_FOLDER = f'C:\\Users\\{USER}\\Pictures'
    VIDEOS_FOLDER = f'C:\\Users\\{USER}\\Videos'
    DOCUMENTS_FOLDER = f'C:\\Users\\{USER}\\Documents'
    APPS_FOLDER = f'C:\\Users\\{USER}\\Apps'
elif 'pt' in language:
    TRACK_FOLDER = f'/home/{USER}/Transferências'
    MUSIC_FOLDER = f'C:\\Users\\{USER}\\Musicas'
    PICTURES_FOLDER = f'C:\\Users\\{USER}\\Imagens'
    VIDEOS_FOLDER = f'C:\\Users\\{USER}\\Vídeos'
    DOCUMENTS_FOLDER = f'C:\\Users\\{USER}\\Documentos'
    APPS_FOLDER = f'C:\\Users\\{USER}\\Aplicações'