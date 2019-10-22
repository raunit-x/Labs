import bitarray
import time
import os
import numpy as np
import sys
import random
sys.setrecursionlimit(10**8)


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    g, y, x = extended_gcd(b % a, a)
    return g, x - (b // a) * y, y


# Find square root in Zp where p = 3 mod 4
def sqrt_p_3_mod_4(a, p):
    r = pow(a, (p + 1) // 4, p)
    return r


# Find square root in Zp where p = 5 mod 8
def sqrt_p_5_mod_8(a, p):
    d = pow(a, (p - 1) // 4, p)
    r = 0
    if d == 1:
        r = pow(a, (p + 3) // 8, p)
    elif d == p - 1:
        r = 2 * a * pow(4 * a, (p - 5) // 8, p) % p
    return r


def generate_prime_number(prime_bit_length='512'):
    command_line_key = os.popen('openssl prime -generate -bits ' + prime_bit_length).readlines()
    return int(command_line_key[0].rstrip('\n'))


def encryption(num_bits, plain_text):
    p, q = generate_prime_number(num_bits), generate_prime_number(num_bits)
    n = p * q
    print("PUBLIC KEY FOR THE ENCRYPTION SIDE: {}".format(n))
    plain_text_int = random.randint(n // 2, n - 1)
    return (plain_text_int * plain_text_int) % n, n, p, q, {plain_text : plain_text_int}


def decryption(n, p, q, cipher_num, text_dictionary):
    r, s = 0, 0
    # find sqrt
    # for p
    if p % 4 == 3:
        r = sqrt_p_3_mod_4(cipher_num, p)
    elif p % 8 == 5:
        r = sqrt_p_5_mod_8(cipher_num, p)
    # for q
    if q % 4 == 3:
        s = sqrt_p_3_mod_4(cipher_num, q)
    elif q % 8 == 5:
        s = sqrt_p_5_mod_8(cipher_num, q)

    gcd, c, d = extended_gcd(p, q)
    x = (r * d * q + s * c * p) % n
    y = (r * d * q - s * c * p) % n
    candidate_decrypted_messages = [x, n - x, y, n - y]
    print("FOUR CANDIDATE DECRYPTED NUMBERS: {}".format(candidate_decrypted_messages))
    for key, value in zip(text_dictionary, text_dictionary.values()):
        if candidate_decrypted_messages.count(value):
            return key
    return candidate_decrypted_messages


if __name__ == '__main__':
    prime_num_bits = input("Enter the number of bits for the prime number: ")
    message = input("Enter the plain text to be encrypted: ")
    cipher, public_n, private_p, private_q, dictionary = encryption(num_bits=prime_num_bits, plain_text=message)
    print("ENCRYPTED MESSAGE: {}".format(cipher))
    print("PRIVATE KEYS:\np = [{}], q = [{}]".format(private_p, private_q))
    print("DECRYPTED MESSAGE: {}".format(decryption(public_n, private_p, private_q, cipher, dictionary)))

 
