#!/usr/bin/env python3
import datetime as dt

yesterday = dt.datetime(2013,12,30,23,59,59) 
today = dt.datetime(2013,12,31,23,59,59)

print("Yesterday - Today: ", (yesterday - today).total_seconds())
print("Today - Yesturday: ", (today - yesterday).total_seconds())
