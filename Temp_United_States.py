# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 23:39:06 2018

@author: b934c867
"""

import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import pandas

df = pandas.read_csv('./Temperatures.csv')
df = df[df.columns.difference(['Unnamed: 0'])]
df = df.transpose()
lon = df[1].apply(float)
lat = df[0].apply(float)
temp = df[2]
df[2] = df[2].apply(str).str.replace('\(|\)','')
temp = temp.tolist()
# 1. Draw the map background
pdat = temp


buff = 0.5 #Edge buffer (degrees)
xmn = lon.min() - buff # Create left boundary
xmx = lon.max() + buff # Create right boundary
ymn = lat.min() - buff # Create bottom boundary
ymx = lat.max() + buff # Create top boundary

w = 8.5 #width of figure [inches]
h = 11 #height of figure [inches]
pw = 0.8 # Width of plot as fraction
yfac = w/h #y-scale factor
sfac = (ymx-ymn)/(xmx-xmn) #size scale factor
cmap = plt.cm.jet
fig = plt.figure(figsize=(w,h)) #Create Figure
ax = plt.axes([0.1,0.15,pw,pw*yfac*sfac],facecolor='White',frameon=True) # Create Axes
#m = Basemap(projection='cyl',llcrnrlat=24,urcrnrlat=50,llcrnrlon=-125,urcrnrlon=-67,resolution='c') # Contiguous United States
#m = Basemap(projection='cyl',llcrnrlat=51,urcrnrlat=72,llcrnrlon=-170,urcrnrlon=-128,resolution='c') # Alaska
#m = Basemap(projection='cyl',llcrnrlat=18.5,urcrnrlat=22.5,llcrnrlon=-161,urcrnrlon=-154,resolution='c')  # Hawaii
#m = Basemap(projection='cyl',llcrnrlat=30.5,urcrnrlat=50,llcrnrlon=-125,urcrnrlon=-102,resolution='c') # West US
#m = Basemap(projection='cyl',llcrnrlat=35.5,urcrnrlat=50,llcrnrlon=-105,urcrnrlon=-80,resolution='c') # Midwest US
#m = Basemap(projection='cyl',llcrnrlat=24,urcrnrlat=38,llcrnrlon=-107,urcrnrlon=-74,resolution='c') # South US
#m = Basemap(projection='cyl',llcrnrlat=36,urcrnrlat=50,llcrnrlon=-83,urcrnrlon=-67,resolution='c') # Northeast US
m.drawcoastlines() # draw coastlines
m.drawstates() # draw states
m.drawcountries()
m.drawcounties()

sc = plt.scatter(lon, lat, c=pdat, s=3, cmap=cmap) #Plot points, can add vmin=0, vmax=500 to set the limits
plt.title('Yearly Temperature Change (1950-2008)') # Add Title to the plot

cax = fig.add_axes([0.1,0.1,0.8,0.015]) #Create Axes for Colorbar
bar = fig.colorbar(sc,orientation='horizontal',cax=cax) #Create Color bar
bar.set_label('Yearly Temperature Change (deg. F)') # Add Label to Colorbar

plt.savefig('Northeast.pdf',format='pdf',bbox_inches='tight')   # Save the figure

plt.show() #Show Figure