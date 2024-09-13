import math

arr = []

def solve(n):
    if n == 0:
        return
    
    if n == 1:
        arr.append((0, 0))
    
    if n % 2 == 0:
        solve(n // 2)
        
        for i in range(len(arr)):
            arr[i] = (arr[i][0] + 1, arr[i][1])
            
        
    else:
        m = int(math.floor(math.log(n, 3)))
        arr.append((0, m))
        
        solve(n - 3**m)

solve(7)

print(arr)
