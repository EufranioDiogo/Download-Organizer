from locale import getdefaultlocale
from os import getenv, path

HOME = getenv('HOME')

language = getdefaultlocale()[0].lower()

def validate_folder(list_of_folders):
    for index in range(len(list_of_folders)):
        if not path.isdir(list_of_folders[index]):
            if list_of_folders[index][-1].lower() != 's':
                if path.isdir(list_of_folders[index] + 's'):
                    list_of_folders[index] = list_of_folders[index] + 's'
                    continue
            list_of_folders[index] = f'{list_of_folders[index].split("/")[-1]} folder doesn\'t exist'
    return list_of_folders


if 'en' in language:
    TRACK_FOLDER = f'{HOME}/Downloads'
    if not path.isdir(TRACK_FOLDER):
        TRACK_FOLDER = 'Error'
    folder_list = validate_folder([f'{HOME}/Music', f'{HOME}/Pictures', f'{HOME}/Videos', f'{HOME}/Documents'])

    MUSIC_FOLDER = folder_list[0]
    PICTURES_FOLDER = folder_list[1]
    VIDEOS_FOLDER = folder_list[2]
    DOCUMENTS_FOLDER = folder_list[3]
elif 'pt' in language:
    TRACK_FOLDER = f'{HOME}/Transferências'
    if not path.isdir(TRACK_FOLDER):
        TRACK_FOLDER = 'Error'
    folder_list = validate_folder([f'{HOME}/Música', f'{HOME}/Imagens', f'{HOME}/Vídeos', f'{HOME}/Documentos'])

    MUSIC_FOLDER = folder_list[0]
    PICTURES_FOLDER = folder_list[1]
    VIDEOS_FOLDER = folder_list[2]
    DOCUMENTS_FOLDER = folder_list[3]