def extended_gcd(x, y):
    
    if y == 0:
        return x, 1, 0
    else:
        gcd, a1, b1 = extended_gcd(y, x % y)
        a = b1
        b = a1 - (x // y) * b1
        return gcd, a, b
    
x = 8
y = 12
gcd, a, b = extended_gcd(x, y)
print(f"gcd: {gcd}")
print(f"a: {a}")
print(f"b: {b}")