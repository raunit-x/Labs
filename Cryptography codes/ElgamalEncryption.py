import os
import random


def generate_prime_number(prime_bit_length='512'):
    command_line_key = os.popen('openssl prime -generate -bits ' + prime_bit_length).readlines()
    return int(command_line_key[0].rstrip('\n'))


def fast_exponentiation(a, b, n):
    if b == 0:
        return 1 if a else 0
    temp = fast_exponentiation(a, b // 2, n)
    return ((temp * temp) % n * a) % n if b & 1 else (temp * temp) % n


def initialize_session(num_bits='512'):
    p = generate_prime_number(num_bits)
    alpha, d = random.randint(2, p // 2 - 2), random.randint(2, p - 2)
    beta = fast_exponentiation(alpha, d, p)
    return beta, alpha, p, d


def encryption(input_text, beta, alpha, p):
    i = random.randint(2, p - 2)
    mask_key, public_e = fast_exponentiation(beta, i, p), fast_exponentiation(alpha, i, p)
    cipher = (input_text * mask_key) % p
    return cipher, public_e, mask_key


def decryption(cipher, prime, public_key, d, mask_key):
    mask_key_inverse = fast_exponentiation(public_key, prime - d - 1, prime)
    # print("FERMAT'S THEOREM AT WORK: {}".format((mask_key * mask_key_inverse) % prime))
    return (cipher * mask_key_inverse) % prime


if __name__ == '__main__':
    beta_, alpha_, p_, d_ = initialize_session()
    text = input("Input the text to be encrypted: ")
    numbers = [int(ord(c)) for c in text]
    cipher_block = [encryption(n, beta_, alpha_, p_) for n in numbers]
    print("PUBLIC PARAMETERS:")
    print("   Beta: {}\n   Alpha: {}\n   Prime: {}\n   Public Key: {}".format(beta_, alpha_, p_, cipher_block[0][1]))
    print("ENCRYPTED BLOCK: {}".format("".join([str(c[0]) for c in cipher_block])))
    decrypted_block = [decryption(c[0], p_, c[1], d_, c[2]) for c in cipher_block]
    decrypted_string = "".join([chr(d) for d in decrypted_block])
    print("DECRYPTED STRING: {}".format(decrypted_string))
