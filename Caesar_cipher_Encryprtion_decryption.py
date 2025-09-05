#Encryption
def encrypt_text(plaintext,n):
  ans = " "
  for i in range(len(plaintext)):
    ch = plaintext[i]

    if ch == " ":
      ans += " "

    elif (ch.isupper()):
      ans += chr((ord(ch) + n - 65) % 26 + 65)

    else:
      ans += chr((ord(ch) + n - 97) % 26 + 97)

  return ans

#Decryption
def decrypt_text(ciphertext, n):
    ans = ""
    for i in range(len(ciphertext)):
        ch = ciphertext[i]
        if ch == " ":
            ans += " "
        elif ch.isupper():
            ans += chr((ord(ch) - 65 - n) % 26 + 65)
        else:
            ans += chr((ord(ch) - 97 - n) % 26 + 97)
    return ans

plaintext = input("Enter the plaintext: ")
n = int(input("Enter the shift amount: "))

ciphertext = encrypt_text(plaintext, n)
print("Plain Text is : " + plaintext)
print("Shift pattern is : " + str(n))
print("Cipher Text is : " + ciphertext)

# Decrypt the ciphertext
decrypted_text = decrypt_text(ciphertext, n)
print("Decrypted Text is : " + decrypted_text)
