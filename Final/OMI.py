#The quadrant definitions are analagous to the original WH04
#EOF structures, with OMI +EOF2=Active over MC (4/5) and OMI EOF1
#=Active over IO (2/3). Here, the "warm pool" in the model
#is treated as the WP (6/7). Thus, active convection over
#the center of the domain (20,000 km) should correspond to +EOF2.

#Import needed functions and packages
import matplotlib.pyplot as plt
import numpy as np
import pandas
from operator import itemgetter
import collections

#Read in data for OMI indices
b = pandas.read_csv('OMI_indices.csv', header = 0)
PC1 = b["OMI1"]
PC2 = b["OMI2"]
OMI_phase = []
OMI_phases = []

#For loop to assign phases based off 2 leading EOFs
for i in range(len(b)):
  if PC1[i] > 0 and PC2[i] >= 0:
    if PC1[i] > PC2[i]:
      OMI_phase = 3
    else:
      OMI_phase = 4 # PC2.ge.PC1
     
  if PC1[i] <= 0 and PC2[i] > 0:
    if PC2[i] > abs(PC1[i]):
      OMI_phase = 5
    else:
      OMI_phase = 6 # abs(PC1).ge.PC2

  if PC1[i] < 0 and PC2[i] <= 0:
    if abs(PC1[i]) > abs(PC2[i]):
      OMI_phase = 7
    else:
      OMI_phase = 8 # abs(PC2).ge.abs(PC1)

  if PC1[i] >= 0 and PC2[i] < 0:
    if abs(PC2[i]) > PC1[i]:
      OMI_phase = 1
    else:
      OMI_phase = 2 # PC1.ge.abs(PC2)

  OMI_phases.append(OMI_phase)
  
OMI_phases = np.array(OMI_phases)

#Merge all data into one dataframe
span = np.array(list(range(14120)))
OMI = np.column_stack(((span,b,OMI_phases)))
bb = pandas.DataFrame(OMI)
bb = bb.rename(columns={0:"Index", 1:"Year", 2:"Month", 3:"Day", 4:"OMI1", 5:"OMI2", 6:"Amplitude", 7:"Phase"})

#Retain only data that has amplitude greater than 1
n = 1
bb = bb[bb["Amplitude"] >= n]

#Group data that is in consecutive days by finding consecutive numbers in "Index"
eventsOMI = []
for k,g in bb.groupby(bb["Index"] - np.arange(bb.shape[0])):
    eventsOMI.append(g)

#Collect phase information from all events       
OMIphases = list(map(itemgetter("Phase"), eventsOMI))

#Collect only terminating phase numbers for every event
TerminationOMI = []
for i in range(len(OMIphases)):
    OMIvalue = OMIphases[i].iloc[-1]
    TerminationOMI.append(OMIvalue)
    
#Frequency of terminating phases   
OMIcounter = list(collections.Counter(TerminationOMI).items())

OMIcount = pandas.DataFrame(OMIcounter)
OMIcount = OMIcount.rename(columns={0:"Phase", 1:"Frequency"})
OMIcount = OMIcount.sort_values(by=["Phase"])
df = OMIcount

df.to_csv("OMIcount.csv", encoding='utf-8', index=False)
    
#Plot hustogram of frequency of terminating phases
x = TerminationOMI
num_bins = 8
n, bins, patches = plt.hist(x, num_bins, facecolor='blue', alpha=1, edgecolor='black', linewidth=1.2)
plt.title("OMI Terminating Phases")
plt.xlabel("Phases")
plt.ylabel("Frequency")
plt.savefig("OMI.png")
