import sys
import random
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

def search(n, p, arr, X = 0, L = 10):
    if X == L:
        print(*arr)
        print(len(arr) / L)
        x = Counter(arr)
        print(x[0]/len(arr))
        return x[0]/len(arr)
    lo, hi = 0, p
    
    out = []
    
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid == n: break
        if mid > n:
            hi = mid - 1
            out.append(0)
        else:
            lo = mid + 1
            out.append(1)

    s_1 = 0
    s_2 = 0
    fir = True
    L_o = []
    L_e = []
    for i in range(len(out)):
        if fir:
            s_1 = s_1*2 + out[i]
            L_e.append(out[i])
            fir = False
        else:
            s_2 = s_2*2 + out[i]
            L_o.append(out[i])
            fir = True
    
    if out[-1] == 1: arr += L_e
    else: arr += L_o
    alpha = 0.5
    # s = int(min(s_1, s_2) * alpha + max(s_1, s_2) * (1 - alpha))
    s = s_1 * s_2
    return search(pow(2, s, p), p, arr, X + 1, L)
         

p = 7382748937 # just some prime I looked up
try:
    n = int(sys.argv[1])
    L = int(sys.argv[2])
except:
    print("Usage: python3 prg.py <seed> <iterations>")
    quit()

N = 10000
vals = []
for x in range(N):
    n = random.randint(1, p)
    full = []
    print("Using seed:", n)
    vals.append(search(n, p, full, 0, L))

vals.sort()
S = sum(vals)
print("Average:", S/N)
print("Median:", vals[len(vals) >> 1])
print("Min diff:", abs(0.5 - S/N))
print("Min:", min(vals), " Max:", max(vals))
print("SD:", np.std(vals))

coun = []

for x in vals:
    coun.append(int(x * 10000))
tab = Counter(coun)

lists = sorted(tab.items())
x, y = zip(*lists)
plt.plot(x, y)
plt.show()
