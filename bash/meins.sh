#!/bin/bash

#  Global Variabels
NAME=$1
PASSWORD=$2
USERFILE="/home/pi/meins.txt"


# Check Command Parameter
if [[ ! $NAME && ! $PASSWORD ]]; then
    echo "Use command <name> <password>"
    exit 1
fi

if [[ ! $NAME  ]]; then
    echo "No name provided in command."
    exit 1
fi
if [[ ! $PASSWORD  ]]; then
    echo "No password provided in command."
    exit 1
fi


if [ -f $USERFILE ]; then
    echo "\"Meins Meins\" will override the current data!"
    echo "Claiming the PaspberryPI and update the password"

    echo "Override the userdata in $USERFILE"
    echo $NAME >> $USERFILE 

    echo "Changing password to your input."
    echo "pi:$PASSWORD" | sudo chpasswd

    echo "Reboot the PaspberryPI"
    reboot
else
    echo "You want to claim this PaspberryPI as \"meins\"..."
    echo "Claiming the PaspberryPI and update the password"
    
    echo $NAME >> $USERFILE 

    echo "pi:$PASSWORD" | sudo chpasswd

    echo "Reboot the PaspberryPI"
    reboot
fi



