from os import getlogin, path
from locale import getdefaultlocale
USER = getlogin()

language = getdefaultlocale()[0].lower()

if 'en' in language:
    TRACK_FOLDER = path.normcase(f'C:/Users/{USER}/Downloads')
    MUSIC_FOLDER = path.normcase(f'C:/Users/{USER}/Music')
    PICTURES_FOLDER = path.normcase(f'C:/Users/{USER}/Pictures')
    VIDEOS_FOLDER = path.normcase(f'C:/Users/{USER}/Videos')
    DOCUMENTS_FOLDER = path.normcase(f'C:/Users/{USER}/Documents')
    APPS_FOLDER = path.normcase(f'C:/Users/{USER}/Apps')
elif 'pt' in language:
    TRACK_FOLDER = path.normcase(f'C:/Users/{USER}/Transferências')
    MUSIC_FOLDER = path.normcase(f'C:/Users/{USER}/Musicas')
    PICTURES_FOLDER = path.normcase(f'C:/Users/{USER}/Imagens')
    VIDEOS_FOLDER = path.normcase(f'C:/Users/{USER}/Vídeos')
    DOCUMENTS_FOLDER = path.normcase(f'C:/Users/{USER}/Documentos')
    APPS_FOLDER = path.normcase(f'C:/Users/{USER}/Aplicações')