import time

def makeTable(n):
    start = [3, 5, 7]
    for i in range(1, n): start += [start[-2] + 6, start[-1] + 6]
    return start

def filter(arr):
    ma = arr[-1]
    n = len(arr)

    for i in range(n):
        if arr[i] == 0:
            continue
        if arr[i] * arr[i] > ma:
            break
        for j in range(i + 1, n):
            if arr[j] % arr[i] == 0:
                arr[j] = 0
    
    return arr

def SieveOfEratosthenes(n):

    # Create a boolean array
    # "prime[0..n]" and initialize
    #  all entries it as true.
    # A value in prime[i] will
    # finally be false if i is
    # Not a prime, else true.
    prime = [i for i in range(n+1)]
    p = 2
    while (p * p <= n):

        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] != 0):

            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = 0
        p += 1

    # Print all prime numbers
    return prime

k = 100000

p6 = time.time()
t = makeTable(k)
print(time.time() - p6)
o = filter(t)
p6 = time.time() - p6


soe = time.time()
SieveOfEratosthenes(6 * k + 1)
soe = time.time() - soe

print(p6, soe)
print(soe - p6)
print(p6 - soe)
