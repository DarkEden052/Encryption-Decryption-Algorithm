def generate_vigenere_key(text, key):
    key = list(key)
    if len(text) == len(key):
        return key
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)
#Encryption
def vigenere_encrypt(text, key):
    encrypted_text = []
    for i in range(len(text)):
        x = (ord(text[i]) + ord(key[i])) % 26
        x += ord('A')
        encrypted_text.append(chr(x))
    return "".join(encrypted_text)
#Decryption
def vigenere_decrypt(encrypted_text, key):
    decrypted_text = []
    for i in range(len(encrypted_text)):
        x = (ord(encrypted_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        decrypted_text.append(chr(x))
    return "".join(decrypted_text)

# Example usage
text = "HELLOWORLD"
key = "KEY"
key = generate_vigenere_key(text, key)

print("Text :",text)

encrypted_text = vigenere_encrypt(text, key)
print(f"Encrypted Text: {encrypted_text}")

decrypted_text = vigenere_decrypt(encrypted_text, key)
print(f"Decrypted Text: {decrypted_text}")
