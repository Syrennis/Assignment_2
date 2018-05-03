#The quadrant definitions are analagous to the original WH04
#EOF structures, with OMI +EOF2=Active over MC (4/5) and OMI EOF1
#=Active over IO (2/3). Here, the "warm pool" in the model
#is treated as the WP (6/7). Thus, active convection over
#the center of the domain (20,000 km) should correspond to +EOF2.

#Import needed functions and packages
import numpy as np
import pandas
from operator import itemgetter
import matplotlib.pyplot as plt
import collections

#Read in data for FMO indices
c = pandas.read_csv('FMO_indices.csv', header = 0)
PC1 = c["FMO1"]
PC2 = c["FMO2"]
FMO_phase = []
FMO_phases = []

#For loop to assign phases based off 2 leading EOFs
for i in range(len(c)):
  if PC1[i] > 0 and PC2[i] >= 0:
    if PC1[i] > PC2[i]:
      FMO_phase = 3
    else:
      FMO_phase = 4 # PC2.ge.PC1
     
  if PC1[i] <= 0 and PC2[i] > 0:
    if PC2[i] > abs(PC1[i]):
      FMO_phase = 5
    else:
      FMO_phase = 6 # abs(PC1).ge.PC2

  if PC1[i] < 0 and PC2[i] <= 0:
    if abs(PC1[i]) > abs(PC2[i]):
      FMO_phase = 7
    else:
      FMO_phase = 8 # abs(PC2).ge.abs(PC1)

  if PC1[i] >= 0 and PC2[i] < 0:
    if abs(PC2[i]) > PC1[i]:
      FMO_phase = 1
    else:
      FMO_phase = 2 # PC1.ge.abs(PC2)

  FMO_phases.append(FMO_phase)
  
FMO_phases = np.array(FMO_phases)

#Merge all data into one dataframe
span = np.array(list(range(12454)))
FMO = np.column_stack(((span,c,FMO_phases)))
cc = pandas.DataFrame(FMO)
cc = cc.rename(columns={0:"Index", 1:"Year", 2:"Month", 3:"Day", 4:"FMO1", 5:"FMO2", 6:"Amplitude", 7:"Phase"})

#Retain only data that has amplitude greater than 1
n = 1
cc = cc[cc["Amplitude"] >= n]

#Group data that is in consecutive days by finding consecutive numbers in "Index"
eventsFMO = []
for k,g in cc.groupby(cc["Index"] - np.arange(cc.shape[0])):
    eventsFMO.append(g)
    
#Collect phase information from all events   
FMOphases = list(map(itemgetter("Phase"), eventsFMO))

#Collect only terminating phase numbers for every event
TerminationFMO = []
for i in range(len(FMOphases)):
    FMOvalue = FMOphases[i].iloc[-1]
    TerminationFMO.append(FMOvalue)

#Frequency of terminating phases   
FMOcounter = list(collections.Counter(TerminationFMO).items())

FMOcount = pandas.DataFrame(FMOcounter)
FMOcount = FMOcount.rename(columns={0:"Phase", 1:"Frequency"})
FMOcount = FMOcount.sort_values(by=["Phase"])

#Plot hustogram of frequency of terminating phases
x = TerminationFMO
num_bins = 8
n, bins, patches = plt.hist(x, num_bins, facecolor='blue', alpha=1, edgecolor='black', linewidth=1.2)
plt.title("FMO Terminating Phases")
plt.xlabel("Phases")
plt.ylabel("Frequency")
plt.savefig("FMO.png")