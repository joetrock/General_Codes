import matplotlib.pyplot as plt
import numpy as np
import csv

# Raw Laser Data
with open(r"C:\Users\Joetrock\OneDrive - Georgia Institute of Technology\School\Advanced Lab\Double Slit\Pasco Data\Raw Laser Data.csv") as Raw_data:
    csv_reader = csv.reader(Raw_data, delimiter = ",")
    int = []
    dis = []
    Linecount = 0
    for row in csv_reader:
        if Linecount == 0:
            Linecount += 1
        else:
            int.append(float(row[0]))
            dis.append((float(row[1])-0.0675)*100)

    plt.plot(dis,int)
    plt.title("Raw Laser")
    plt.xlabel("Distance (mm)")
    plt.xlim([0,7.35])
    plt.ylabel("Light Intensity")
    plt.ylim([0,105])
    plt.grid()
    plt.show()

# Varying Slit count
with open(r"C:\Users\Joetrock\OneDrive - Georgia Institute of Technology\School\Advanced Lab\Double Slit\Pasco Data\Multi-Slit Data.csv") as multi_data:
    csv_reader = csv.reader(multi_data, delimiter = ",")
    int1 = []
    dis1 = []
    int2 = []
    dis2 = []
    int3 = []
    dis3 = []
    int4 = []
    dis4 = []
    int5 = []
    dis5 = []
    Linecount = 0
    for row in csv_reader:
        if Linecount == 0:
            Linecount += 1
        elif row[6] == '':
            int5.append(float(row[8]))
            dis5.append((float(row[9])-0.04)*100)
            Linecount += 1
        elif row[4] == '':
            int4.append(float(row[6]))
            dis4.append((float(row[7])-0.04)*100)
            int5.append(float(row[8]))
            dis5.append((float(row[9])-0.04)*100)
            Linecount += 1
        elif row[2] == '':
            int3.append(float(row[4]))
            dis3.append((float(row[5])-0.04)*100)
            int4.append(float(row[6]))
            dis4.append((float(row[7])-0.04)*100)
            int5.append(float(row[8]))
            dis5.append((float(row[9])-0.04)*100)
            Linecount += 1
        elif row[0] == '':
            int2.append(float(row[2]))
            dis2.append((float(row[3])-0.04)*100)
            int3.append(float(row[4]))
            dis3.append((float(row[5])-0.04)*100)
            int4.append(float(row[6]))
            dis4.append((float(row[7])-0.04)*100)
            int5.append(float(row[8]))
            dis5.append((float(row[9])-0.04)*100)
            Linecount += 1
        else:
            int1.append(float(row[0]))
            dis1.append((float(row[1])-0.04)*100)
            int2.append(float(row[2]))
            dis2.append((float(row[3])-0.04)*100)
            int3.append(float(row[4]))
            dis3.append((float(row[5])-0.04)*100)
            int4.append(float(row[6]))
            dis4.append((float(row[7])-0.04)*100)
            int5.append(float(row[8]))
            dis5.append((float(row[9])-0.04)*100)
            Linecount += 1

    plt.plot(dis1,int1,label = "Single Slit")
    plt.plot(dis2,int2,label = "Double Slit")
    plt.plot(dis3,int3,label = "Triple Slit")
    plt.plot(dis4,int4,label = "Quadruple Slit")
    plt.plot(dis5,int5,label = "Quintople Slit")
    plt.title("Multi-Slit Inteference")
    plt.legend()
    plt.xlabel("Distance (mm)")
    plt.xlim([0,11])
    plt.ylabel("Light Intensity")
    plt.ylim([0,50])
    plt.grid()
    plt.show()

# Varying Distance
with open(r"C:\Users\Joetrock\OneDrive - Georgia Institute of Technology\School\Advanced Lab\Double Slit\Pasco Data\Varying Distance Data.csv") as Dist_data:
    csv_reader = csv.reader(Dist_data, delimiter = ",")
    int1 = []
    dis1 = []
    int2 = []
    dis2 = []
    int3 = []
    dis3 = []
    int4 = []
    dis4 = []
    int5 = []
    dis5 = []
    Linecount = 0
    for row in csv_reader:
        if Linecount == 0:
            Linecount += 1
        elif row[6] == '':
            int2.append(float(row[2]))
            dis2.append((float(row[3])-0.065)*100)
            Linecount += 1
        elif row[4] == '':
            int2.append(float(row[2]))
            dis2.append((float(row[3])-0.065)*100)
            int4.append(float(row[6]))
            dis4.append((float(row[7])-0.065)*100)
            Linecount += 1
        elif row[8] == '':
            int2.append(float(row[2]))
            dis2.append((float(row[3])-0.065)*100)
            int3.append(float(row[4]))
            dis3.append((float(row[5])-0.065)*100)
            int4.append(float(row[6]))
            dis4.append((float(row[7])-0.065)*100)
            Linecount += 1
        elif row[0] == '':
            int2.append(float(row[2]))
            dis2.append((float(row[3])-0.065)*100)
            int3.append(float(row[4]))
            dis3.append((float(row[5])-0.065)*100)
            int4.append(float(row[6]))
            dis4.append((float(row[7])-0.065)*100)
            int5.append(float(row[8]))
            dis5.append((float(row[9])-0.065)*100)
            Linecount += 1
        else:
            int1.append(float(row[0]))
            dis1.append((float(row[1])-0.055)*100)
            int2.append(float(row[2]))
            dis2.append((float(row[3])-0.065)*100)
            int3.append(float(row[4]))
            dis3.append((float(row[5])-0.065)*100)
            int4.append(float(row[6]))
            dis4.append((float(row[7])-0.065)*100)
            int5.append(float(row[8]))
            dis5.append((float(row[9])-0.065)*100)
            Linecount += 1

    plt.plot(dis1,int1,label = "20 cm")
    plt.plot(dis2,int2,label = "40 cm")
    plt.plot(dis3,int3,label = "60 cm")
    plt.plot(dis4,int4,label = "80 cm")
    plt.plot(dis5,int5,label = "100 cm")
    plt.title("Variable Distance Inteference")
    plt.legend()
    plt.xlabel("Distance (mm)")
    plt.xlim([0,8])
    plt.ylabel("Light Intensity")
    plt.ylim([0,10])
    plt.grid()
    plt.show()

# Varying Slit Variables
with open(r"C:\Users\Joetrock\OneDrive - Georgia Institute of Technology\School\Advanced Lab\Double Slit\Pasco Data\Varying Slit Variables Data.csv") as variable_data:
    csv_reader = csv.reader(variable_data, delimiter = ",")
    int1 = []
    dis1 = []
    int2 = []
    dis2 = []
    int3 = []
    dis3 = []
    int4 = []
    dis4 = []
    int5 = []
    dis5 = []
    Linecount = 0
    for row in csv_reader:
        if Linecount == 0:
            Linecount += 1
        elif row[6] == '':
            int5.append(float(row[8]))
            dis5.append((float(row[9])-0.075)*100)
            Linecount += 1
        elif row[4] == '':
            int4.append(float(row[6]))
            dis4.append((float(row[7])-0.075)*100)
            int5.append(float(row[8]))
            dis5.append((float(row[9])-0.075)*100)
            Linecount += 1
        elif row[2] == '':
            int3.append(float(row[4]))
            dis3.append((float(row[5])-0.075)*100)
            int4.append(float(row[6]))
            dis4.append((float(row[7])-0.075)*100)
            int5.append(float(row[8]))
            dis5.append((float(row[9])-0.075)*100)
            Linecount += 1
        elif row[0] == '':
            int2.append(float(row[2]))
            dis2.append((float(row[3])-0.075)*100)
            int3.append(float(row[4]))
            dis3.append((float(row[5])-0.075)*100)
            int4.append(float(row[6]))
            dis4.append((float(row[7])-0.075)*100)
            int5.append(float(row[8]))
            dis5.append((float(row[9])-0.075)*100)
            Linecount += 1
        else:
            int1.append(float(row[0]))
            dis1.append((float(row[1])+0.0085-0.075)*100)
            int2.append(float(row[2]))
            dis2.append((float(row[3])-0.075)*100)
            int3.append(float(row[4]))
            dis3.append((float(row[5])-0.075)*100)
            int4.append(float(row[6]))
            dis4.append((float(row[7])-0.075)*100)
            int5.append(float(row[8]))
            dis5.append((float(row[9])-0.075)*100)
            Linecount += 1

    plt.plot(dis1,int1,label = "a = 0.04 mm, d = 0.125 mm")
    plt.plot(dis2,int2,label = "a = 0.04 mm, d = 0.25 mm")
    plt.plot(dis3,int3,label = "a = 0.04 mm, d = 0.5 mm")
    plt.plot(dis4,int4,label = "a = 0.08 mm, d = 0.25 mm")
    plt.plot(dis5,int5,label = "a = 0.08 mm, d = 0.5 mm")
    plt.title("Variable Slit Variable Inteference")
    plt.legend()
    plt.xlabel("Distance (mm)")
    plt.xlim([0,5.35])
    plt.ylabel("Light Intensity")
    plt.ylim([0,10])
    plt.grid()
    plt.show()