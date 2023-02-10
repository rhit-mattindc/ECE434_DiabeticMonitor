#!/usr/bin/env python3
import os
import csv
import time
import subprocess
import shlex
import Adafruit_BBIO.GPIO as GPIO
from datetime import datetime
from subprocess import call

####################################################################################################################################
# For the LEDs with 220 Ohm resistors:
#     Red is P9_11
#     Green is P9_15
#     Blue is P9_21
#     Yellow is P9_23
# The LCD is connected to SPI 1:
#     VCC is P9_4
#     GND is P9_2
#     CS is P9_28
#     RESET is P9_25
#     D/C is P9_27
#     MOSI is P9_30
#     SCK is P9_31
#     LED is P9_16
#     MISO is P9_29
####################################################################################################################################
def main():
    # This section will get the file we need with its path and open it with a csv reader
    systemRunningLED(True)
    startTime = time.perf_counter()
    pathName = os.getcwd() + "/ExcelFiles/"
    newestFile = getNewestFile(pathName)
    pathName += newestFile
    filename = open(pathName, "r")
    file = csv.DictReader(filename)
    # This section will get the column of sugar values *****THIS IS WHAT TAKES SO LONG*****
    sugars = getSugarsFromFile(file)
    # This section will get the date
    currentDate = getDate(newestFile)
    # This section will get the time
    currentTime = getTimeEastern(newestFile)
    # This section will get the A1C value from these sugars
    a1c = getA1C(sugars)
    # This section will get the current sugar
    currentSugar = sugars[-1]
    # This section will sort the sugars from lowest to highest
    sugars.sort()
    # This section will get the Highest sugar
    highest = sugars[-1]
    # This section will get the lowest sugar
    lowest = sugars[0]

    endTime = time.perf_counter()
    runTime = endTime - startTime
    # This section will display the info to the LCD screen
    subprocess.call(shlex.split(f"./text.sh {currentDate.strftime('%m-%d-%Y')} {currentTime} {round(a1c, 1)} {currentSugar} {highest} {lowest} {round(runTime, 2)}"))
    # This section will handle the LEDs
    sugarLevelLED(currentSugar)
    systemRunningLED(False)
    ########## General print statements for debugging ##########
    # print(sugars)
    # print(len(sugars))
    print("Date: ", currentDate.strftime('%m-%d-%Y'))
    print("Time: ", currentTime)
    print("A1C: ", round(a1c, 1))
    print("Current: ", currentSugar)
    print("Highest: ", highest)
    print("Lowest: ", lowest)
    print("Runtime: ", round(runTime, 2), "seconds")
####################################################################################################################################
def getNewestFile(pathName):
    fileNames = os.listdir(pathName)
    newestDate = datetime(2000, 1, 1, 1, 00, 00)
    newestFile = ""
    for i in range(0, len(fileNames)):
        if (fileNames[i].endswith(".csv")):
            currentDate = getDate(fileNames[i])
            if ((currentDate - newestDate).total_seconds() > 0):
                newestDate = currentDate
                newestFile = fileNames[i]
    return newestFile
####################################################################################################################################
def getSugarsFromFile(file):
    # This section will get all of the sugar values we need from the csv file, remove the first 10 we dont need, and return them
    tempArray = []
    # This will get the array
    for col in file:
        tempArray.append(col["Glucose Value (mg/dL)"])
    # This will get rid of the first 10
    for i in range(0, 10):
        tempArray.pop(0)
    # This will remove any Highs
    value = 'High'
    while (value in tempArray):
        tempArray.remove(value)
    # This will turn all strings to ints
    tempArray2 = [int(numeric_string) for numeric_string in tempArray]
    return tempArray2
####################################################################################################################################
def getA1C(sugars):
    averageSugar = getAverage(sugars)
    a1c = (41.6 + averageSugar) / 28.7
    return a1c
####################################################################################################################################
def getAverage(sugars):
    return sum(sugars) / len(sugars)
####################################################################################################################################
def getDate(fileName):
    if fileName.endswith(".csv"):
        currentDate = datetime(year = int(fileName[29:33]), month = int(fileName[34:36]), day = int(fileName[37:39]), hour = int(fileName[40:42]), minute = int(fileName[42:44]), second = int(fileName[44:46]))
    return currentDate
####################################################################################################################################
def getTimeEastern(fileName):
    if fileName.endswith(".csv"):
        hour = fileName[40:42]
        minute = fileName[42:44]
        second = fileName[44:46]
        if (hour == "04"):
            hour = "23"
        elif (hour == "03"):
            hour = "22"
        elif (hour == "02"):
            hour = "21"
        elif (hour == "01"):
            hour = "20"
        elif (hour == "00"):
            hour = "19"
        else:
            hour = str(int(hour) - 5)
        # easternTimeMilitary = hour + "::" + minute + "::" + second
        if (hour == "13"):
            hour = "1"
        elif (hour == "14"):
            hour = "2"
        elif (hour == "15"):
            hour = "3"
        elif (hour == "16"):
            hour = "4"
        elif (hour == "17"):
            hour = "5"
        elif (hour == "18"):
            hour = "6"
        elif (hour == "19"):
            hour = "7"
        elif (hour == "20"):
            hour = "8"
        elif (hour == "21"):
            hour = "9"
        elif (hour == "22"):
            hour = "10"
        elif (hour == "23"):
            hour = "11"
        elif (hour == "00"):
            hour = "12"
        easternTimeStandard = hour + "::" + minute + "::" + second
        currentTime = datetime.strptime(easternTimeStandard, '%H::%M::%S').time()
    return currentTime
####################################################################################################################################
def sugarLevelLED(currentSugar):
    RED = "P9_11"
    GREEN = "P9_15"
    BLUE = "P9_21"
    GPIO.setup(RED, GPIO.OUT)
    GPIO.setup(GREEN, GPIO.OUT)
    GPIO.setup(BLUE, GPIO.OUT)
    if (currentSugar >= 170):
        GPIO.output(RED, GPIO.HIGH)
        GPIO.output(GREEN, GPIO.LOW)
        GPIO.output(BLUE, GPIO.LOW)
    elif (currentSugar < 170 and currentSugar > 70):
        GPIO.output(RED, GPIO.LOW)
        GPIO.output(GREEN, GPIO.HIGH)
        GPIO.output(BLUE, GPIO.LOW)
    elif (currentSugar <= 70):
        GPIO.output(RED, GPIO.LOW)
        GPIO.output(GREEN, GPIO.LOW)
        GPIO.output(BLUE, GPIO.HIGH)
    else:
        GPIO.output(RED, GPIO.HIGH)
        GPIO.output(GREEN, GPIO.HIGH)
        GPIO.output(BLUE, GPIO.HIGH)
####################################################################################################################################
def systemRunningLED(running):
    YELLOW = "P9_23"
    GPIO.setup(YELLOW, GPIO.OUT)
    if (running):
        GPIO.output(YELLOW, GPIO.HIGH)
    else:
        GPIO.output(YELLOW, GPIO.LOW)
####################################################################################################################################
# This is a call to main to get the ball rolling
if __name__ == '__main__':
    newExcelPull = call("./getNewExcel.sh", shell=True)
    main()
# END FILE
####################################################################################################################################
