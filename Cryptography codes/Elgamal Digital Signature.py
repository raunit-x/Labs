import os
import sys
import random
import bitarray
sys.setrecursionlimit(10 ** 8)


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


def generate_prime_numbers(num_bits='1024'):
    if int(num_bits) < 1024:
        num_bits = '1024'
    return int(os.popen('openssl prime -generate -bits ' + num_bits).readlines()[0].rstrip('\n'))


def belongs_to_a_subgroup(generator_candidate, p):
    return (generator_candidate ** 2) % p != 1 and (generator_candidate ** 3) % p != 1


def get_public_parameters():
    num_bits = input("Enter the bit length of the prime numbers to be generated: ")
    p = generate_prime_numbers(num_bits)
    alpha = random.randint(2, p - 2)
    print("PUBLIC PARAMETERS: ")
    while not belongs_to_a_subgroup(alpha, p):
        alpha = random.randint(2, p - 2)
    print("P: [{}]".format(p))
    print("ALPHA: [{}]".format(alpha))
    return alpha, p


def set_up(public_parameters):
    alpha, p = public_parameters
    d = random.randint(2, p - 2)  # Private key
    beta = fast_exponentiation(alpha, d, p)
    return d, beta


def generate_signature(alpha, p, d):
    ephemeral_key = generate_prime_numbers('256')  # Any prime number or gcd(Ke, p - 1) == 1
    print("Ephemeral Key: [{}]".format(ephemeral_key))
    text = input("Enter the message for which the Digital Signature is to be generated: ")
    ba = bitarray.bitarray()
    ba.frombytes(text.encode('utf-8'))
    x = int(ba.to01(), 2) % p
    r = fast_exponentiation(alpha, ephemeral_key, p)
    s = ((x - d * r) * mod_inv(ephemeral_key, p - 1)) % (p - 1)
    return x, r, s


def verify_signature(beta, x, r, s, p, alpha):
    val = (fast_exponentiation(beta, r, p) * fast_exponentiation(r, s, p)) % p - fast_exponentiation(alpha, x, p)
    print("PROOF OF CORRECTNESS: {}".format(val))
    return not val


def main():
    alpha, p = get_public_parameters()
    d, beta = set_up((alpha, p))
    print("BETA: [{}]".format(beta))
    x, r, s = generate_signature(alpha, p, d)
    print("x: [{}]".format(x))
    print("r: [{}]".format(r))
    print("s: [{}]".format(s))
    print("VERIFIED!") if verify_signature(beta, x, r, s, p, alpha) else print("NOT VERIFIED!")


if __name__ == '__main__':
    main()
