from os import getlogin
from shutil import move

USER = getlogin()

# DESTINATION FOLDERS
MUSIC_FOLDER = f'/home/{USER}/Music'
PICTURES_FOLDER = f'/home/{USER}/Pictures'
VIDEOS_FOLDER = f'/home/{USER}/Videos'
DOCUMENTS_FOLDER = f'/home/{USER}/Documents'
APPS_FOLDER = f'/home/{USER}/Apps'

# Files Extensions
music_extensions = {'mp3', '3gpp'}
pictures_extensions = {'jpg', 'png', 'jpeg'}
documents_extensions = { 'pdf', 'docx', 'doc', 'txt'}
videos_extensions = {'mp4', 'webm', 'mkv'}
apps_extensions = {'deb', 'exec'}


def find_dest_folder(file):
    if '.' in file:
        file_extension = file.split('.')
        file_extension = file_extension[-1]

        if file_extension in music_extensions:
            return MUSIC_FOLDER
        if file_extension in pictures_extensions:
            return PICTURES_FOLDER
        if file_extension in documents_extensions:
            return DOCUMENTS_FOLDER
        if file_extension in videos_extensions:
            return VIDEOS_FOLDER
        if file_extension in apps_extensions:
            return  APPS_FOLDER
    return 'Unknow'


def over_view_and_organize():
    from os import listdir, chdir, remove, path

    chdir(TRACK_FOLDER)

    files = (element for element in listdir() if path.isfile(element))

    for file in files:
        DEST_FOLDER = find_dest_folder(file)

        if DEST_FOLDER != 'Unknow':
            try:
                print(f'Moving {file} to {DEST_FOLDER}')
                move(file, DEST_FOLDER)
            except:
                remove(DEST_FOLDER + '/' + file)
                return over_view_and_organize()


TRACK_FOLDER = f'/home/{USER}/Downloads'
over_view_and_organize()
