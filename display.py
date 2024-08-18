import csv
import math
import numpy as np
import matplotlib.pyplot as plt

rownum = 0
class band():
    def __init__(self, bandLetter):
        self.letter = bandLetter
        self.manualPA = []
        self.SFRAVG = []
        self.SFR100 = []
        self.SFRFUV = []
        self.sSFR = []
        self.name = []
    def addRow(self,row):
        try:       
            #a = float(row[8])
            b = float(row[6])
            #c = float(row[7])
        except:
            return
        #self.SFRAVG.append(float(row[8]))
        self.SFR100.append(float(row[6]))
        #self.SFRFUV.append(float(row[7]))
        self.manualPA.append(float(row[3]))
        self.name.append(str(row[0]).strip())
        self.sSFR.append(float(row[6]) / (10 ** float(row[9])))

gband = band('g')
iband = band('i')
rband = band('r')
uband = band('u')
zband = band('z')




surveyfile = open("my_csv.csv",'r')	#open csv file with UG survey data

for row in csv.reader(surveyfile): 		#Read pairs file row by row
    if (rownum > 2):
        if (str(row[1]) == 'g'):
            gband.addRow(row)
        elif (str(row[1]) == 'i'):
            iband.addRow(row)
        elif (str(row[1]) == 'r'):
            rband.addRow(row)
        elif (str(row[1]) == 'u'):
            uband.addRow(row)
        elif (str(row[1]) == 'z'):
            zband.addRow(row)
    rownum = rownum + 1


plt.scatter(gband.manualPA,gband.SFR100,color='blue', label='G Band')
plt.scatter(iband.manualPA,iband.SFR100,color='red', label='I Band')
plt.scatter(rband.manualPA,rband.SFR100,color='green', label='R Band')
plt.scatter(uband.manualPA,uband.SFR100,color='orange', label='U Band')
plt.scatter(zband.manualPA,zband.SFR100,color='purple', label='Z Band')

plt.plot(np.unique(iband.manualPA), np.poly1d(np.polyfit(iband.manualPA, iband.SFR100, 1))(np.unique(iband.manualPA)))

""" plt.scatter(zband.manualPA,zband.SFRAVG,color='purple')
plt.scatter(uband.manualPA,uband.SFRAVG,color='black')
plt.scatter(rband.manualPA,rband.SFRAVG,color='green')
plt.scatter(iband.manualPA,iband.SFRAVG,color='red')
plt.scatter(gband.manualPA,gband.SFRAVG,color='blue') """



plt.ylabel("SFR")
plt.xlabel("Pitch angle")

plt.legend()

plt.show()
