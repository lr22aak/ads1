# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 11:17:45 2022

@author: lr22aak
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 5)

y = np.sinh(x)

plt.figure()

plt.plot(x,y)