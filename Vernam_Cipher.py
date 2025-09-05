def vernam_cipher(message, key):
    
    if len(message) != len(key):
        raise ValueError("Message and key must be of the same length")

  
    result = []
    for m_char, k_char in zip(message, key):
        encrypted_char = chr((ord(m_char) ^ ord(k_char)) % 256)  # Using % 256 to wrap around if needed
        result.append(encrypted_char)
    
    return ''.join(result)

message = "ONETIMEPAD"
key = "XFJRDOVHSG"

encrypted_message = vernam_cipher(message, key)
print("Encrypted Message:" ,encrypted_message)

decrypted_message = vernam_cipher(encrypted_message, key)
print("Decrypted Message:" ,decrypted_message)
