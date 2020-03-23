import numpy as np
import math as m

def coswin(a,n):
    t = np.linspace(0,1,n)
    # Section 1
    i = 0
    res = []
    while t[i] >= 0.0 and t[i] <= a:
        c1 = (1-m.cos(m.pi/a*t[i]))/2
        res.append(c1)
        i = i + 1

    # Section 2
    j = 0
    while t[j] <= a:
        j = j + 1
        while t[j] >= a and t[j] <= (1-a):
            c2 = 1.0
            res.append(c2)
            j = j + 1

    # Section 3
    k = 0
    while t[k] <= (1-a):
        k = k + 1
    kk = k+1
    while kk <= n:
        c3 = (1-m.cos(m.pi/a*(1-t[kk-1])))/2
        res.append(c3)
        kk = kk + 1
    return res
