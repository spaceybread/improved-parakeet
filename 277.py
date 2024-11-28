x = 11391
y = 5673
r = 3

for i in range(-10000, 100000):
    a = (r - (x * i)) / y
    
    if int(a) == a:
        print(a, i)


print(x * -126 + y * 253)
