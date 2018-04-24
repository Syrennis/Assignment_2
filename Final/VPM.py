# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 20:35:01 2018

@author: b934c867
"""

import numpy as np
import pandas

#Read in data for psi values
a = pandas.read_csv('VPM_indices.csv', header = 0)
a_matrix = np.array(a)
PC1 = a["VPM1"]
PC2 = a["VPM2"]
VPM_phase = []
VPM_phases = []

for i in range(13761):
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

VPM = np.column_stack((a,VPM_Phases))

print(VPM_Phases)
