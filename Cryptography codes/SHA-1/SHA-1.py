import bitarray
from sha_dependencies import *
import time


def circular_left_shift(n, d):
    return ((n << d) | (n >> (32 - d))) & 0xFFFFFFFF


def preprocess_message(input_x):
    ba = bitarray.bitarray()
    ba.frombytes(input_x.encode('utf-8'))
    input_x_binary = ba.to01()
    n = len(input_x_binary)
    if not n % 512:
        return input_x_binary
    k = (448 - (n + 1)) % 512
    return input_x_binary + '1' + '0' * k + bin(n).lstrip('0b').zfill(64)


def message_schedule(x):
    words = [int(x[i:i + 32], 2) for i in range(0, len(x), 32)]
    for j in range(16, 80):
        words.append(words[j - 16] ^ words[j - 4] ^ words[j - 8] ^ words[j - 3])
    return words


def round_function(hash_state, k_constant, stage_function, message_j):
    new_hash = [(hash_state[-1] + stage_function(hash_state[1], hash_state[2], hash_state[3]) +
                circular_left_shift(hash_state[0], 5) + message_j + k_constant) & 0xffffffff, hash_state[0],
                circular_left_shift(hash_state[1], 30), hash_state[2], hash_state[3]]
    return new_hash


def calculate_hash(preprocessed_message):
    words = message_schedule(x=preprocessed_message)
    hash_result = initial_hash_values
    for i in range(80):
        hash_result = round_function(hash_result, k_constants[i // 20], stage_functions[i // 20], words[i])
    hash_result = [(initial_hash_values[i] + hash_result[i]) & 0xffffffff for i in range(5)]
    return hash_result


if __name__ == '__main__':
    plain_text = input("Enter the text to be hashed: ")
    start = time.time()
    preprocessed_text = preprocess_message(plain_text)
    print(len(preprocessed_text))
    calculated_hash = calculate_hash(preprocessed_text)
    end = time.time()
    hash_string = "".join([hex(val).lstrip('0x').zfill(8) for val in calculated_hash])
    print("HASH (IN HEX): {}\nLENGTH OF HASH: {}".format(hash_string, 4 * len(hash_string)))
    print("TIME TAKEN: {} seconds".format(end - start))








