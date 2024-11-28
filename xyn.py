import time as t
import math

n = 293**2
sq_n = (n ** 0.5)
print(sq_n)
ly = []
lx = []

for x in range(1, math.floor(sq_n) // 2 + 1 + 1):
    lx.append((x, math.sqrt(n - x**2)))

for x in range(math.floor(sq_n), math.ceil(sq_n) // 2 + 1, -1):
    ly.append((x, math.sqrt(n - x**2)))


#print(*lx)
#print(*ly[::-1])
    
for p in lx:
    for q in ly:
        if p == q[::-1]:
            print(p, q)
        
    
