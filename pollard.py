# absolute value function
def abs(x):
    if x < 0: return -1 * x
    return x

# polynomial used for Pollard's Rho Algorithm
def g(x, n):
    return (x * x - 1) % n

# Euclidean GCD
def gcd(x, y):
    while(y): x, y = y, x % y
    return abs(x)

# Number to be factored
N = 547011651065197249

# Init
x, y, d = 2, 2, 1

while d == 1:
    x = g(x, N)
    y = g(g(y, N), N)
    d = gcd(abs(x - y), N)


if d == N: print("fail")
else: print(d)
