
# ECE434_DiabeticMonitor

Embedded Linux Final Project

Eddie Mannan, David Mattingly

## Setup

### Install

Clone this repository under the name ECE434_DiabeticMonitor.
Run install.sh

### Pinout

| Pin   | Connection |
| --- |  --- |
| P9_11 | Red LED    |
| P9_15 | Green LED  |
| P9_21 | Blue LED   |
| P9_23 | Yellow LED |
| P9_04 | LCD VCC    |
| P9_02 | LCD GND    |
| P9_28 | LCD CS     |
| P9_25 | LCD RESET  |
| P9_27 | LCD D/C    |
| P9_30 | LCD MOSI   |
| P9_31 | LCD SCK    |
| P9_16 | LCD LED    |
| P9_29 | LCD MISO   |

## Project Discription
This project is meant to make handling Type 1 Diabetes easier. The project will take a Dexcom .csv file full of blood sugar data, pull the values from this file, and output various data points to the user such as:

Eddie Mannan Dexcom Monitor
Date: XX-XX-XXXX
Time: XX:XX:XX
A1C: XXX
Current Sugar: XXX
Highest Sugar: XXX
Lowest Sugar: XXX
Computation Time: X.XX seconds

Next