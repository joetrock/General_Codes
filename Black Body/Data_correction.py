import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt(r"C:\Users\Joetrock\OneDrive - Georgia Institute of Technology\School\Advanced Lab\Black Body\Temp-Voltage_data.txt",usecols=(0, 1, 2))
t = data[:,0]
T = data[:,1]
V = data[:,2]
Tcalc = V/(t-200)

f, (ax1,ax2,ax3,ax4) = plt.subplots(1,4)
ax1.plot(t,T)
ax2.plot(t,V)
ax3.plot(t,V/T)
ax4.plot(t,Tcalc)
plt.show()