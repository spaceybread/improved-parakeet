a = [3, 1, 4, 5, 2, 6, 2]
n = len(a)
best = [1] * n

for i in range(1, n):
    for p in range(0, i):
        if a[i] > a[p]: best[i] = max(best[i], best[p] + 1)

print(max(best))
