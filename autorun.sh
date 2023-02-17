#!/bin/sh
# File Name: autorun.sh
# Author: David Mattingly, Eddie Mannan
# Date Created: 13FEB2023
# Date last edited: 17FEB2023
# Topic: ECE434 Embedded Linux, Dr. Yoder
# Project: Diabetic Monitor
# Description: Called by crontab, runs the main code

git pull

python3 /home/debain/ECE434_DiabeticMonitor/mainTest.py

