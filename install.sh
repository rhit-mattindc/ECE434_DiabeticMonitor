#!/bin/sh
# File Name: install.sh
# Author: David Mattingly, Eddie Mannan
# Date Created: 07FEB2023
# Date last edited: 07FEB2023
# Topic: ECE434 Embedded Linux, Dr. Yoder
# Project: Diabetic Monitor
# Description: Sets the program to run every 5 minutes

# Install modules/packages
# apt install fbi

# Configure git
git config pull.rebase false

# Configure autorun in crontab
if ! grep -q "Diabetic" /etc/crontab; then
    echo "*/5 * * * * root ~/ECE434_DiabeticMonitor/autorun.sh" >> /etc/crontab
fi

