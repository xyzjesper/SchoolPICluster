#!/bin/bash

NAME=$1
PASSWORD=$2
USERFILE="/home/pi/name.txt"

if [[ ! $NAME || ! $PASSWORD ]]; then
    echo "Bitte Skript wie folgt aufrufen:"
    echo "./meinsmeinsmeins.sh <Vorname> <Passwort>"
    exit 1
fi

echo $NAME > $USERFILE 
echo "pi:$PASSWORD" | sudo chpasswd
sudo reboot
