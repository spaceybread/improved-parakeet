def size10(n):
    return len(str(n)) - 1

def kar(n1, n2):
    if (n1 < 10 or n2 < 10): return n1 * n2
    
    m = max(size10(n1), size10(n2)) // 2
    
