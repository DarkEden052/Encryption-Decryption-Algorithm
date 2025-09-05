def euclidean_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Example usage for the given pairs:
a1, b1 = 252, 105
a2, b2 = 401, 700

gcd1 = euclidean_gcd(a1, b1)
gcd2 = euclidean_gcd(a2, b2)

print(f"The GCD of {a1} and {b1} is: {gcd1}")
print(f"The GCD of {a2} and {b2} is: {gcd2}")
