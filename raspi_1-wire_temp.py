#!/usr/bin/python3

probe_adress = "/sys/bus/w1/devices/28-0000067040a8/w1_slave"

with open(probe_adress, 'r') as file:
    raw_reading = file.read()

temp = int(raw_reading[~5:])/1000
print(f"Temp is {temp:.2f}°C")
