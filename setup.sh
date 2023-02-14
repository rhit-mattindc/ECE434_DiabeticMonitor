#!/bin/sh
# File Name: setup.sh
# Author: David Mattingly, Eddie Mannan
# Date Created: 13FEB2023
# Date last edited: 13FEB2023
# Topic: ECE434 Embedded Linux, Dr. Yoder
# Project: Diabetic Monitor
# Description: Configures BeagleBone for running project from reboot

# Get most up-to-date code, excel sheets
git pull

# Run actual file
python3 mainTest.py