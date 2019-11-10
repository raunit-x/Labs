# Q1. a) Implement Shift Cipher (or Caesar Cipher)
import time


def encryption(text, key):
    return "".join([chr((ord(t) - ord('a') + key) % 26 + ord('a')) for t in text])


def decryption(cipher, key):
    return "".join([chr((ord(c) - ord('a') - key) % 26 + ord('a')) for c in cipher])


def main():
    text = input("ENTER THE TEXT TO BE ENCRYPTED(a-z): ")
    key = int(input("ENTER THE SHIFT VALUE: "))
    start = time.time()
    cipher = encryption(text, key)
    decrypted_text = decryption(cipher, key)
    end = time.time()
    print("CIPHER: {}".format(cipher))
    print("DECRYPTED TEXT: {}".format(decrypted_text))
    print("TIME TAKEN: {} seconds".format(end - start))


if __name__ == '__main__':
    main()
