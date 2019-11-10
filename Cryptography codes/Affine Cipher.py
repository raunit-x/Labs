# Q1. c) Implement Affine Cipher.
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


def encryption(text, a, b):
    return "".join([chr(((ord(t) - ord('a')) * a + b) % 26 + ord('a')) for t in text])


def decryption(cipher, a_inv, b):
    return "".join([chr(((ord(c) - ord('a') - b) * a_inv) % 26 + ord('a')) for c in cipher])


def main():
    text = input("ENTER THE TEXT TO BE ENCRYPTED(a-z): ")
    a, b = 17, 20
    print("a: {}, b: {}".format(a, b))
    start = time.time()
    cipher = encryption(text, a, b)
    decrypted_text = decryption(cipher, a, b)
    a_inv = mod_inv(a, 26)
    if a_inv is None:
        print("The key is not invertible with respect to 26!")
        exit()
    cipher = encryption(text, a, b)
    decrypted_text = decryption(cipher, a_inv, b)
    end = time.time()
    print("CIPHER: {}".format(cipher))
    print("DECRYPTED TEXT: {}".format(decrypted_text))
    print("TIME TAKEN: {} seconds".format(end - start))


if __name__ == '__main__':
    main()
