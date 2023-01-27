#!/usr/bin/env python3
import random
import time

values = []
numberOfValues = 30000
start = 50
end = 400
average = 0.0

# This loop will create an array of length NUMBEROFVALUES and fill it with random ints between START and END
for i in range(numberOfValues):
    values.append(random.randint(start, end))

# This loop will print all of the array values
# for each in values:
#     print(each)

# Find the average of the array and print it
startTime = time.perf_counter()
average = sum(values) / len(values)
endTime = time.perf_counter()
runTime = endTime - startTime

# Print our values
print("The array length is: ", numberOfValues)
print("The average is: ", average)
print("Runtime: ", runTime * 1000, "ms")