import numpy as np
import scipy.signal as signal
import scipy as sp
import pylab as pl
#import matplotlib.pyplot as plt

n = np.arange(-200,200+1)
h = (1/(n*np.pi)) * (np.sin(45/500*2*np.pi*n) - np.sin(55/500*2*np.pi*n))

h[200] = 1-(55/500*2*np.pi - 45/500*2*np.pi)/np.pi
pl.plot(h)
pl.show()

y2 = signal.lfilter(h,1,y)