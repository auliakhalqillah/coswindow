import math as m
import numpy as np
import matplotlib.pyplot as plt
from coswindow import coswin

print("---------------")
print("INPUT PARAMETER")
print("---------------")
a = float(input("Taper Ratio \t\t:"))
dt = float(input("Sampling Time \t\t:"))
f = float(input("Signal Frequancey \t:"))
if a == dt:
    print("Sampling rate have to smaller than Taper ratio!")
t = np.arange(0,1,dt)
n = len(t)

# Generate signal
l = 0
signal = []
while l < n:
    x = m.sin(2*m.pi*f*t[l])
    signal.append(x)
    l = l + 1

# using coswindow
res = coswin(a,n)

# Add cosine tapper to signal
p = 0
up = []
while p < n:
    xx = signal[p]*res[p]
    up.append(xx)
    p = p + 1

# Plot
fig = plt.figure()
fig1 = fig.add_subplot(311)
plt.plot(t,signal,color='black',label='signal')
plt.ylabel('Magnitude')
plt.legend(loc='upper left')

fig2 = fig.add_subplot(312)
plt.plot(t,res,color='red',label='cosine taper')
plt.ylabel('Magnitude')
plt.legend(loc='upper left')

fig3 = fig.add_subplot(313)
plt.plot(t,up,color='blue',label='windowed')
plt.xlabel("Time (s)")
plt.ylabel('Magnitude')
plt.legend(loc='upper left')
plt.show()
