# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 19:42:16 2018

@author: b934c867
"""
#Import needed functions and packages
import numpy as np
import pandas
from itertools import groupby
from operator import itemgetter
import matplotlib.pyplot as plt
import collections

#Read in data for RMM indices
d = pandas.read_csv('RMM_indices.csv', header = 0)

#Merge all data into one dataframe
span = np.array(list(range(16034)))
d = np.column_stack((span,d))
d = pandas.DataFrame(d)
d = d.rename(columns={0:"Index", 1:"Year", 2:"Month", 3:"Day", 4:"RMM1", 5:"RMM2", 6:"Phase", 7:"Amplitude"})

#Retain only data that has amplitude greater than 1
n = 1
d = d[d["Amplitude"] >= n]

#Group data that is in consecutive days by finding consecutive numbers in "Index"
eventsRMM = []
for k,g in d.groupby(d["Index"] - np.arange(d.shape[0])):
    eventsRMM.append(g)

#Collect phase information from all events 
RMMphases = list(map(itemgetter("Phase"), eventsRMM))

#Collect only terminating phase numbers for every event
TerminationRMM = []
for i in range(len(RMMphases)):
    RMMvalue = RMMphases[i].iloc[-1]
    TerminationRMM.append(RMMvalue)

#Frequency of terminating phases       
RMMcounter = list(collections.Counter(TerminationRMM).items())

RMMcount = pandas.DataFrame(RMMcounter)
RMMcount = RMMcount.rename(columns={0:"Phase", 1:"Frequency"})
RMMcount = RMMcount.sort_values(by=["Phase"])

#Plot hustogram of frequency of terminating phases
x = TerminationRMM
num_bins = 8
n, bins, patches = plt.hist(x, num_bins, facecolor='blue', alpha=1, edgecolor='black', linewidth=1.2)
plt.title("RMM Terminating Phases")
plt.xlabel("Phases")
plt.ylabel("Frequency")
plt.savefig("RMM.png")