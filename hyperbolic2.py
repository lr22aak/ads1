# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 11:17:45 2022

@author: lr22aak
"""
# import 
# from numpy import sin, cos, linspace
import numpy as np
import matplotlib.pyplot as plt

plt.figure()

plt.xlabel('fx')
plt.ylabel('fy')

pi_arr = np.linspace(0, 2*np.pi, 5000)


def trigon1(a, b, j):
    x = np.cos(a*pi_arr) - np.cos(b*pi_arr)**j
    return x

def trigon2(c, d, k):
    y = np.sin(c*pi_arr) - np.sin(d*pi_arr)**k
    return y


plt.plot(trigon1(1, 60, 1), trigon2(1, 120, 1), "b:")

# plt.legend()

plt.show()