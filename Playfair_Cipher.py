# This function converts the input text to lowercase
def toLowerCase(text):
  return text.lower()

# This fumction removes all spaces from a string.
def removeSpaces(text):
  newText = ""
  for i in text:
    if i == " ":
      continue
    else:
      newText = newText + i
  return newText

# This fucntion groups the text into digraphs (pairs of two characters).

def Diagraph(text):
    Diagraph = []
    i = 0
    while i < len(text):
        if i + 1 < len(text):
            Diagraph.append(text[i:i+2])
            i += 2
        else:
            Diagraph.append(text[i] + 'x')  # Append 'x' if single character left
            i += 1
    return Diagraph

# This function inserts a filler letter ('x') between two identical letters in the text.

def FillerLetter(text):
    new_word = ""
    i = 0
    while i < len(text):
        new_word += text[i]
        if i + 1 < len(text) and text[i] == text[i + 1]:
            new_word += 'x'  # Insert 'x' if two identical letters are found
        i += 1
    return new_word

list1 = ['a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q',
         'r','s','t','u','v','w','x','y','z']

# This function generates a 5x5 key square matrix for the PlayFair cipher.

def generateKeymatrix(word, list1):
  key_letters = []
  for i in word:
    if i not in key_letters:
      key_letters.append(i)

  compElements = []
  for i in key_letters:
    if i not in compElements:
      compElements.append(i)
  for i in list1:
    if i not in compElements:
      compElements.append(i)

  matrix = []
  while compElements != []:
    matrix.append(compElements[:5])
    compElements = compElements[5:]

  return matrix

# This function finds the position (row and column) of an element in the matrix.

def search(mat, element):
  for i in range(5):
    for j in range(5):
      if(mat[i][j] == element):
        return i, j

# This fucntion encrypts a digraph according to the row rule of the PlayFair cipher.
def encrypt_RowRule(matr, e1r, e1c, e2r, e2c):
  char1 = ''
  if e1c == 4:
    char1 = matr[e1r][0]
  else:
    char1 = matr[e1r][e1c+1]

  char2 = ''
  if e2c == 4:
    char2 = matr[e2r][0]
  else:
    char2 = matr[e2r][e2c+1]

  return char1, char2

# This function encrypts a digraph according to the column rule of the Playfair cipher.

def encrypt_ColumnRule(matr, e1r, e1c, e2r, e2c):
  char1 = ''
  if e1r == 4:
    char1 = matr[0][e1c]
  else:
    char1 = matr[e1r+1][e1c]

  char2 = ''
  if e2r == 4:
    char2 = matr[0][e2c]
  else:
    char2 = matr[e2r+1][e2c]

  return char1, char2

# This function encrypts a digraph according to the rectangle rule of the Playfair cipher.

def encrypt_RectangleRule(matr, e1r, e1c, e2r, e2c):
  char1 = ''
  char1 = matr[e1r][e2c]

  char2 = ''
  char2 = matr[e2r][e1c]

  return char1, char2

# This function ecrypts a list of digraphs using the Playfair cipher.

def encryptByPlayfairCipher(Matrix, plainList):
  CipherText = []
  for i in range(0, len(plainList)):
    c1 = 0
    c2 = 0
    ele1_x, ele1_y = search(Matrix, plainList[i][0])
    ele2_x, ele2_y = search(Matrix, plainList[i][1])

    if ele1_x == ele2_x:
      c1, c2 = encrypt_RowRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
      # Get 2 letter cipherText
    elif ele1_y == ele2_y:
      c1, c2 = encrypt_ColumnRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
    else:
      c1, c2 = encrypt_RectangleRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)

    cipher = c1 + c2
    CipherText.append(cipher)
  return CipherText

# Decryption functions.
def decrypt_RowRule(matr, e1r, e1c, e2r, e2c):
    char1 = matr[e1r][(e1c - 1) % 5]
    char2 = matr[e2r][(e2c - 1) % 5]
    return char1, char2

def decrypt_ColumnRule(matr, e1r, e1c, e2r, e2c):
    char1 = matr[(e1r - 1) % 5][e1c]
    char2 = matr[(e2r - 1) % 5][e2c]
    return char1, char2

def decrypt_RectangleRule(matr, e1r, e1c, e2r, e2c):
    char1 = matr[e1r][e2c]
    char2 = matr[e2r][e1c]
    return char1, char2

def decryptByPlayfairCipher(Matrix, cipherList):
    PlainText = []
    for digraph in cipherList:
        ele1_x, ele1_y = search(Matrix, digraph[0])
        ele2_x, ele2_y = search(Matrix, digraph[1])
        if ele1_x == ele2_x:
            p1, p2 = decrypt_RowRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        elif ele1_y == ele2_y:
            p1, p2 = decrypt_ColumnRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        else:
            p1, p2 = decrypt_RectangleRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        PlainText.append(p1 + p2)
    return PlainText


text_Plain = 'HELLO My Name is Anubhav Singh'
text_Plain = removeSpaces(toLowerCase(text_Plain))
PlainTextList = Diagraph(FillerLetter(text_Plain))
if len(PlainTextList[-1]) != 2:
  PlainTextList[-1] = PlainTextList[-1]+'z'

key = "Security"
print("Key Text: ", key)
key = toLowerCase(key)
Matrix = generateKeymatrix(key, list1)

print("Plain Text: ", text_Plain)
CipherList = encryptByPlayfairCipher(Matrix, PlainTextList)

CipherText = ""
for i in CipherList:
  CipherText += i
print("CipherText: ", CipherText)

# Decrypting the cipher text
DecryptedPlainList = decryptByPlayfairCipher(Matrix, CipherList)
DecryptedText = "".join(DecryptedPlainList)
DecryptedText = DecryptedText.replace('x', '')
print("Decrypted Text: ", DecryptedText)
