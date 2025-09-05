def permute(bits, table):
    return ''.join(bits[i] for i in table)

def fk(subkey, right):
    ep = [3, 0, 1, 2, 1, 2, 3, 0]
    expanded = permute(right, ep)

    xor_result = ''.join(str(int(expanded[i]) ^ int(subkey[i])) for i in range(len(subkey)))

    s0 = [[1, 0, 3, 2],
          [3, 2, 1, 0],
          [0, 2, 1, 3],
          [3, 1, 3, 2]]

    s1 = [[0, 1, 2, 3],
          [2, 0, 1, 3],
          [3, 0, 1, 0],
          [2, 1, 0, 3]]

    row1 = int(xor_result[0] + xor_result[3], 2)
    col1 = int(xor_result[1] + xor_result[2], 2)
    s0_output = format(s0[row1][col1], '02b')

    row2 = int(xor_result[4] + xor_result[7], 2)
    col2 = int(xor_result[5] + xor_result[6], 2)
    s1_output = format(s1[row2][col2], '02b')

    s_output = s0_output + s1_output

    p4 = [1, 3, 2, 0]
    return permute(s_output, p4)

def sdes_encrypt(plain_text, k1, k2):

    ip = [1, 5, 2, 0, 3, 7, 4, 6]
    ip_result = permute(plain_text, ip)

    left, right = ip_result[:4], ip_result[4:]


    temp = left
    left = right
    right = ''.join(str(int(temp[i]) ^ int(fk(k1, right)[i])) for i in range(4))

    temp = left
    left = right
    right = ''.join(str(int(temp[i]) ^ int(fk(k2, right)[i])) for i in range(4))

    combined = left + right

    fp = [3, 0, 2, 4, 6, 1, 7, 5]
    cipher_text = permute(combined, fp)

    return cipher_text

plain_text = '01110010'
k1 = '10100100'
k2 = '10101000'


cipher_text = sdes_encrypt(plain_text, k1, k2)
print(f'Cipher Text: {cipher_text}')
