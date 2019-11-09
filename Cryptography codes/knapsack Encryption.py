import numpy as np
import random
import os
import bitarray


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


# A secure Knapsack encryption: 200 weights with all of them having > 200 bit length
def init():
    a = [random.randint(1, 5)]
    for i in range(400):
        a.append(a[-1] + random.randint(1, 3))
    return a[200:]


def encryption(text, public_weights):
    ba = bitarray.bitarray()
    ba.fromstring(text)
    input_bits = ba.to01()
    print(input_bits)
    n = len(public_weights) - len(input_bits) % len(public_weights)
    input_bits += '0' * n
    encrypted_numbers = []
    for i in range(len(input_bits) // len(public_weights)):
        encrypted = 0
        for char, weight in zip(input_bits[i * len(public_weights):], public_weights):
            encrypted += (ord(char) - ord('0')) * weight
        encrypted_numbers.append(encrypted)
    return encrypted_numbers, n


def decryption(multiplier, modulus, public_weights, encrypted_numbers):
    multiplier_inverse = mod_inv(multiplier, modulus)
    private_weights = [(a * multiplier_inverse) % modulus for a in public_weights]
    print("PRIVATE WEIGHTS: {}".format(private_weights))
    decrypted_codes = []
    for num in encrypted_numbers:
        num, index, code = (num * multiplier_inverse) % modulus, len(private_weights) - 1, ''
        while index >= 0:
            flag = private_weights[index] <= num
            if flag:
                num -= private_weights[index]
            code += '1' if flag else '0'
            index -= 1
        decrypted_codes.append(code[::-1])
    return decrypted_codes


def main():
    private_weights = init()
    # private_weights = [1, 2, 4, 10, 20, 40]
    modulus, multiplier = private_weights[-1] + random.randint(100, 500), generate_prime_number('128')
    # modulus, multiplier = 110, 31
    text = input("Enter a message to be encrypted: ")
    public_weights = [(a * multiplier) % modulus for a in private_weights]
    print("PUBLIC KEY: {}".format(public_weights))
    encrypted_numbers, padding = encryption(text, public_weights)
    print("ENCRYPTED MESSAGE: {}".format(encrypted_numbers))
    decrypted_codes = decryption(multiplier, modulus, public_weights, encrypted_numbers)
    decrypted_codes[-1] = decrypted_codes[-1][: len(decrypted_codes[-1]) - padding]
    decrypted_string_code = "".join(decrypted_codes)
    print("DECRYPTED MESSAGE: {}".format("".join([chr(int(decrypted_string_code[i: i + 8], 2)) for i in range(0,
                                         len(decrypted_string_code), 8)])))


if __name__ == '__main__':
    main()


