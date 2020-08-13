#!/bin/bash

mkdir /opt/download_organizer/
cp download_organizer.py dest_folders.py /opt/download_organizer
chown $USER /opt/download_organizer/download_organizer.py

chmod +x download_organizer
cp download_organizer /bin
chown $USER /bin/download_organizer