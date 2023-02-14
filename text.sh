#!/bin/sh
# File Name: text.sh
# Author: David Mattingly, Eddie Mannan
# Date Created: 13FEB2023
# Date last edited: 13FEB2023
# Topic: ECE434 Embedded Linux, Dr. Yoder
# Project: Diabetic Monitor
# Description: Will write the diabetic data to the LCD screen

# Make a blank image
SIZE=320x240
TMP_FILE=/tmp/frame.png

# Write the values the shell script takes in to the screen
convert -background black -fill white -font Times-Roman -pointsize 24 \
      -size $SIZE \
      label:'Eddie Mannan Dexcom Monitor' \
      -draw "text 0,50 'Date: $1'" \
      -draw "text 0,75 'Time: $2'" \
      -draw "text 0,100 'A1C: $3'" \
      -draw "text 0,125 'Current Sugar: $4'" \
      -draw "text 0,150 'Highest Sugar: $5'" \
      -draw "text 0,175 'Lowest Sugar: $6'" \
      -draw "text 0,200 'Computation Time: $7 seconds'" \
      $TMP_FILE

sudo fbi -noverbose -T 1 $TMP_FILE
