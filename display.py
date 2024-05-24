import csv
import math
import numpy as np
import matplotlib.pyplot as plt

rownum = 0

gmanualPA = []
gSFRavg = []
gSFR100 = []
gSFRFUV = []
gname = []


surveyfile = open("my_csv.csv",'r')	#open csv file with UG survey data

for row in csv.reader(surveyfile): 		#Read pairs file row by row
    if (rownum > 2):
        if (str(row[1]) == 'g'):
            gname.append(str(row[0]).strip())
            gmanualPA.append(float(row[3]))  
            try:       
                gSFRavg.append(float(row[8]))
            except:
                gSFRavg.append(0)
            try:       
                gSFR100.append(float(row[6]))
            except:
                gSFR100.append(0)
            try:       
                gSFRFUV.append(float(row[7]))
            except:
                gSFRFUV.append(0)
    rownum = rownum + 1


plt.scatter(gmanualPA,gSFRavg,color='blue')
plt.scatter(gmanualPA,gSFR100,color='red')
plt.scatter(gmanualPA,gSFRFUV,color='green')


plt.ylabel("SFR")
plt.xlabel("Pitch angle")

plt.show()
