import bitarray
from DES_dependencies import *
import random
import time


def dec_to_bin(x):
    return int(bin(x)[2:])


def expansion_box(right_half_32) -> np.array:
    expanded_48 = np.zeros(48, dtype=int)
    for i in range(8):
        expanded_48[6 * i] = right_half_32[(4 * i - 1) % 32]
        for j in range(1, 5):
            expanded_48[6 * i + j] = right_half_32[4 * i + j - 1]
        expanded_48[6 * i + 5] = right_half_32[(4 * (i + 1)) % 32]
    return expanded_48


def function_f(key_48, right_half_32):
    right_half_48 = (expansion_box(right_half_32) + key_48) % 2
    temp_array = []
    for i in range(8):
        temp = np.array(list(str(dec_to_bin(s_boxes[i][int(str(right_half_48[6 * i]) + str(right_half_48[6 * i + 5]),
                        2)][int("".join(right_half_48[6 * i + 1: 6 * i + 5].astype(str)), 2)]))), dtype=int)
        if len(temp) is not 4:
            temp = np.append(np.zeros(4 - len(temp)), temp)
        temp_array.append(temp.astype(int))
    right_half_32 = np.asarray(temp_array).reshape((32,))
    return np.array([right_half_32[straight_p_box[i] - 1] for i in range(32)])


def key_generation(key_56):
    key_56, keys = np.asarray(key_56, dtype=int), []
    shift_values = [1 if i == 0 or 1 or 8 or 15 else 2 for i in range(16)]
    for i in range(16):
        key_56[0:28], key_56[28:56] = np.roll(key_56[0:28], -shift_values[i]), np.roll(key_56[28:56], -shift_values[i])
        keys.append(np.array([key_56[compression_p_box[i] - 1] for i in range(48)]))
    return keys


def encryption(key_56, input_string: str):
    if len(input_string) != 8:
        raise Exception("Enter a string of length 8!")
    # Convert the input string to bits
    bit_object = bitarray.bitarray()
    bit_object.fromstring(input_string)
    input_bits = np.array(bit_object.tolist(), dtype=int)
    # INITIAL PERMUTATION
    print("\nINPUT BITS: {}".format(input_bits))
    print("ENCRYPTION")
    input_bits = np.array([input_bits[initial_permutation[i] - 1] for i in range(64)])
    print("INITIAL PERMUTATION: {}".format(input_bits))
    left_half32, right_half32 = input_bits[0:32], input_bits[32:64]
    keys = key_generation(key_56)
    # print("LEFT: {}\nRIGHT: {}".format(left_half32, right_half32))
    for i in range(16):
        left_half32, right_half32 = right_half32, (function_f(keys[i], right_half32.copy()) + left_half32) % 2
        print("Stage {}: {}".format(i, np.append(left_half32, right_half32)))
        # print("LEFT: {}\nRIGHT: {}".format(left_half32, right_half32))
    # left_half32, right_half32 = function_f(keys[15], right_half32.copy()), right_half32  # For the last round; no swap
    encrypted_bits = np.append(left_half32, right_half32)
    # print("Final Permutation: {}".format(encrypted_bits))
    # FINAL PERMUTATION

    return np.array([encrypted_bits[final_permutation[i] - 1] for i in range(64)])


def decryption(key_56, cipher):
    # INITIAL PERMUTATION
    print("\nDECRYPTION")
    cipher = np.array([cipher[initial_permutation[i] - 1] for i in range(64)])
    print(cipher)
    left_half32, right_half32 = cipher[0:32], cipher[32:64]
    keys = key_generation(key_56)
    # left_half32, right_half32 = right_half32, function_f(keys[15], right_half32.copy())  # For the last round; no swap
    for i in range(16):
        left_half32, right_half32 = (function_f(keys[15 - i], left_half32.copy()) + right_half32) % 2, left_half32
        print("Stage {}: {}".format(i, np.append(left_half32, right_half32)))
    encrypted_bits = np.append(left_half32, right_half32)
    encrypted_bits = np.array([encrypted_bits[final_permutation[i] - 1] for i in range(64)])
    print("FINAL PERMUTATION: {}".format(encrypted_bits))
    return encrypted_bits


# [0 1 1 1 0 0 1 0 0 1 1 0 0 0 0 1 0 1 1 1 0 1 0 1 0 1 1 0 1 1 1 0 0 1 1 0 1
#  0 0 1 0 1 1 1 0 1 0 0 0 1 1 1 0 0 1 1 0 1 1 1 0 0 1 1]
# [0 1 1 1 0 0 1 0 0 1 1 0 0 0 0 1 0 1 1 1 0 1 0 1 0 1 1 0 1 1 1 0 0 1 1 0 1
#  0 0 1 0 1 1 1 0 1 0 0 0 1 1 1 0 0 1 1 0 1 1 1 0 0 1 1]
if __name__ == '__main__':
    key = [1 if random.randint(1, 3) == 2 else 0 for i in range(56)]
    print("KEY(56-bits): {}".format(key))
    text = input("Enter the text to be encrypted(8 letters at a time): ")
    start_time = time.time()
    encrypted = encryption(key, text)
    print("Encryption bits: {}".format(encrypted))
    decrypted_bits = decryption(key, encrypted)
    print("Decrypted bits: {}".format(decrypted_bits))
    print("Decrypted String: {}".format(bitarray.bitarray([True if val else False for val in decrypted_bits]).tobytes().
                                        decode('utf-8')))
    print("Time taken: {} seconds".format(time.time() - start_time))
