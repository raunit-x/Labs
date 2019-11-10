# Q1. b) Implement Multiplicative Cipher.
import time


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    g, y, x = extended_gcd(b % a, a)
    return g, x - (b // a) * y, y


def mod_inv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        return None
    return x % m


def encryption(text, key):
    return "".join([chr(((ord(t) - ord('a')) * key) % 26 + ord('a')) for t in text])


def decryption(text, key_inverse):
    return "".join([chr(((ord(t) - ord('a')) * key_inverse) % 26 + ord('a')) for t in text])


def main():
    text = input("ENTER THE TEXT TO BE ENCRYPTED(a-z): ")
    key = int(input("ENTER THE KEY: "))
    key_inverse = mod_inv(key, 26)
    if key_inverse is None:
        print("The key is not invertible with respect to 26!")
        exit()
    start = time.time()
    cipher = encryption(text, key)
    decrypted_text = decryption(cipher, key_inverse)
    end = time.time()
    print("CIPHER: {}".format(cipher))
    print("DECRYPTED TEXT: {}".format(decrypted_text))
    print("TIME TAKEN: {} s".format(end - start))


if __name__ == '__main__':
    main()
