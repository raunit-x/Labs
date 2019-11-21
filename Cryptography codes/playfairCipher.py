import string


def find_char(key_matrix, c):
    for i in range(5):
        for j in range(5):
            if key_matrix[i][j] == c:
                return i, j
    return None


def generate_matrix_key(key):
    characters = dict.fromkeys(set(key), True)
    ascii_letters = string.ascii_lowercase.replace('j', '')
    key_matrix = [['.' for i in range(5)] for j in range(5)]
    index1, index2 = 0, 0
    for i in range(5):
        for j in range(5):
            if index1 < len(key):
                key_matrix[i][j] = key[index1]
                index1 += 1
            else:
                while ascii_letters[index2] in characters:
                    index2 += 1
                key_matrix[i][j] = ascii_letters[index2]
                index2 += 1
    print("KEY MATRIX: ")
    for row in key_matrix:
        print(row)
    return key_matrix


def encryption(text, key):
    key_matrix = generate_matrix_key(key)
    text += 'x' if len(text) & 1 else ''
    print("TEXT: {}".format(text))
    pairs = [(text[i], text[i + 1]) for i in range(0, len(text), 2)]
    cipher = ''
    print("TEXT PAIRS: {}".format(pairs))
    for val in pairs:
        point1, point2 = find_char(key_matrix, val[0]), find_char(key_matrix, val[1])
        if point1[0] == point2[0]:
            cipher += key_matrix[point1[0]][(point1[1] + 1) % 5] + key_matrix[point2[0]][(point2[1] + 1) % 5]
        elif point1[1] == point2[1]:
            cipher += key_matrix[(point1[0] + 1) % 5][point1[1]] + key_matrix[(point2[0] + 1) % 5][point2[1]]
        else:
            point3, point4 = (point1[0], point2[1]), (point2[0], point1[1])
            first = point3 if point3[0] == point1[0] else point4
            second = point4 if first == point3 else point3
            cipher += key_matrix[first[0]][first[1]] + key_matrix[second[0]][second[1]]
    print("CIPHER: {}".format(cipher))
    return cipher


def decryption(cipher, key):
    key_matrix = generate_matrix_key(key)
    print("CIPHER: {}".format(cipher))
    pairs = [(cipher[i], cipher[i + 1]) for i in range(0, len(cipher), 2)]
    print("CIPHER PAIRS: {}".format(pairs))
    text = ''
    for val in pairs:
        point1, point2 = find_char(key_matrix, val[0]), find_char(key_matrix, val[1])
        if point1[0] == point2[0]:
            text += key_matrix[point1[0]][(point1[1] - 1) % 5] + key_matrix[point2[0]][(point2[1] - 1) % 5]
        elif point1[1] == point2[1]:
            text += key_matrix[(point1[0] - 1) % 5][point1[1]] + key_matrix[(point2[0] - 1) % 5][point2[1]]
        else:
            point3, point4 = (point1[0], point2[1]), (point2[0], point1[1])
            first = point3 if point3[0] == point1[0] else point4
            second = point4 if first == point3 else point3
            text += key_matrix[first[0]][first[1]] + key_matrix[second[0]][second[1]]
    return text


def main():
    text = input("ENTER THE TEXT TO BE ENCRYPTED: ")
    key = input("ENTER THE KEY FOR ENCRYPTION: ")
    cipher = encryption(text=text, key=key)
    text_d = decryption(cipher=cipher, key=key)
    if len(text) & 1:
        text_d = text_d[:-1]
    print("DECRYPTED TEXT: {}".format(text_d))


if __name__ == '__main__':
    main()








