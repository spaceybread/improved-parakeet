import sys
import random
from collections import Counter

def search(n, p, arr, X = 0, L = 10):
    if X == L:
        print(*arr)
        print(len(arr) / L)
        x = Counter(arr)
        # print(x[0]/len(arr))
        quit()
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
    
    if s_1 > s_2:
        arr += L_e
        search(pow(2, s_1, p), p, arr, X + 1, L)
    else:
        arr += L_o
        search(pow(2, s_2, p), p, arr, X + 1, L)
        

p = 7382748937 # just some prime I looked up
try:
    n = int(sys.argv[1])
    L = int(sys.argv[2])
except:
    print("Usage: python3 prg.py <seed> <iterations>")
    quit()
# n = random.randint(1, p)
full = []
print("Using seed:", n)
search(n, p, full, 0, L)
