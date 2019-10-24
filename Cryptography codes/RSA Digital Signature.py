import os
import sys
import random
sys.setrecursionlimit(10**8)

# The only difference from the RSA encryption is that the signature is produced using a private key and the verification
# of the signature is done using a public which is completely opposite of the RSA encryption


def generate_prime_number(prime_bit_length='512'):
    command_line_key = os.popen('openssl prime -generate -bits ' + prime_bit_length).readlines()
    return int(command_line_key[0].rstrip('\n'))


def fast_exponentiation(a, b, n):
    if b == 0:
        return 1 if a else 0
    temp = fast_exponentiation(a, b // 2, n)
    return ((temp * temp) % n * a) % n if b & 1 else (temp * temp) % n


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


def get_e(phi):
    for i in range(2, phi - 1):
        if extended_gcd(i, phi)[0] == 1:
            return i
    raise Exception("No e exists for this n")


def digital_signature(x, private_key):
    return fast_exponentiation(x, private_key, n)


def verify_signature(x, sig, public_key):
    return fast_exponentiation(sig, public_key, n) == x


if __name__ == '__main__':
    plain_text = input("Enter the text with which you wish to send the signature: ")
    num_bits = input("Number of bits for the prime numbers: ")
    p, q = generate_prime_number(num_bits), generate_prime_number(num_bits)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    print("Chosen primes:\np = [{}], q = [{}]".format(p, q))
    print("n = p * q = [{}]".format(n))
    print("Euler's Totient function, phi(n): [{}]".format(phi_n))
    e_public = get_e(phi_n)
    d_private = mod_inv(e_public, phi_n)
    # Map the plain text to the ring Z(n)
    plain_text_num = random.randint(1, n)
    signature = digital_signature(x=plain_text_num, private_key=d_private)
    print("Digital Signature: {}".format(signature))
    print("Verification of the digital Signature: {}".format("REAL!" if verify_signature(x=plain_text_num, sig=signature
                                                            , public_key=e_public) else "FAKE!"))
