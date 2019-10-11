import numpy as np


def hill_cipher_encryption():
    global plain_text, key
    n = len(plain_text)
    try:
        key_matrix = [[ord(key[i + j]) - ord('a') for i in range(n)] for j in range(0, n * n, n)]
        text_matrix = [[ord(c) - ord('a')] for c in plain_text]
        encryption_matrix = []
        for i, row in enumerate(key_matrix):
            temp = 0
            for j in range(n):
                temp += row[j] * text_matrix[j][0]
            encryption_matrix.append([temp % 26])
        return "".join(chr(a[0] + 97) for a in encryption_matrix), key_matrix
    except IndexError as e:
        print('The key is not of the length: {}. Error: {}'.format(n ** 2, e))


def hill_cipher_decryption(key_matrix, encrypted_message):
    try:
        n = len(key_matrix)
        key_matrix_inverse = np.linalg.det(np.asanyarray(key_matrix)) * np.linalg.inv(np.asanyarray(key_matrix))
        for i in range(n):
            for j in range(n):
                key_matrix_inverse[i][j] = key_matrix_inverse[i][j] % 26
        encrypted_matrix = np.asanyarray([[ord(c) - ord('a')] for c in encrypted_message])
        plain_text_matrix = []
        for i, row in enumerate(key_matrix_inverse):
            temp = 0
            for j in range(n):
                temp += int(encrypted_matrix[j][0] * row[j])
            plain_text_matrix.append([temp])
        print(plain_text_matrix)
        return "".join(chr(int(a[0] % 26) + 97) for a in plain_text_matrix)
    except np.linalg.LinAlgError as e:
        print("Not a Singular Matrix!")


if __name__ == '__main__':
    plain_text = input("PLAIN TEXT: ")
    key = (input("KEY: "))
    encryption = hill_cipher_encryption()
    print(encryption[0])
    decrypted_text = hill_cipher_decryption(encryption[1], "poh")
    print(decrypted_text)
