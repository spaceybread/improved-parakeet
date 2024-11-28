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
# N = 1238926361552897 * 93461639715357977769163558199606896584051237541638188580280321

N = 93461639715357977769163558199606896584051237541638188580280321

# Init
x, y, d = 2, 2, 1

while d == 1:
    x = g(x, N)
    y = g(g(y, N), N)
    d = gcd(abs(x - y), N)


if d == N: print("fail")
else: print(d)
