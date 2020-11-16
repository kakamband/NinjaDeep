#!/bin/bash
clear
echo "
                          ₦Ї₦ℑ₳
                   #########     #########  ########    ########
                   #         #   #          #           #        #
                   #         #   ######     ######      #        #
                   #         #   #          #           ########
                   #########     #########  ########    #
"
# Termux session string generator for NinjaDeep
echo Starting dependency installation in 5 seconds...
sleep 5
apt-get update
apt-get upgrade -y
pkg upgrade -y
pkg install python wget -y
wget https://raw.githubusercontent.com/Lovedeep-ViRk/NinjaDeep/master/resources/ninjadeep-setup.py
pip install telethon
python ninjadeep-setup.py
