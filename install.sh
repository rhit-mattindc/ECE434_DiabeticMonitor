#!/bin/sh
# File Name: install.sh
# Author: David Mattingly, Eddie Mannan
# Date Created: 07FEB2023
# Date last edited: 07FEB2023
# Topic: ECE434 Embedded Linux, Dr. Yoder
# Project: Diabetic Monitor
# Description: Sets the program to run every 5 minutes

echo 'Warning: install requires a reboot to enable the FBI device tree.'
echo 'Enter ABORT to go back and save work, anything else to run install.'
read userinput

if $userinput -eq 'ABORT'; then
    exit 1
fi

# Install modules/packages
# apt install fbi

# Configure git
# git config pull.rebase false

# Configure autorun in crontab
if ! grep -q "Diabetic" /etc/crontab; then
    echo "*/1 * * * * debian ~/ECE434_DiabeticMonitor/autorun.sh >> ~/ECE434_DiabeticMonitor/cron.log" >> /etc/crontab
fi

# reboot

