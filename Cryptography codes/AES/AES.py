from AES_dependencies import *
import os
import bitarray
import time


def master_key_generation_routine():
    command_line_key = os.popen('openssl enc -aes-128-cbc -k secret -P -md sha1').readlines()
    command_line_key = command_line_key[1].lstrip('key=').rstrip('\n')
    key_binary_string = bin(int(command_line_key, 16)).lstrip('0b').zfill(128)
    print(key_binary_string)
    return np.array(list(key_binary_string), dtype=int)


def round_key_generation_g_function(key_32, r_c_i):
    key_32 = np.roll(key_32, -8)
    key_32_copy = key_32.copy()
    for index in range(4):
        row_index, col_index = int("".join(key_32[8 * index:8 * index + 4].astype(str)), 2), int("".
                                                                                                 join(key_32[8 * index +
                                                                                                             4:8 * index
                                                                                                               + 8].
                                                                                                      astype(str)), 2)
        hex_substitution = s_box[row_index][col_index]
        left_array, right_array = np.array(list(bin(int(hex_substitution[0], 16)).lstrip('0b').zfill(4)), dtype=int), \
                                  np.array(list(bin(int(hex_substitution[1], 16)).lstrip('0b').zfill(4)), dtype=int)
        temp_8 = np.append(left_array, right_array)
        if not index:
            temp_8 = (temp_8 + r_c_i) % 2
        key_32_copy[8 * index: 8 * index + 8] = temp_8
    return key_32_copy


def round_key_generation(key_128):
    keys, temp_key = [key_128], key_128.copy()
    for index in range(9):
        key_128_temp = temp_key.copy()
        w0, w1, w2, w3 = key_128_temp[0:32], key_128_temp[32:64], key_128_temp[64:96], key_128_temp[96:128]
        w3_copy = round_key_generation_g_function(w3, r_c[index])
        w0 = (w0 + w3_copy) % 2
        w1 = (w0 + w1) % 2
        w2 = (w1 + w2) % 2
        w3 = (w2 + w3) % 2
        keys.append(np.append(np.append(w0, w1), np.append(w2, w3)))
    return np.array(keys)


def polynomial_modulo(polynomial1, polynomial2, prime_polynomial=AES_polynomial):
    polynomial3 = np.zeros(16, dtype=int)
    polynomial1, polynomial2 = polynomial1[::-1], polynomial2[::-1]
    for i_index in range(len(polynomial1)):
        for j_index in range(len(polynomial2)):
            polynomial3[i_index + j_index] = (polynomial3[i_index + j_index] + polynomial1[i_index] * polynomial2[
                j_index]) % 2
    if not polynomial3[8]:
        return polynomial3[0:8][::-1]
    polynomial3 = polynomial3[0:9][::-1]
    return ((polynomial3 + prime_polynomial) % 2)[1:9]


def substitution_layer(input_bits):
    for index in range(16):
        row_index = int("".join(input_bits[8 * index:8 * index + 4].astype(str)), 2)
        col_index = int("".join(input_bits[8 * index + 4: 8 * index + 8].astype(str)), 2)
        a, b = s_box[row_index][col_index][0], s_box[row_index][col_index][1]
        binary_a, binary_b = np.array(list(bin(int(a, 16)).lstrip('0b').zfill(4)), dtype=int), np.array(list(bin(int(b, 16)).
                                                                                                    lstrip('0b').zfill(4)),
                                                                                               dtype=int)
        binary_a = np.append(np.zeros(4 - len(binary_a)), binary_a).astype(int)
        binary_b = np.append(np.zeros(4 - len(binary_b)), binary_b).astype(int)
        input_bits[8 * index:8 * index + 8] = np.append(binary_a, binary_b)
    return input_bits


def row_shift_layer(input_bits):
    try:
        reshaped_input_bits = input_bits.reshape((4, 32))
        for index in range(4):
            reshaped_input_bits[index, :] = np.roll(reshaped_input_bits[index, :], -8 * index)
        return reshaped_input_bits.reshape((128,))
    except ValueError as error:
        print("Size of the input is not 128 bits long, ERROR: [{}]".format(error))
        return None


def col_shift_layer(input_bits):
    try:
        reshaped_input_bits = input_bits.reshape((4, 32))
        for index in range(4):
            b_prime = reshaped_input_bits[:, 8 * index: 8 * index + 8]
            temp = np.zeros(b_prime.shape).astype(int)
            for index_j in range(4):
                for k in range(4):
                    temp[index] += polynomial_modulo(col_shift_matrix[index_j][k], b_prime[k])
            reshaped_input_bits[:, 8 * index: 8 * index + 8] = temp
        return reshaped_input_bits.reshape((128,))
    except ValueError as error:
        print("Size of the input is not 128 bits long, ERROR: [{}]".format(error))
        return None


def encryption(input_string: str):
    bit_object = bitarray.bitarray()
    bit_object.fromstring(input_string)
    input_bits = np.array(bit_object.tolist(), dtype=int)
    print("Input bits: [{}]".format(",".join(input_bits.astype(str))))
    key_128 = master_key_generation_routine()
    print("KEY: [{}]".format(",".join(key_128.astype(str))))
    print("KEY LENGTH: [{}]".format(len(key_128)))
    keys = round_key_generation(key_128)
    for index in range(10):
        input_bits = substitution_layer(input_bits)
        input_bits = row_shift_layer(input_bits)
        input_bits = col_shift_layer(input_bits)
        input_bits = (input_bits + keys[index]) % 2
    return input_bits


if __name__ == '__main__':
    text = input("Enter the input(16 bytes): ")
    if len(text) is not 16:
        raise Exception("Text length not 16!")
    start_time = time.time()
    encrypted_bits = encryption(text)
    print("ENCRYPTED BITS: [{}]".format(",".join(encrypted_bits.astype(str))))
    try:
        print("ENCRYPTED STRING(UTF-16): [{}]".format(
            bitarray.bitarray([True if val else False for val in encrypted_bits]).tobytes().decode('utf-16')))
        print(
            "ENCRYPTED STRING(UTF-32): [{}]".format(
                bitarray.bitarray([True if val else False for val in encrypted_bits]).tobytes().decode('utf-32')))
        print(
            "ENCRYPTED STRING(UTF-8): [{}]".format(
                bitarray.bitarray([True if val else False for val in encrypted_bits]).tobytes().decode('utf-8')))
    except UnicodeDecodeError as e:
        ascii_string = ''
        for i in range(16):
            char = chr(int("".join(encrypted_bits[8 * i:8 * i + 8].astype(str)), 2))
            ascii_string += char
        print("ASCII DECODING: [{}]".format(ascii_string))
    print("ENCRYPTION TIME: {}seconds".format(time.time() - start_time))
