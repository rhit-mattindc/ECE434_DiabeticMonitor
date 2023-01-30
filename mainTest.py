#!/usr/bin/env python3
import os
import csv
from datetime import datetime
from keyword import iskeyword
import math

####################################################################################################################################
def main():
    # This section will get the file we need with its path and open it with a csv reader
    pathName = os.getcwd() + "/ExcelFiles/"
    fileNames = os.listdir(pathName)
    if fileNames[0].endswith(".csv"):
        pathName += fileNames[0]
    filename = open(pathName, "r")
    file = csv.DictReader(filename)
    # This section will get the column of sugar values
    sugars = getSugarsFromFile(file)
    # This section will get the date
    date = getDate(fileNames[0])
    # This section will get the A1C value from these sugars
    a1c = getA1C(sugars)
    # This section will get the Highest sugar
    highest = getHighestSugar(sugars)
    # This section will get the lowest sugar
    lowest = getLowestSugar(sugars)

# General print statements for debugging
    # print(sugars)
    # print(len(sugars))
    print("Date: ", date.strftime('%m-%d-%Y'))
    print("A1C: ", a1c)
    print("Highest: ", highest)
    print("Lowest: ", lowest)
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
        date = datetime(year = int(fileName[29:33]), month = int(fileName[34:36]), day = int(fileName[37:39]))
    return date
####################################################################################################################################
def getHighestSugar(sugars):
    sugars.sort()
    return sugars[-1]

def getLowestSugar(sugars):
    sugars.sort()
    return sugars[0]
####################################################################################################################################
# This is a call to main to get the ball rolling
main()
# END FILE
####################################################################################################################################
