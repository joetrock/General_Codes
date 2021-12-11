import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import rfft,irfft
import csv

with open(r"C:\Users\Joetrock\Desktop\GTMS\12-4.csv") as Raw_data:
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
            accy.append(float(row[2]))
            accz.append(float(row[3]))
            accx.append(float(row[4]))
            Linecount += 1


    accyf = rfft(accy)
    N = round(len(accyf)*.01)
    accyf[N:len(accyf)] = 0
    accyt = irfft(accyf)
    one = np.ones(len(accy))
    none = np.ones(len(accy))*-1
    neu = accyt[258000:273000]
    pro = accyt[357200:372200]
    prot = (accyt[390000:405000])*-1
    promt = accyt[428500:443500]
    onen = np.ones(len(pro))
    nonen = np.ones(len(pro))*-1

    plt.plot(promt,'r',label = 'pro + more rear toe')
    plt.plot(pro,'b',label = 'pro')
    plt.plot(onen,'k',nonen,'k')
    plt.legend()
    #plt.plot(accy,'r',accyt,'b',one,'k',none,'k')
    plt.xlabel('Data point')
    plt.ylim([-2,2])
    plt.ylabel('Lateral Acceleration (G)')
    plt.grid()
    
    #fig, (axx,axy,axz) = plt.subplots(3,1,sharex = True)
    #axx.plot(accx,'g')
    #axx.set_ylabel('$a_x$ (G)')
    #axx.grid()
    #axy.plot(accy,'r',accyt,'k')
    #axy.set_ylabel('$a_y$ (G)')
    #axy.grid()
    #axz.plot(accz)
    #axz.set_ylabel('$a_z$ (G)')
    #axz.grid()
    #plt.xlabel('time (s)')
    plt.show()