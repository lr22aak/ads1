# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 11:17:45 2022

@author: lr22aak
"""

import numpy as np
import matplotlib.pyplot as plt




x = np.linspace(-5, 5, 1000)

y1 = np.sinh(x)
y2 = np.cosh(x)

plt.figure()

plt.xlabel('fx')
plt.ylabel('fy')

plt.plot(x, y1, label="sinh(x)")
plt.plot(x, y2, label="cosh(x)")

plt.xlim(-5, 5)

plt.legend()

plt.show()