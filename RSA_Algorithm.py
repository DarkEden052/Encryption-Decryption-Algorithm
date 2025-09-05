def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

p = 3
q = 11
e = 7
M = 2  

n = p * q
phi = (p - 1) * (q - 1)

if gcd(e, phi) != 1:
    raise ValueError("e and phi(n) are not coprime!")

d = mod_inverse(e, phi)
if d is None:
    raise ValueError("Modular inverse of e does not exist!")

C = pow(M, e, n)
print(f"Ciphertext (C): {C}")

decrypted_M = pow(C, d, n)
print(f"Decrypted Plaintext (M): {decrypted_M}")
