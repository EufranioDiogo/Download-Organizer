from shutil import move
from os import listdir, chdir, remove, path, rename
from time import sleep
from dest_folders import MUSIC_FOLDER, PICTURES_FOLDER, VIDEOS_FOLDER, DOCUMENTS_FOLDER, USER, TRACK_FOLDER
from file_extensions import music_exten, pictures_exten, documents_exten, videos_exten


def find_dest_folder(file):
    if '.' in file:
        file_extension = file.split('.')
        file_extension = file_extension[-1].lower()

        if file_extension in music_exten:
            return MUSIC_FOLDER
        if file_extension in pictures_exten:
            return PICTURES_FOLDER
        if file_extension in documents_exten:
            return DOCUMENTS_FOLDER
        if file_extension in videos_exten:
            return VIDEOS_FOLDER
    return 'Unknow'

def delete_every_not_needed_file():
    for dir in [DOCUMENTS_FOLDER, MUSIC_FOLDER, VIDEOS_FOLDER, PICTURES_FOLDER]:
        chdir(dir)
        files = (file for file in listdir() if path.isfile(file) == True)

        for file in files:
            if path.getsize(path.join(dir, file)) == 0:
                remove(file)

def generate_alternative_name(file, DEST_FOLDER):
    actual_file_name = file

    chdir(DEST_FOLDER)

    while actual_file_name in (element for element in listdir() if path.isfile(element)):
        actual_file_name = 'Copy ' + actual_file_name
    return f'{actual_file_name}'

def over_view_and_organize():
    chdir(TRACK_FOLDER)

    files = (element for element in listdir() if path.isfile(element))

    for file in files:
        DEST_FOLDER = find_dest_folder(file)

        if DEST_FOLDER != 'Unknow':
            try:
                move(file, DEST_FOLDER)
            except:
                new_file_name = generate_alternative_name(file, DEST_FOLDER)
                chdir(TRACK_FOLDER)
                rename(file, new_file_name)
                return over_view_and_organize()
    delete_every_not_needed_file()

while True:
    over_view_and_organize()
    sleep(20)

