import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt(r"C:\Users\Joetrock\OneDrive - Georgia Institute of Technology\School\Advanced Lab\Black Body\Temp-Voltage_data.txt",usecols=(0, 1, 2))

t = data[4:800,0]
Tc = data[4:800,1]
V = data[4:800,2]
W = (V/22.69)*0.001
T = Tc+273
f,axs = plt.subplots(2,2)
axs[0,0].plot(t,T)
axs[0,0].set_title('Temperature(K) vs. time(s)')
axs[0,1].plot(t,W)
axs[0,1].set_title('Pressure(W/m^2) vs. time(s)')
axs[1,0].plot(t,T/W)
axs[1,0].set_title('Temp/Pressure(K*m^2/W) vs. time(s)')
axs[1,1].plot(T,W)
axs[1,1].set_title('Pressure(W/m^2) vs. Temp(K)')
plt.show()