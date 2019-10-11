def encryption(message: str, key: str) -> str:
    return "".join([chr((ord(val) - ord('a') + ord(key[j % len(key)]) - ord('a')) % 26 + ord('a'))
                    for j, val in enumerate(message)])


def decryption(cipher: str, key: str) -> str:
    return "".join([chr((ord(val) - ord('a') - ord(key[j % len(key)]) + ord('a')) % 26 + ord('a'))
                    for j, val in enumerate(cipher)])


if __name__ == '__main__':
    text = input("Enter the text to be encrypted: ")
    key = input("Enter the key: ")
    print("Cipher: {}".format(encryption(text, key)))
    print("Decrypted plain text: {}".format(decryption(encryption(text, key), key)))
