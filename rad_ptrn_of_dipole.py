# -*- coding: utf-8 -*-
"""
Created on Thu May  1 09:53:58 2025

@author: Omurcan
"""

import numpy as np 
import matplotlib.pyplot as plt

# we use simple radiation pattern like sin wawe 

theta = np.linspace(0 , 2*np.pi, 360) #form zero to 2pi there are 360 points out there

r = np.abs(np.sin(theta)) #absolute value makes all values non-negative

plt.figure(figsize=(3,3))

ax = plt.subplot(111, polar = True)

ax.plot(theta, r, label="Dipole Antenna")

ax.set_title("Radiation Pattern of Dipole Antenna", va="bottom")

ax.legend(loc="upper right")

plt.show