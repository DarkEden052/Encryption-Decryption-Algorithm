# Hill Cipher 
import numpy as np

# Key matrix 
key_matrix = np.array([[17, 17, 5],
                       [21, 18, 21],
                       [2, 2, 19]])

# Function to convert a character to a number (A = 0, B = 1, ..., Z = 25)
def char_to_num(c):
    return ord(c) - ord('a')

# Function to convert a number to a character (0 = A, 1 = B, ..., 25 = Z)
def num_to_char(n):
    return chr(n + ord('a'))

# Function to encrypt a block of 3 characters
def encrypt_block(block, key_matrix):
    block_vector = np.array([char_to_num(c) for c in block])
    encrypted_vector = np.dot(key_matrix, block_vector) % 26
    return ''.join(num_to_char(num) for num in encrypted_vector)

# Function to decrypt a block of 3 characters
def decrypt_block(block, inv_key_matrix):
    block_vector = np.array([char_to_num(c) for c in block])
    decrypted_vector = np.dot(inv_key_matrix, block_vector) % 26
    return ''.join(num_to_char(num) for num in decrypted_vector)

# Function to find modular inverse of matrix
def mod_inverse_matrix(matrix, mod):
    det = int(np.round(np.linalg.det(matrix)))  
    det_inv = pow(det, -1, mod) 
    matrix_mod_inv = det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % mod
    return matrix_mod_inv

# Function to encrypt the plaintext using Hill cipher
def hill_encrypt(plaintext, key_matrix):
    if len(plaintext) % 3 != 0:
        plaintext += 'x' * (3 - len(plaintext) % 3)
    
    ciphertext = ''
    for i in range(0, len(plaintext), 3):
        block = plaintext[i:i+3]
        ciphertext += encrypt_block(block, key_matrix)
    return ciphertext

# Function to decrypt the ciphertext using Hill cipher
def hill_decrypt(ciphertext, key_matrix):
    inv_key_matrix = mod_inverse_matrix(key_matrix, 26)
    plaintext = ''
    for i in range(0, len(ciphertext), 3):
        block = ciphertext[i:i+3]
        plaintext += decrypt_block(block, inv_key_matrix)
    return plaintext

# Example 
plaintext = "paymoremoney"
ciphertext = hill_encrypt(plaintext, key_matrix)
print("Original PlainText: ", plaintext)
print("\n")

print("After Encryption : ")
print("Ciphertext:", ciphertext)
decrypted_text = hill_decrypt(ciphertext, key_matrix)
print("Decrypted Text:", decrypted_text)
