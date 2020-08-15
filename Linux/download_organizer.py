from shutil import move
from time import sleep
from src.watchdog.observers import Observer
from src.watchdog.events import FileSystemEventHandler
from file_extensions import music_exten, pictures_exten, documents_exten, videos_exten, apps_exten
from dest_folders import MUSIC_FOLDER, PICTURES_FOLDER, VIDEOS_FOLDER, DOCUMENTS_FOLDER, APPS_FOLDER, TRACK_FOLDER
from os import listdir, chdir, remove, path, rename


class Handler(FileSystemEventHandler):
    def __init__(self):
        pass

    def on_created(self, event):
        self.over_view_and_organize()

    def find_dest_folder(self, file):
        if '.' in file:
            file_extension = file.split('.')
            file_extension = file_extension[-1]

            if file_extension in music_exten:
                return MUSIC_FOLDER
            if file_extension in pictures_exten:
                return PICTURES_FOLDER
            if file_extension in documents_exten:
                return DOCUMENTS_FOLDER
            if file_extension in videos_exten:
                return VIDEOS_FOLDER
            if file_extension in apps_exten:
                return  APPS_FOLDER
        return 'Unknow'

    def generate_alternative_name(self, file, DEST_FOLDER):
        actual_file_name = file

        while path.isfile(f'{DEST_FOLDER}/{actual_file_name}'):
            actual_file_name = 'Copy_' + actual_file_name
        return f'{DEST_FOLDER}/{actual_file_name}'

    def over_view_and_organize(self):
        chdir(TRACK_FOLDER)

        files = (element for element in listdir() if path.isfile(element))

        for file in files:
            DEST_FOLDER = self.find_dest_folder(file)

            if DEST_FOLDER != 'Unknow':
                try:
                    move(file, DEST_FOLDER)
                except:
                    pass

event_observer = Observer()
tracked_event = Handler()

event_observer.schedule(tracked_event, TRACK_FOLDER, recursive=False)

event_observer.start()

tracked_event.over_view_and_organize()

try:
    while True:
        sleep(10)
except KeyboardInterrupt:
    event_observer.stop()

event_observer.join()