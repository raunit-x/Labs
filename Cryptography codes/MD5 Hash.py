# Q.2 g) Implement MD5 Hashing Algorithm.
import numpy as np
import math
import bitarray
import time


def left_rotate(x, c):
    return (x << c) or (x >> (32 - c))


def main():
    shift_values = np.zeros(64).astype(int)
    shift_values[0:16] = [7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22]
    shift_values[16:32] = [5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20]
    shift_values[32:48] = [4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23]
    shift_values[48:64] = [6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21]
    k = [abs(math.sin(i + 1)) * (2 ** 32) for i in range(64)]
    a0, b0, c0, d0 = 0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476
    functions = [lambda x, y, z: (x and y) or (~x and z), lambda x, y, z: (x and y) or (~z and y),
                 lambda x, y, z: x ^ y ^ z, lambda x, y, z: x ^ (y and ~z)]
    message = input("ENTER THE MESSAGE TO BE HASHED: ")
    ba = bitarray.bitarray()
    ba.fromstring(message)
    message = ba.to01()
    original_length = bin(len(message)).lstrip('0b').zfill(64)
    message = message + '1' + '0' * (448 - len(message) - 1) + original_length
    start = time.time()
    message_block = [int(message[i:i + 16], 2) for i in range(0, len(message), 16)]
    print("PROCESSED MESSAGE: {}\nLENGTH: {}".format(message, len(message)))
    a, b, c, d = a0, b0, c0, d0
    for i in range(64):
        if 0 <= i <= 15:
            idx = i
        elif 16 <= i <= 31:
            idx = (5 * i + 1) % 16
        elif 32 <= i <= 47:
            idx = (3 * i + 5) % 16
        else:
            idx = (7 * i) % 16
        f = int((functions[i // 16](b, c, d) + k[i] + message_block[idx] + a) % (2 ** 32))
        a = d
        d = c
        c = b
        b = (b + left_rotate(f, shift_values[i])) % (2 ** 32)
    a, b, c, d = (a + a0) % (2 ** 32), (b + b0) % (2 ** 32), (c + c0) % (2 ** 32), (d + d0) % (2 ** 32)
    hashed_binary = str(hex(a).lstrip('0x').zfill(4)) + str(hex(b).lstrip('0x').zfill(4)) + \
                    str(hex(c).lstrip('0x').zfill(4)) + str(hex(d).lstrip('0x').zfill(4))
    end = time.time()
    print("HASH: {}".format(hashed_binary))
    print("LENGTH OF THE HASH: {}".format(len(hashed_binary) * 4))
    print("TIME TAKEN: {} seconds".format(end - start))


if __name__ == '__main__':
    main()
