import matplotlib.pyplot as plt
import numpy as np
import csv

with open(r"C:\Users\Joetrock\Desktop\GTMS\11-21.csv") as Raw_data:
    csv_reader = csv.reader(Raw_data, delimiter = ",")
    time = []
    throttle = []
    accx = []
    accy = []
    accz = []
    Linecount = 0
    for row in csv_reader:
        if Linecount == 0 or Linecount == 1:
            Linecount += 1
        else:
            time.append(float(row[0]))
            throttle.append(float(row[1]))
            accx.append(float(row[2]))
            accy.append(float(row[3]))
            accz.append(float(row[4]))
            Linecount += 1

    plt.plot(time,accx)
    plt.grid()
    plt.show()