# Caesar Cipher
def caesar_cipher_encrypt(plaintext, shift):
    encrypted_message = []

    for char in plaintext:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                start = ord('a')
                encrypted_char = chr(start + (ord(char) - start + shift_amount) % 26)
            elif char.isupper():
                start = ord('A')
                encrypted_char = chr(start + (ord(char) - start + shift_amount) % 26)
            encrypted_message.append(encrypted_char)
        else:
            encrypted_message.append(char)

    return ''.join(encrypted_message)

# Define the plaintext and shift
plaintext = "MEET me at the PARK"
shift_value = 4
print("Plaintext Massage :",plaintext)
# Encrypt the message
encrypted_message = caesar_cipher_encrypt(plaintext, shift_value)
print("Encrypted Message:", encrypted_message)
