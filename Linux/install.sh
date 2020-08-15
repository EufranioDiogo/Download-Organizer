#!/bin/bash

USER=${SUDO_USER:-${USER}}
INSTALLATION_DIRECTORY="/opt/download_organizer"

echo "Hi :) You're installing the download_organizer"
echo ""
read -p "Do you agree with the changes that we'll going to do to make it run [Y/n]: " user_answer

echo ""

if [[ "$user_answer" = "Y" || "$user_answer" = "y" ]]
then
    if [ ! -d "$INSTALLATTION_DIRECTORY" ]
    then
        mkdir $INSTALLATION_DIRECTORY
    else
        rm -r $INSTALLATION_DIRECTORY
        mkdir $INSTALLATION_DIRECTORY
    fi

    echo "Building the script root at $INSTALLATION_DIRECTORY"
    #Moving the Scripts to the INSTALLATION_DIRECTORY
    cp -r * $INSTALLATION_DIRECTORY
    chmod 755 -R /opt/download_organizer
    chown $USER -R /opt/download_organizer
    echo "Script root at $INSTALLATION_DIRECTORY created!"

    #Moving the SHELL SCRIPT(COMMAND) to the /bin directory
    echo "Creating the command: download_organizer"
    chmod +x download_organizer
    cp download_organizer /bin
    chown $USER /bin/download_organizer
    echo "Command succefully created!"
    echo "Command \"download_organizer\" created!"

    #Creating the service
    service_file="/etc/systemd/system/download_organizer_startup.service"

    echo "[Unit]" > $service_file
    echo "Description=Run the download_organizer a service that organize the download folder" >> $service_file
    echo "DefaultDependencies=no" >> $service_file
    echo "After=network.target" >> $service_file

    echo "" >> $service_file
    echo "[Service]" >> $service_file
    echo "Type=simple" >> $service_file
    echo "User=$USER" >> $service_file
    echo "ExecStart=/bin/download_organizer" >> $service_file
    echo "TimeoutStartSec=0" >> $service_file
    echo "RemainAfterExit=yes" >> $service_file
    
    echo "" >> $service_file
    echo "[Install]" >> $service_file
    echo "WantedBy=default.target" >> $service_file

    systemctl daemon-reload
    systemctl enable download_organizer_startup.service
    systemctl restart download_organizer_startup.service
    echo "Script Created! And already running!"
else
    echo "You didn't agree with us, sorry about that, hope see you soon :)!"
fi