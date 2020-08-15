from locale import getdefaultlocale
from os import getenv

HOME = getenv('HOME')

language = getdefaultlocale()[0].lower()

if 'en' in language:
    TRACK_FOLDER = f'{HOME}/Downloads'
    MUSIC_FOLDER = f'{HOME}/Music'
    PICTURES_FOLDER = f'{HOME}/Pictures'
    VIDEOS_FOLDER = f'{HOME}/Videos'
    DOCUMENTS_FOLDER = f'{HOME}/Documents'
    APPS_FOLDER = f'{HOME}/Apps'
elif 'pt' in language:
    TRACK_FOLDER = f'{HOME}/Transferências'
    MUSIC_FOLDER = f'{HOME}/Musicas'
    PICTURES_FOLDER = f'{HOME}/Imagens'
    VIDEOS_FOLDER = f'{HOME}/Vídeos'
    DOCUMENTS_FOLDER = f'{HOME}/Documentos'
    APPS_FOLDER = f'{HOME}/Aplicações'