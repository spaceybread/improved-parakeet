def abs(x):
    if x < 0: return -1 * x
    return x

def g(x, n):
    return (x * x - 1) % n

def gcd(x, y):
    while(y): x, y = y, x % y
    return abs(x)

N = 9

x, y, d = 2, 2, 1

while d == 1:
    x = g(x, N)
    y = g(g(y, N), N)
    d = gcd(abs(x - y), N)


if d == N: print("fail")
else: print(d)
