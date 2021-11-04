import matplotlib.pyplot as plt
import numpy as np

# Data importing
data1 = np.genfromtxt(r"C:\Users\Joetrock\OneDrive - Georgia Institute of Technology\School\Advanced Lab\Double Slit\Non-Pasco Data\I - Double_slit.txt",usecols=(0, 1))
data2 = np.genfromtxt(r"C:\Users\Joetrock\OneDrive - Georgia Institute of Technology\School\Advanced Lab\Double Slit\Non-Pasco Data\II - Single_slit_left.txt",usecols=(0, 1))
data3 = np.genfromtxt(r"C:\Users\Joetrock\OneDrive - Georgia Institute of Technology\School\Advanced Lab\Double Slit\Non-Pasco Data\III - Single_slit_right.txt",usecols=(0, 1))
data4 = np.genfromtxt(r"C:\Users\Joetrock\OneDrive - Georgia Institute of Technology\School\Advanced Lab\Double Slit\Non-Pasco Data\IV - Single_photon_interference.txt",usecols=(0, 2))

# Double slit laser data
t1 = data1[225:,0]
dis1 = (t1/(6.4*0.5))-15
I1 = data1[225:,1]

# Ploting double slit
plt.plot(dis1,I1)
plt.xlabel("Distance (mm)")
plt.ylabel("Intensity")
plt.title("Double Slit")
plt.grid()
plt.show()

# Single slit data
t2 = data2[200:,0]
dis2 = (t2/(6.4*0.5))-13.5
I2 = data2[200:,1]
t3 = data3[201:,0]
dis3 = (t3/(6.4*0.5))-13.5
I3 = data3[200:,1]

# Single slit FFT
s1 = np.fft.rfft(I2)
N1 = round(len(s1)/50)
s1[N1:len(s1)] = 0
slit1 = np.fft.irfft(s1)
s2 = np.fft.rfft(I3)
N2 = round(len(s2)/50)
s2[N2:len(s2)] = 0
slit2 = np.fft.irfft(s2)

# Changing Y axis to % of max intensity
max1 = np.max(slit1)
slit1 = (slit1/max1) *100
max2 = np.max(slit2)
slit2 = (slit2/max2) *100

# Plotting single slits
plt.plot(dis2,slit1,label="Left")
plt.plot(dis3,slit2,label="Right")
plt.legend()
plt.xlabel("Distance (mm)")
plt.ylabel("% of Max Intensity")
plt.title("Single Slits")
plt.grid()
plt.show()

# Photon count data
t4 = data4[250:850,0]
dis4 = (t4/(6.4*0.5))-10
count = data4[250:850,1]

# Photon FFT
c = np.fft.rfft(count)
N3 = round(len(c)/10)
c[N3:len(c)] = 0
countfft = np.fft.irfft(c)

# Ploting photon count
plt.plot(dis4,count,'.')
plt.plot(dis4,countfft)
plt.xlabel("Distance (mm)")
plt.ylabel("Count")
plt.title("Photon Counter")
plt.grid()
plt.show()