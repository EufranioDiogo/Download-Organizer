#!/bin/bash

USER=${SUDO_USER:-${USER}}
INSTALLATION_DIRECTORY="/opt/download_organizer"

echo "Removing the installation directory: $INSTALLATION_DIRECTORY"
if [ -d $INSTALLATION_DIRECTORY ]
then
    rm -r $INSTALLATION_DIRECTORY
    echo "Removed!"
else
    echo "The folder does not exist!"
fi


echo "Deleting the command: download_organizer"
if [ -f "/bin/download_organizer" ]
then
    rm  "/bin/download_organizer"
    echo "Command Deleted!"
else
    echo "The command already don't exists"
fi

echo "Deleting the service /etc/systemd/system/download_organizer_startup.service!"

if [ -f "/etc/systemd/system/download_organizer_startup.service" ]
then
    rm "/etc/systemd/system/download_organizer_startup.service"
    echo "Service Deleted!"
else
    echo "The service doesn't exists"
fi

systemctl stop download_organizer_startup.service

echo "download_organizer was succefully deleted! :)"