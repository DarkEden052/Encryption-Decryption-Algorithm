#Extended Euclidean algorithm to find the multiplicative inverse of an integer a modulo m. 
# a)	a= 7, m = 26
# b)	a=14, m=28

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return (gcd, x, y)

def multiplicative_inverse(a, m):
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError(f"The inverse does not exist because GCD({a}, {m}) != 1.")
    else:
        return x % m

# Example usage
a1, m1 = 7, 26
a2, m2 = 14, 28

inverse1 = multiplicative_inverse(a1, m1)
inverse2 = None
try:
    inverse2 = multiplicative_inverse(a2, m2)
except ValueError as e:
    inverse2 = str(e)

print(f"The multiplicative inverse of {a1} modulo {m1} is: {inverse1}")
print(f"The multiplicative inverse of {a2} modulo {m2} is: {inverse2}")
