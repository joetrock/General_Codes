import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt(r"C:\Users\Joetrock\OneDrive - Georgia Institute of Technology\School\Advanced Lab\Black Body\Temp-Voltage_data.txt",usecols=(0, 1, 2))

t = data[:,0]
T = data[:,1]
V = data[:,2]
Tcalc = (V/(np.exp(1/(t-200))))-V

plt.plot(t,Tcalc)
plt.show()