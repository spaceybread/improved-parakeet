import math

X = 15
Y = 3

def sieve(srt, n):
    prime = [True for i in range(n + 1)]
    prime[0] = False
    prime[1] = False

    for p in range(2, int(math.sqrt(n))+1):
        if prime[p] == True:
            for i in range(p*p, n+1, p):
                prime[i] = False
    out = []
    for p in range(srt, n+1):
        if prime[p]:
            out.append(p)
    
    return out


def psi(x, y, plist):
    x, y = math.floor(x), math.floor(y)
    if x < 1 and y < 1: return 0
    if x >= 1 and y == 1: return 1
    if x >= 1 and y == 2: return math.floor(math.log(x, 2)) + 1
    if y >= x: return x
    
    
    a = 1
    
    for p in plist:
        a += psi(x / p, p, plist)
    
    return a

pl = sieve(2, Y)

out = psi(X, Y, pl)
print(out)
