#!/bin/sh
# File Name: install.sh
# Author: David Mattingly, Eddie Mannan
# Date Created: 07FEB2023
# Date last edited: 07FEB2023
# Topic: ECE434 Embedded Linux, Dr. Yoder
# Project: Diabetic Monitor
# Description: Sets the program to run every 5 minutes

# Install modules/packages
apt install fbi
apt install imagemagick

# Add device tree to uEnv.txt
line=$(grep "uboot_overlay_addr4" /boot/uEnv.txt)
sed -i "s|$line|uboot_overlay_addr4=BB-LCD-ADAFRUIT-24-SPI1-00A0.dtbo|g" /boot/uEnv.txt

# Configure git
git config pull.rebase false

# Configure autorun in crontab
if ! grep -q "DiabeticMonitor" /etc/crontab; then
    echo "*/5 * * * * root /home/debian/ECE434_DiabeticMonitor/autorun.sh 2>&1 | logger" >> /etc/crontab
fi

echo "Reboot device to enable device overlay"

