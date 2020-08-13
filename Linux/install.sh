#!/bin/bash

INSTALLATION_DIRECTORY="/opt/download_organizer"


[ ! -d "$INSTALLATTION" ] && mkdir -p $INSTALLATION_DIRECTORY

#Moving the Scripts to the INSTALLATION_DIRECTORY
cp download_organizer.py dest_folders.py $INSTALLATION_DIRECTORY
chown $USER /opt/download_organizer/download_organizer.py

#Moving the SHELL SCRIPT(COMMAND) to the /bin directory
chmod +x download_organizer
cp download_organizer /bin
chown $USER /bin/download_organizer
echo "Script sucefully installedTo run it type: \"download_organizer\""