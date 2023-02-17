#!/bin/sh
# File Name: autorun.sh
# Author: David Mattingly, Eddie Mannan
# Date Created: 13FEB2023
# Date last edited: 13FEB2023
# Topic: ECE434 Embedded Linux, Dr. Yoder
# Project: Diabetic Monitor
# Description: Tells the Kernal what to run when the Beagle first boots

git pull

python3 mainTest.py

echo 'hi' >> ~/ECE434_DiabeticMonitor/cronlog.txt
