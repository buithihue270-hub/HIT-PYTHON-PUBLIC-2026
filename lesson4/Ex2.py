def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def gcd_v2(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a