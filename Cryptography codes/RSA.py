import os
import sys
sys.setrecursionlimit(10**8)


def generate_prime_number(prime_bit_length='512'):
    command_line_key = os.popen('openssl prime -generate -bits ' + prime_bit_length).readlines()
    return int(command_line_key[0].rstrip('\n'))


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


def get_e(a):
    for i in range(2, phi):
        if extended_gcd(i, phi)[0] == 1:  # gcd(e, phi(n)) == 1 and e Ε ring Z(phi) = {1, 2, ... phi(n) - 1}
            return i
    return None


def fast_exponentiation(a, b, n):
    if b == 0:
        return 1 if a else 0
    temp = fast_exponentiation(a, b // 2, n)
    return ((temp * temp) % n * a) % n if b & 1 else (temp * temp) % n


def encryption(s):
    return [fast_exponentiation(ord(x), e, n) for x in list(s)]


def decrypt_string(encrypted_list):
    return ''.join([chr(fast_exponentiation(x, d, n)) for x in encrypted_list])


if __name__ == '__main__':
    num_bits = input("Number of bits for the prime numbers: ")
    p = generate_prime_number(num_bits)
    q = generate_prime_number(num_bits)
    print("Chosen primes:\np = [{}], q = [{}]".format(p, q))
    n = p * q
    print("n = p * q = [{}]".format(n))
    phi = (p - 1) * (q - 1)
    print("Euler's Totient function, phi(n): [{}]".format(phi))
    e = get_e(n)
    if e is None:
        print("The entered numbers were not primes")
        exit()
    print("e = [{}]".format(e))
    d = mod_inv(e, phi)
    print("Your public key is a pair of numbers (e = [{}], n = [{}]).".format(e, n))
    print("Your private key is a pair of numbers (d = [{}], n = [{}]).".format(d, n))

    s = input("\nEnter a message to encrypt: ")
    print("Plain message: [{}]".format(s))
    encrypted_block = encryption(s)
    bit_string = "".join([bin(x).lstrip('0b').zfill(8) for x in encrypted_block])
    encrypted_string = "".join([chr(int(x, 2)) for x in [bit_string[i:i + 8] for i in range(0, len(bit_string), 8)]])
    print("\nEncrypted message: [{}]".format(encrypted_string))
    dec = decrypt_string(encrypted_block)
    print("Decrypted message: [{}]".format(dec))
