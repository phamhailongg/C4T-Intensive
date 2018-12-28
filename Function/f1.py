# Tinh giai thua
def giaithua(n) : 
    if n == 1 : 
        return 1 
    else : 
        return (n * giaithua(n - 1))

# UCLN 
def UCLN(a, b) : 
    x = abs(a)
    y = abs(b)
    if x == 0 : 
        return y 
    if y == 0 : 
        return x 
    if x == y : 
        return x 
    if x < y : 
        return UCLN(x, y - x)
    return UCLN(y, x - y)
    
