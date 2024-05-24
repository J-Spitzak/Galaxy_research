import csv
import math
import numpy as np
import matplotlib.pyplot as plt

rownum = 0

gmanualPA = []
gSFRavg = []
gname = []

imanualPA = []
iSFRavg = []
iname = []

rmanualPA = []
rSFRavg = []
rname = []

umanualPA = []
uSFRavg = []
uname = []

zmanualPA = []
zSFRavg = []
zname = []

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
        elif (str(row[1]) == 'i'):
            iname.append(str(row[0]).strip())
            imanualPA.append(float(row[3]))        
            try:       
                iSFRavg.append(float(row[8]))
            except:
                iSFRavg.append(0)
        elif (str(row[1]) == 'r'):
            rname.append(str(row[0]).strip())
            rmanualPA.append(float(row[3]))        
            try:       
                rSFRavg.append(float(row[8]))
            except:
                rSFRavg.append(0)
        elif (str(row[1]) == 'u'):
            uname.append(str(row[0]).strip())
            umanualPA.append(float(row[3]))        
            try:       
                uSFRavg.append(float(row[8]))
            except:
                uSFRavg.append(0)
        elif (str(row[1]) == 'z'):
            zname.append(str(row[0]).strip())
            zmanualPA.append(float(row[3]))        
            try:       
                zSFRavg.append(float(row[8]))
            except:
                zSFRavg.append(0)
    rownum = rownum + 1


plt.scatter(gmanualPA,gSFRavg,color='blue')
plt.scatter(imanualPA,iSFRavg,color='red')
plt.scatter(rmanualPA,rSFRavg,color='green')
plt.scatter(umanualPA,uSFRavg,color='purple')
plt.scatter(zmanualPA,zSFRavg,color='black')

plt.ylabel("SFR")
plt.xlabel("Pitch angle")

plt.show()
