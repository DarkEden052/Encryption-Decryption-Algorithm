#Affine Cipher 
import math

def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError("Modular inverse does not exist")
#Encryption 
def affine_encrypt(plaintext, a, b):
    m = 26
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            x = ord(char) - shift
            encrypted = (a * x + b) % m
            encrypted_char = chr(encrypted + shift)
            ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext
#Decryption
def affine_decrypt(ciphertext, a, b):
    m = 26
    a_inv = mod_inverse(a, m)
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            y = ord(char) - shift
            decrypted = (a_inv * (y - b)) % m
            decrypted_char = chr(decrypted + shift)
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    a = 5
    b = 8

    if gcd(a, 26) != 1:
        raise ValueError("Key 'a' must be coprime with 26")

    plaintext = "Anubhav Singh"
    ciphertext = affine_encrypt(plaintext, a, b)
    decrypted_text = affine_decrypt(ciphertext, a, b)

    print("Plaintext:", plaintext)
    print("Ciphertext:", ciphertext)
    print("Decrypted Text:", decrypted_text)
