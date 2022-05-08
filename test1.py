import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
w = np.linspace(-np.pi,np.pi,100)
#plt.plot(w,np.cos(0.5*w))
#plt.show()

x = np.random.normal(0,1,1000)

#plt.plot(x)
#plt.show()

xf = np.fft.fft(x)
#plt.plot(np.abs(xf))
#plt.show()

h = np.array([0.5,0.5])
y = signal.lfilter(h,1,x)
plt.plot(y)
plt.show()