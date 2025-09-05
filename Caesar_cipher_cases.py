#Caesar Cipher for Upper and Lower Cases
def caesar_cipher_encrypt(plaintext, shift):
    encrypted_message = []

    for char in plaintext:
        if char.isalpha():  
            if char.islower():
                start = ord('a')
                encrypted_char = chr(start + (ord(char) - start + shift) % 26)
            elif char.isupper():
                start = ord('A')
                encrypted_char = chr(start + (ord(char) - start + shift) % 26)
            encrypted_message.append(encrypted_char)
        else:
            encrypted_message.append(char)

    return ''.join(encrypted_message)

plaintext = "MEET me at the PARK"
shift_value = 4

print("Plaintext Massage :", plaintext)

encrypted_message = caesar_cipher_encrypt(plaintext, shift_value)
print("Encrypted Message:", encrypted_message)
