from os import getlogin, path
from locale import getdefaultlocale
USER = getlogin()

language = getdefaultlocale()[0].lower()

if 'en' in language:
    TRACK_FOLDER = 'C:\\Users\\{}\\Downloads'.format(USER)
    MUSIC_FOLDER = 'C:\\Users\\{}\\Music'.format(USER)
    PICTURES_FOLDER = 'C:\\Users\\{}\\Pictures'.format(USER)
    VIDEOS_FOLDER = 'C:\\Users\\{}\\Videos'.format(USER)
    DOCUMENTS_FOLDER = 'C:\\Users\\{}\\Documents'.format(USER)
elif 'pt' in language:
    TRACK_FOLDER = 'C:\\Users\\{}\\Downloads'.format(USER)
    MUSIC_FOLDER = 'C:\\Users\\{}\\Music'.format(USER)
    PICTURES_FOLDER = 'C:\\Users\\{}\\Pictures'.format(USER)
    VIDEOS_FOLDER = 'C:\\Users\\{}\\Videos'.format(USER)
    DOCUMENTS_FOLDER = 'C:\\Users\\{}\\Documents'.format(USER)