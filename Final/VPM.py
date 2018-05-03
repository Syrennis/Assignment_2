# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 20:35:01 2018

@author: b934c867
"""
#Import needed functions and packages
import matplotlib.pyplot as plt
import numpy as np
import pandas
from itertools import groupby, count
from operator import itemgetter
import collections
import tables
import csv

#Read in data for VPM indices
a = pandas.read_csv('VPM_indices.csv', header = 0)
a_matrix = np.array(a)
PC1 = a["VPM1"]
PC2 = a["VPM2"]
VPM_phase = []
VPM_phases = []

#For loop to assign phases based off 2 leading EOFs
for i in range(len(a_matrix)):
  if PC1[i] > 0 and PC2[i] >= 0:
    if PC1[i] > PC2[i]:
      VPM_phase = 8
    else:
      VPM_phase = 7 # PC2.ge.PC1
     
  if PC1[i] <= 0 and PC2[i] > 0:
    if PC2[i] > abs(PC1[i]):
      VPM_phase = 6
    else:
      VPM_phase = 5 # abs(PC1).ge.PC2

  if PC1[i] < 0 and PC2[i] <= 0:
    if abs(PC1[i]) > abs(PC2[i]):
      VPM_phase = 4
    else:
      VPM_phase = 3 # abs(PC2).ge.abs(PC1)

  if PC1[i] >= 0 and PC2[i] < 0:
    if abs(PC2[i]) > PC1[i]:
      VPM_phase = 2
    else:
      VPM_phase = 1 # PC1.ge.abs(PC2)

  VPM_phases.append(VPM_phase)
  
VPM_Phases = np.array(VPM_phases)

#Merge all data into one dataframe
span = np.array(list(range(13761)))
VPM = np.column_stack(((span,a,VPM_Phases)))
aa = pandas.DataFrame(VPM)
aa = aa.rename(columns={0:"Index", 1:"Year", 2:"Month", 3:"Day", 4:"VPM1", 5:"VPM2", 6:"Amplitude", 7:"Phase"})

#Retain only data that has amplitude greater than 1
n = 1
aa = aa[aa["Amplitude"] >= n]

#Group data that is in consecutive days by finding consecutive numbers in "Index"
eventsVPM = []
for k,g in aa.groupby(aa["Index"] - np.arange(aa.shape[0])):
    eventsVPM.append(g)

#Collect phase information from all events 
VPMphases = list(map(itemgetter("Phase"), eventsVPM))

#Collect only terminating phase numbers for every event
TerminationVPM = []
for i in range(len(VPMphases)):
    VPMvalue = VPMphases[i].iloc[-1]
    TerminationVPM.append(VPMvalue)
    
#Frequency of terminating phases   
VPMcounter = list(collections.Counter(TerminationVPM).items())

VPMcount = pandas.DataFrame(VPMcounter)
VPMcount = VPMcount.rename(columns={0:"Phase", 1:"Frequency"})
VPMcount = VPMcount.sort_values(by=["Phase"])
df = VPMcount

df.to_csv("VPMcount.csv", encoding='utf-8', index=False)

#Plot hustogram of frequency of terminating phases
y = np.array(TerminationVPM)
x = TerminationVPM
num_bins = 8
plt.hist(x, num_bins, facecolor='blue', alpha=1., edgecolor='black', linewidth=1.2)
plt.title("VPM Terminating Phases")
plt.xlabel("Phases")
plt.ylabel("Frequency")
plt.savefig("VPM.png")