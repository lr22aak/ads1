# doing all the imports HERE
import numpy as np
import matplotlib.pyplot as plt




def trigon1(a, b, j):
    """ Computes the trigonomical polynomial cos(at) - cos(bt)**j with t from 0.0 to 2*pi"""

    t=np.linspace(0.0, 2.0*np.pi, 10000)
    f= np.cos(a*t) -np.cos(b*t)**j

    return t, f
def trigon2(c, d, k):
    """ Computes the trigonomical polynomial cos(ct) - cos(dt)**k with t from 0.0 to 2*pi"""

    t = np.linspace(0.0, 2.0*np.pi, 10000)
    f = np.sin(c*t) - np.sin(d*t)**k

    return t, f

t,x = trigon1(1,60,3)
t,y = trigon2(1,120,4)
plt.figure()
plt.plot(x, y)

plt.xlabel("cos(phi) - cos(60*phi)^3")
plt.xlabel("sin(60*phi) - sin(phi)^4")

plt.show()

