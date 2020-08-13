from os import getlogin
from locale import getdefaultlocale
USER = getlogin()

language = getdefaultlocale()[0].lower()

if 'en' in language:
    TRACK_FOLDER = f'/home/{USER}/Downloads'
    MUSIC_FOLDER = f'/home/{USER}/Music'
    PICTURES_FOLDER = f'/home/{USER}/Pictures'
    VIDEOS_FOLDER = f'/home/{USER}/Videos'
    DOCUMENTS_FOLDER = f'/home/{USER}/Documents'
    APPS_FOLDER = f'/home/{USER}/Apps'
elif 'pt' in language:
    TRACK_FOLDER = f'/home/{USER}/Transferências'
    MUSIC_FOLDER = f'/home/{USER}/Musicas'
    PICTURES_FOLDER = f'/home/{USER}/Imagens'
    VIDEOS_FOLDER = f'/home/{USER}/Vídeos'
    DOCUMENTS_FOLDER = f'/home/{USER}/Documentos'
    APPS_FOLDER = f'/home/{USER}/Aplicações'