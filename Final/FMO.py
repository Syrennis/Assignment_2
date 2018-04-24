#The quadrant definitions are analagous to the original WH04
#EOF structures, with OMI +EOF2=Active over MC (4/5) and OMI EOF1
#=Active over IO (2/3). Here, the "warm pool" in the model
#is treated as the WP (6/7). Thus, active convection over
#the center of the domain (20,000 km) should correspond to +EOF2.

import numpy as np
import pandas

#Read in data for psi values
c = pandas.read_csv('FMO_indices.csv', header = 0)
PC1 = c["FMO1"]
PC2 = c["FMO2"]
FMO_phase = []
FMO_phases = []

for i in range(12454):
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
