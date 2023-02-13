#!/bin/sh
# File Name: install.sh
# Author: David Mattingly, Eddie Mayfield
# Date Created: 07FEB2023
# Date last edited: 07FEB2023
# Topic: ECE434 Embedded Linux, Dr. Yoder
# Project: Diabetic Monitor
# Description: 

# Install modules/packages
# apt in`stall fbi


# Configure git
git config pull.rebase false

# Configure autorun in crontab
if ! grep -q "Diabetic" /etc/crontab; then
    echo "*/5 * * * * root ~/ECE434_DiabeticMonitor/autorun.sh" >> /etc/crontab
fi

