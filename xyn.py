import time as t
import math

n = 100
sq_n = math.ceil(n ** 0.5)

L = []

for y in range(sq_n):
    can_x = math.sqrt(n - y**2)
    
    if can_x == int(can_x):
        L.append((can_x, y))

print(L)
