#! /usr/bin/python

TEMP_PATH="/sys/class/thermal/thermal_zone0/"

#fo = open(TEMP_PATH + "temp", "r")
#temp = fo.read()
#print(temp)

def readTemp():
    fo = open(TEMP_PATH + "temp", "r")
    value = float(fo.read())
    temp = value*0.001
    return temp

times = int(input("How many times do you want to read the temperature? "))

def avg(times):
    temperature = 0

    for i in range (0,times):

        temperature+=readTemp()
        
    average = temperature/times
    return average

print(avg(times))
