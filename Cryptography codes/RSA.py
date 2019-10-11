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
    for i in range(2, a):
        if extended_gcd(i, a)[0] == 1 and mod_inv(i, phi) is not None:
            return i
    return None


def fast_exponentiation(a, b, n):
    if b == 0:
        return 1 if a else 0
    temp = fast_exponentiation(a, b // 2, n)
    return ((temp * temp) % n * a) % n if b & 1 else (temp * temp) % n


def encrypt_string(s):
    return ''.join([chr(fast_exponentiation(ord(x), e, n)) for x in list(s)])


def decrypt_string(s):
    return ''.join([chr(fast_exponentiation(ord(x), d, n)) for x in list(s)])


p = int(input('Enter prime p: '))
q = int(input('Enter prime q: '))
print("Choosen primes:\np = {}, q = {}".format(p, q))
n = p * q
print("n = p * q = {}".format(n))
phi = (p - 1) * (q - 1)
print("Euler's function (totient) [phi(n)]: {}".format(phi))

e = get_e(n)
if e is None:
    print("The entered numbers were not primes")
    exit()
print("e = {}".format(e))
d = mod_inv(e, phi)
print("Your public key is a pair of numbers (e = {}, n = {}).".format(e, n))
print("Your private key is a pair of numbers (d = {}, n = {}).".format(d, n))

s = input("\nEnter a message to encrypt: ")
print("Plain message: {}".format(s))
enc = encrypt_string(s)
print("\nEncrypted message: {}".format(enc))
dec = decrypt_string(enc)
print("Decrypted message: {}".format(dec))