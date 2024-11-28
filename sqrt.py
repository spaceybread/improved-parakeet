import sys

def is_square(n, p):
    if n % p == 0: return True
    return pow(n, (p - 1) // 2, p) == 1

def search_2(n, p, k = 2):
    lo, hi = 0, (p**k // 2) + 1
    
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid**2 == n:
            print("Found:", mid, (-1 * mid) % p)
            return True
        
        if mid**2 > n: hi = mid - 1
        else: lo = mid + 1

def lifting(a, p, k = 2):
    out = [a]
    iter = [a]
    pump = 0
    while pump < (p*p // 4) + 1:
        iter.append(out[-1] + p)
        out.append(iter[-1] % (p*p))
        pump += p
    
    print(len(out))
    quit()
    return out

def clean_lift(p, n):
    out = [n]
    iter = [n]
    pump = 0
    sq = p*p
    while pump < (sq // 2) + 1:
        print(pump/sq)
        if search_2(out[-1], p): quit()
        iter.append(out[-1] + p)
        out.append(iter[-1] % (sq))
        pump += p
        
        

try:
    p = int(sys.argv[1])
    n = int(sys.argv[2])
except:
    print("Usage: python3 sqrt.py <p> <n>")
    quit()

#lifts = lifting(n, p)
if is_square(n, p): clean_lift(p, n)
else: print("Not a square!")

#for lift in lifts:
#    print("Lift:", lift)
#    if search_2(lift, p): quit()

print("Not found!")
    
