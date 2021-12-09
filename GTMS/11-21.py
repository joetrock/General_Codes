import matplotlib.pyplot as plt
import numpy as np
import csv

with open(r"C:\Users\Joetrock\Desktop\GTMS\11-21.csv") as Raw_data:
    csv_reader = csv.reader(Raw_data, delimiter = ",")
    t = []
    throttle = []
    accx = []
    accy = []
    accz = []
    Linecount = 0
    for row in csv_reader:
        if Linecount == 0 or Linecount == 1:
            Linecount += 1
        else:
            t.append(float(row[0]))
            throttle.append(float(row[1]))
            accx.append(float(row[2]))
            accz.append(float(row[3]))
            accy.append(float(row[4]))
            Linecount += 1

    t = t[45000:72500]
    throttle = throttle[45000:72500]
    accx = accx[45000:72500]
    accy = accy[45000:72500]
    accz = accz[45000:72500]

    fig, (axx,axy,axz) = plt.subplots(3,1,sharex = True)
    axx.plot(t,accx,'r')
    axx.set_ylabel('$a_x$ (G)')
    axx.grid()
    axy.plot(t,accy,'g')
    axy.set_ylabel('$a_y$ (G)')
    axy.grid()
    axz.plot(t,accz)
    axz.set_ylabel('$a_z$ (G)')
    axz.grid()
    plt.xlabel('time (s)')
    plt.show()